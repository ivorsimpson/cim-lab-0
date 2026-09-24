# Weights & Biases (W&B)

Weights & Biases (W&B) is a platform for tracking machine learning experiments. We will use it to record experiment settings, results and model checkpoints.

## Create an account

Create an account at [wandb.ai](https://wandb.ai/).

## Login

From a WSL terminal, run:

```bash
uv run wandb login
```

Copy your API key from the W&B website and paste it into the terminal.

## Run an experiment

Our training script has a config option for W&B. Run an experiment with W&B enabled:

```bash
uv run python -m cim_lab_0.train logging.use_wandb=true
```

## Explore your run

Open the W&B dashboard in your browser. Your run should appear in the `cim-lab-0` project.

Inspect the run to find:
* Training and test metrics
* Loss and accuracy curves
* The Hydra configuration used for the run

## Compare experiments

Run another experiment with a different configuration:

```bash
uv run python -m cim_lab_0.train \
    logging.use_wandb=true \
    model.hidden_layers=1 \
    model.hidden_neurons=32
```

Compare the two runs and observe how the different model configurations affect the results.

Important outputs, such as model weights and checkpoints, should always be stored in W&B. This provides a backup of your experiments and avoids relying on local WSL storage.
