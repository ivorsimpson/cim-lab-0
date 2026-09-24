# Objectives
The objectives of this lab session are as follows:
1. To learn how to use the GPUs on the Chichester 1 lab machines for running machine learning experiments
2. To understand best practice for experimental setup, result tracking and version control.


# Overview
1. Get started with WSL/VSCode/Jupter on the lab machines
2. Clone this project and get started using uv for package management
3. Train a classifier and change the experimental setup using (hydra)
4. Create and link a [wandb](https://wandb.ai/) account, run the classifier experiment and visualise the results.
5. Push this project to your GitHub account.


## 1. Machine Setup
If you're using one of the Windows lab machines, please follow the guidance [here](docs/wsl-setup.md).

Please note that WSL installs on the local machine, not on your network drive and it's not guaranteed to persist indefinitely. This is excellent motivation to back up all your code using GitHub and model artefacts (weights, training information) on wandb. It is also possible to mount your network filesystem.

## 2. Project Startup
Within a WSL terminal session (from VSCode, if you like) 
``` bash
cd ~/
git clone https://github.com/ivorsimpson/cim-lab-0
cd cim-lab-0
uv sync
```

## 3. Training a classifier

to test that it works, type
``` bash
uv run python -m cim_lab_0.train 
```

where you can adjust configurable aspects of the model architecture and training setup (as given in config.py) from the command line e.g.
``` bash
uv run python -m cim_lab_0.train  model.hidden_layers=1 model.hidden_neurons=32 seed=7 training.learning_rate=0.005
```


## 3. Weights and Biases
Make an account at [wandb.ai](https://wandb.ai/).


## 5. Version control
Git is the industry standrard for version control, and we encourage you to use GitHub to store information. Please follow the process detailed [here](docs/github-support.md).
