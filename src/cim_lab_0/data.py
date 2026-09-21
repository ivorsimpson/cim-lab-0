"""MNIST download and DataLoader construction."""

from pathlib import Path

import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


def make_dataloaders(
    root: str,
    batch_size: int,
    num_workers: int,
    seed: int,
    use_cuda: bool,
) -> tuple[DataLoader, DataLoader]:
    """Download MNIST if needed and return training and test loaders."""

    data_root = Path(root).expanduser().resolve()
    transform = transforms.ToTensor()

    train_dataset = datasets.MNIST(
        root=data_root,
        train=True,
        download=True,
        transform=transform,
    )
    test_dataset = datasets.MNIST(
        root=data_root,
        train=False,
        download=True,
        transform=transform,
    )

    generator = torch.Generator().manual_seed(seed)
    loader_options = {
        "batch_size": batch_size,
        "num_workers": num_workers,
        "pin_memory": use_cuda,
    }

    train_loader = DataLoader(
        train_dataset,
        shuffle=True,
        generator=generator,
        **loader_options,
    )
    test_loader = DataLoader(
        test_dataset,
        shuffle=False,
        **loader_options,
    )
    return train_loader, test_loader
