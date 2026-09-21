"""Train a configurable MNIST classifier with Hydra.

Example:
    uv run python -m cim_lab_0.train model.hidden_layers=3 \
        model.hidden_neurons=256 seed=7
"""

import random
from pathlib import Path

import hydra
import numpy as np
import torch
from omegaconf import DictConfig, OmegaConf
from torch import nn
from torch.optim import Adam
from torch.utils.data import DataLoader

from cim_lab_0.config import register_config
from cim_lab_0.data import make_dataloaders
from cim_lab_0.model import MNISTClassifier

register_config()


def set_seed(seed: int) -> None:
    """Seed Python, NumPy and PyTorch for a more reproducible run."""

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def run_epoch(
    model: nn.Module,
    loader: DataLoader,
    loss_function: nn.Module,
    device: torch.device,
    optimizer: Adam | None = None,
) -> tuple[float, float]:
    """Run one training or evaluation epoch."""

    training = optimizer is not None
    model.train(training)

    total_loss = 0.0
    total_correct = 0
    total_examples = 0

    with torch.set_grad_enabled(training):
        for images, labels in loader:
            images = images.to(device, non_blocking=True)
            labels = labels.to(device, non_blocking=True)

            if training:
                optimizer.zero_grad()

            logits = model(images)
            loss = loss_function(logits, labels)

            if training:
                loss.backward()
                optimizer.step()

            batch_size = labels.size(0)
            total_loss += loss.item() * batch_size
            total_correct += (logits.argmax(dim=1) == labels).sum().item()
            total_examples += batch_size

    return total_loss / total_examples, total_correct / total_examples


@hydra.main(version_base=None, config_name="mnist_config")
def main(cfg: DictConfig) -> None:
    """Run one configured training experiment."""

    set_seed(cfg.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Hydra may change the run directory, so resolve data relative to the repo root.
    project_root = Path(hydra.utils.get_original_cwd())
    data_root = project_root / cfg.data.root

    train_loader, test_loader = make_dataloaders(
        root=str(data_root),
        batch_size=cfg.data.batch_size,
        num_workers=cfg.data.num_workers,
        seed=cfg.seed,
        use_cuda=device.type == "cuda",
    )

    model = MNISTClassifier(
        hidden_layers=cfg.model.hidden_layers,
        hidden_neurons=cfg.model.hidden_neurons,
    ).to(device)

    loss_function = nn.CrossEntropyLoss()
    optimizer = Adam(model.parameters(), lr=cfg.training.learning_rate)


    print(f"Using device: {device}")
    print(OmegaConf.to_yaml(cfg))

    for epoch in range(1, cfg.training.epochs + 1):
        train_loss, train_accuracy = run_epoch(
            model,
            train_loader,
            loss_function,
            device,
            optimizer,
        )
        test_loss, test_accuracy = run_epoch(
            model,
            test_loader,
            loss_function,
            device,
        )

        metrics = {
            "epoch": epoch,
            "train/loss": train_loss,
            "train/accuracy": train_accuracy,
            "test/loss": test_loss,
            "test/accuracy": test_accuracy,
        }

        print(
            f"Epoch {epoch:02d} | "
            f"train loss {train_loss:.4f} | "
            f"train accuracy {train_accuracy:.3%} | "
            f"test accuracy {test_accuracy:.3%}"
        )

    model_path = project_root / "mnist_classifier.pt"
    torch.save(model.state_dict(), model_path)



if __name__ == "__main__":
    main()
