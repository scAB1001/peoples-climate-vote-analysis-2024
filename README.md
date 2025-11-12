# comp5122m

### Install python versions with pyenv

```bash
# Install pyenv if not already installed
curl https://pyenv.run | bash

# Add to ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

# Install Python versions
pyenv install 3.8.20
pyenv install 3.10.12
pyenv install 3.12.12
pyenv install 3.14.0
```

#### Commands

```bash
# Set versions for your project
pyenv global 3.10.12

cd /path/to/your/comp5122m/project
pyenv local 3.12.12

# Verify
python --version
```

### pyproject.toml

```bash
[project]
name = "comp5122m"
version = "0.1.0"
description = ""
authors = [
    {name = "Andreas Bazigos",email = "sc222ab@leeds.ac.uk"}
]
package-mode = false
readme = "README.md"
requires-python = ">=3.11"  # ← Match your actual Python 3.12
dependencies = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "scipy",
    "openpyxl",
    "ipykernel"

]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

#### Commands

```bash
python3 -m pip install poetry
poetry init


# Remove ALL Poetry cache and environments
rm -rf ~/.cache/pypoetry/
rm -rf ~/.config/pypoetry/

# Also remove any local Poetry files
rm -f poetry.lock

# Environment
poetry env remove 3.10.19 # --all
poetry env use 3.12.12
poetry env list

# Activate venv
poetry config --list
poetry config virtualenvs.in-project true
poetry self add poetry-plugin-shell
poetry shell

poetry add [package]
poetry lock --no-cache --regenerate
poetry install
```

### JupyterLab configuration

"shortcuts": [
  {
    "command": "notebook:clear-all-cell-outputs",
    "keys": [
    "Shift C",
    "Shift C"
    ],
    "selector": ".jp-Notebook:focus"
  },
  {
    "command": "notebook:clear-cell-output",
    "keys": [
    "Shift J",
    "Shift J"
    ],
    "selector": ".jp-Notebook:focus"
  },
]

#### Commands

```bash
# redhat
jupyter-notebook

# linux mint 22.2
poetry run jupyter-notebook
```

### Local Development

```bash
# Register the Poetry environment as a Jupyter kernel
python -m ipykernel install --user --name=poetry-climate-env --display-name="Poetry Climate Env"

# Run the command directly using poetry run
poetry run python -m ipykernel install --user --name=poetry-climate-env --display-name="Poetry Climate Env"

# List available Jupyter kernels
jupyter kernelspec list
```

Available kernels:
- comp5122m /uolstore/home/student_lnxhome01/sc222ab/.local/share/jupyter/kernels/comp5122m
- poetry-climate-env /uolstore/home/student_lnxhome01/sc222ab/.local/share/jupyter/kernels/poetry-climate-env
- python3 /uolstore/home/student_lnxhome01/sc222ab/.local/share/jupyter/kernels/python3
