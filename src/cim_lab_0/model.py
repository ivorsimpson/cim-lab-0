"""A small configurable multilayer perceptron for MNIST."""

import torch
from torch import nn


class MNISTClassifier(nn.Module):
    """Fully connected classifier with a configurable depth and width."""

    def __init__(self, hidden_layers: int, hidden_neurons: int) -> None:
        super().__init__()

        if hidden_layers < 0:
            raise ValueError("hidden_layers must be non-negative")
        if hidden_layers > 0 and hidden_neurons < 1:
            raise ValueError("hidden_neurons must be positive")

        layers: list[nn.Module] = [nn.Flatten()]
        input_features = 28 * 28

        for _ in range(hidden_layers):
            layers.extend(
                [
                    nn.Linear(input_features, hidden_neurons),
                    nn.ReLU(),
                ]
            )
            input_features = hidden_neurons

        layers.append(nn.Linear(input_features, 10))
        self.network = nn.Sequential(*layers)

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        """Return class logits for a batch of MNIST images."""

        return self.network(images)
