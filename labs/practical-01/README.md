# comp5122m


# Install pyenv if not already installed
curl https://pyenv.run | bash

# Add to ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

# Install Python versions
pyenv install 3.10.12
pyenv install 3.12.12

# Set as local version for your project
cd /path/to/your/comp5122m/project
pyenv local 3.12.12

# Verify
python --version

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
    "scipy"
]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"

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

jupyter-notebook