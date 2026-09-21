# Objectives
The objectives of this lab session are as follows:
1. To learn how to use the GPUs on the Chichester 1 lab machines for running machine learning experiments
2. To understand best practice for experimental setup, result tracking and version control.


# Overview
1. Get started with WSL/VSCode/Jupter on the lab machines
2. Clone this project and get started using uv for package management
3. Create and link a [wandb](https://wandb.ai/) account, run the classifier experiment and visualise the results.
4. Change the experimental setup in (hydra) and save results to wandb
5. Push this project to your GitHub account.


## 1. Machine Setup
See the guide [here]().

## 2. Project Startup
Within a WSL terminal session (possibly in VSCode) 
``` bash
cd ~/
git clone https://github.com/ivorsimpson/cim-lab-0
cd cim-lab-0
uv sync
```

to test that it works, type
``` bash
uv run 
```

## 3. Weights and Biases
Make an account at [wandb.ai](https://wandb.ai/).



## 4. Experimental Tracking
We are using [Hydra](https://hydra.cc/docs/intro/) for experimental setup, which allows us to use .yaml files to hold our experimental parameters.

## 5. Version control
Git is the industry standrard for version control, and we encourage you to use GitHub to store information. Please follow the process detailed [here](https://github.com/ivorsimpson/cim-lab-0/blob/main/GithubSupport.md).






