[![Python 3.12](https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3120/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com)

# Global Climate Attitudes and Eco-Anxiety Analysis

![PartI](docs/Report_PartI.pdf)
![PartII](docs/Report_PartII.pdf)

**BSc Computer Science — COMP5122M Data Science – Coursework Parts I & II**
**University of Leeds, School of Computing, 2025/26**

This repository contains the complete data analysis pipeline for the **UNDP Peoples’ Climate Vote 2024** dataset. The work is divided into two coursework components:

- **Part I (Exploratory Data Analysis)** – Investigates age‑group differences in support for renewable energy transition using descriptive statistics, heatmaps, and grouped bar charts.
- **Part II (Predictive Modelling & Clustering)** – Builds supervised models (logistic regression, random forest) to predict support for strengthening climate commitments, and applies unsupervised clustering (k‑means, PCA) to create a country typology.

---

## Project Overview

The UNDP Peoples’ Climate Vote 2024 is the largest public opinion survey on climate change, covering 73 countries and more than half of the global population. The dataset is aggregated by country, age group, and education level, capturing attitudes toward:

- urgency of replacing fossil fuels with renewable energy,
- trust in governments, businesses, and international organisations,
- personal experience of extreme weather events,
- support for strengthening national climate commitments.

This project answers two central research questions:

1. **Is there a consistent age gap across countries** in the desire to transition away from fossil fuels? (Part I)
2. **Which demographics and attitudes best predict support for stronger climate commitments**, and how can countries be grouped into meaningful typologies? (Part II)

All analyses are reproducible and follow best practices for code quality, version control, and dependency management.

## Repository Structure

```bash
project-root/
├── data/                   # Raw CSV
├── docs/                   # Final PDF reports (Part I and Part II)
│     ├── Report_PartI.pdf
│     └── Report_PartII.pdf
├── notebooks/              # Jupyter Notebooks with full analysis
│     ├── PartI.ipynb       # Data cleaning, EDA, visualisations
│     └── PartII.ipynb      # Preprocessing, modelling, clustering
├── .pre-commit-config.yaml # Pre‑commit hooks (formatting, linting)
├── pyproject.toml          # Project metadata and uv dependencies
└── README.md               # This file

```

*Note: You can download the raw dataset from the [official data centre](https://peoplesclimate.vote/data-center).*

## Setup Instructions

### 1. Install Python with `pyenv` (recommended)

```bash
  # Install pyenv if not already installed
  curl https://pyenv.run | bash

  # Add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  source ~/.bashrc

  # Install Python version 3.12 and set locally
  pyenv install 3.12.12
  pyenv local 3.12.12

```

### 2. Install uv and synchronise dependencies

```bash
  # Sync all dependencies from the pyproject.toml file without cache
  uv sync --all-groups -n

  # Install pre‑commit hooks
  uv run pre-commit install
  uv run pre-commit autoupdate

  # (Optional) Upgrade the lock file
  uv lock --upgrade
  uv lock --check

```

### 3. Configure Jupyter kernel

```bash
  # Activate the virtual environment
  source .venv/bin/activate

  # Install the kernel for the uv environment
  python -m ipykernel install --user --name=comp5122m --display-name="Python (uv-env)"

  # Verify kernels
  jupyter kernelspec list

```

### 4. Launch JupyterLab / Notebook

```bash
  jupyter lab   # or jupyter notebook --autoreload

```

#### Useful JupyterLab Shortcuts

> **Recommended JupyterLab shortcuts** (add via Settings → Advanced Settings Editor → Keyboard Shortcuts):
> - `Shift C, Shift C` → clear all cell outputs
> - `Shift J, Shift J` → clear current cell output

**See JSON**

```json
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

```

## Reproducing the Analysis

1. **Download the dataset** from [peoplesclimate.vote/data-center](https://peoplesclimate.vote/data-center) and place the CSV file(s) inside the `data/` folder.
2. Open `notebooks/PartI.ipynb` and run all cells – this performs data cleaning, exploratory analysis, and generates figures for the age‑gap investigation.
3. Open `notebooks/PartII.ipynb` and run all cells – this builds predictive models, evaluates them (accuracy, F1, balanced accuracy), and applies clustering to identify country typologies.
4. Generated reports are saved as PDF in the `docs/` folder (these are the final submissions).

---

## Key Dependencies

All dependencies are managed via `uv` and pinned in `pyproject.toml`. The main libraries used:

- `pandas`, `numpy` – data manipulation
- `matplotlib`, `seaborn`, `plotly` – visualisation
- `scikit‑learn` – preprocessing, models (logistic regression, random forest, clustering), metrics
- `imbalanced-learn` – handling class imbalance (SMOTE)
- `jupyter` – interactive notebooks

See `pyproject.toml` for the complete list.

---

## Assessment & Academic Integrity

This work was completed as part of the **COMP5122M Data Science** module at the University of Leeds.
**GenAI tools are strictly prohibited** for both coursework components (RED status per the assessment briefs).
All code, analyses, and written interpretations are original and produced by the named group members.

---

## License

Distributed under the **Mozilla Public License Version 2.0**.
