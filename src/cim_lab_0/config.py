"""Hydra structured configuration for the MNIST experiment."""

from dataclasses import dataclass, field

from hydra.core.config_store import ConfigStore


@dataclass
class ModelConfig:
    """Configuration for the fully connected classifier."""

    hidden_layers: int = 2
    hidden_neurons: int = 128


@dataclass
class DataConfig:
    """Configuration for MNIST loading."""

    root: str = "data"
    batch_size: int = 128
    num_workers: int = 2


@dataclass
class TrainingConfig:
    """Configuration for optimisation."""

    epochs: int = 5
    learning_rate: float = 1e-3

@dataclass
class LoggingConfig:
    """Configuration for experiment logging."""
    use_wandb: bool = False
    project: str = "cim-lab-0"
@dataclass
class ExperimentConfig:
    """Complete experiment configuration."""

    seed: int = 42
    model: ModelConfig = field(default_factory=ModelConfig)
    data: DataConfig = field(default_factory=DataConfig)
    training: TrainingConfig = field(default_factory=TrainingConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)


def register_config() -> None:
    """Register the structured configuration with Hydra."""

    ConfigStore.instance().store(name="mnist_config", node=ExperimentConfig)
