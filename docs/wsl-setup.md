# Student installation guide

This script creates a private Ubuntu 24.04 WSL 2 distribution, installs Python through `uv`, installs CUDA-enabled PyTorch, and verifies that PyTorch can run on the NVIDIA GPU.

> **Before starting:** Use a University Windows laboratory machine on which WSL 2 and the NVIDIA Windows driver are already available. You do **not** need Windows administrator access.

## Install steps

Firstly, we need to verify if wsl is installed on your machine: 

```powershell
wsl --status
wsl --version
wsl --list --verbose
```

It is normal for the distribution list to be empty on a new student profile.

To install WSL on your lab machine you will need to install a script with Powershell. Please follow the steps in the following guide precisely to complete the installation. 

## Download the script from Github 

The latest version of the install script is hosted on github. To obtain the install script please open a powershell terminal and run 

```powershell
cd $HOME\Downloads
curl.exe -O https://github.com/<user>/<repo>/archive/refs/heads/<branch>.zip
```

Once the `zip` file is downloaded please unzip the file: 

```powershell
Expand-Archive -Path file.zip -DestinationPath .
```

The unzipped files should now be located in your Downloads directory. **Please make sure that `sussex-cim-bootstrap.ps1` in your Downloads directory before proceeding.**

To use the script please allow the downloaded script for this session:
    
```powershell
Unblock-File .\sussex-cim-bootstrap.ps1
```

We are now ready to smoke test the install script. Please execute the following command.  

```powershell
.\sussex-cim-bootstrap.ps1 -Name cim-smoke -SkipLaunch
```

Expected output looks like:

```
Python: 3.12.x
PyTorch: <installed version>
PyTorch CUDA runtime: 12.6
CUDA available: True
GPU: NVIDIA <model>
PASS: PyTorch completed a CUDA matrix multiplication
```


> **Rerunning is safe.** If a network download or package installation is interrupted, run the same command again. Existing WSL, Python and package components are reused.

Once the installation is confirmed we will reuse the last command to generate a new project environment, if necessary. 

## Using the Environment

After successfully installing the environment we can activate WSL with the following command: 

```powershell
wsl -d LabGPU
```

Please note that you are now in a Linux virtual environment. This will change the way you navigate. For example, while Powershell uses `\` for level delineation, Linux is unix based and will use `/`. 

To navigate to the project directory use `cd` to move in your file system: 

```bash
cd ~/projects/
```

You have now successfully installed WSL and are ready to run code with CUDA GPU support. To finalise the setup change directory into `cim-smoke` and run `uv run src/gpu-test.py`. You can exit WSL with `exit` in the terminal. 

## Additional Information
### What the script installs

- An Ubuntu 24.04 WSL 2 distribution named `LabGPU`, registered only for the current Windows user.
- A Linux account matching your Windows username, with administrative rights inside `LabGPU` only.
- Basic development tools, including Git, curl and a C/C++ build toolchain.
- `uv`, used to install and manage Python and Python environments.
- A selectable Python version (default: Python 3.12).
- CUDA-enabled PyTorch and torchvision (default wheel channel: CUDA 12.6).
- JupyterLab and common computational imaging packages: NumPy, SciPy, scikit-image, matplotlib, Pillow, tifffile and tqdm.
- A project under `~/projects/<project-name>`, including a private `.venv` and a GPU verification program.

> **CUDA driver model:** The NVIDIA display driver remains on Windows. Do not install an NVIDIA Linux display driver inside WSL — PyTorch uses the GPU interface exposed by the Windows driver.

### Where files are stored

| Item                          | Location                                                 |
| ----------------------------- | -------------------------------------------------------- |
| WSL distribution storage      | `%LOCALAPPDATA%\SussexWSL\LabGPU`                        |
| Downloaded Ubuntu image cache | `%LOCALAPPDATA%\SussexWSL\cache`                         |
| Projects inside WSL           | `/home/<username>/projects/<name>`                       |
| Windows view of a project     | `\\wsl.localhost\LabGPU\home\<username>\projects\<name>` |
| PowerShell transcript         | `%TEMP%\cim-bootstrap-YYYYMMDD-HHMMSS.log`               |
### Troubleshooting the install

**The script is not digitally signed**

```powershell
Unblock-File .\sussex-cim-bootstrap.ps1
```

Do not run `Set-ExecutionPolicy` as part of the normal instructions. University policy may override it and display an alarming but harmless warning. After reviewing the script, use `Unblock-File` and run it directly. If execution is still blocked, inspect the effective policies with:

```powershell
Get-ExecutionPolicy -List
```

If `MachinePolicy` or `UserPolicy` is `AllSigned`, unblocking is not sufficient — the centrally managed policy requires a trusted digital signature. In that case, use an institutionally signed copy of the script rather than trying to override the policy.

**`LabGPU` already exists** This is normally expected — the script reuses and repairs the existing distribution. Check it with:

```powershell
wsl --list --verbose
wsl -d LabGPU -u root -- cat /etc/os-release
```

**GPU is not visible**

```powershell
wsl -d LabGPU -- /usr/lib/wsl/lib/nvidia-smi
```

If this fails, the Windows NVIDIA driver or WSL GPU support is unavailable on that machine. Installing a Linux display driver inside `LabGPU` will not fix the Windows host configuration.

**PyTorch reports `CUDA available: False`**

```powershell
wsl -d LabGPU
cd ~/projects/<project-name>
~/.local/bin/uv run --python .venv/bin/python python src/check_gpu.py
```

Confirm the project used a CUDA `TorchChannel` rather than `cpu`. If necessary, recreate the project with a CUDA channel.

**A download or installation was interrupted** Run the same bootstrap command again — the Ubuntu image, `uv` downloads and package caches are reused where possible.

**Find the detailed log**

```powershell
Get-ChildItem $env:TEMP\cim-bootstrap-*.log | Sort-Object LastWriteTime -Descending | Select-Object -First 1
```
