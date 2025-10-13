#!/bin/bash
# Nav to Data Science dir
cd ../.../mnt/fast-data/github-projects/uni/comp5122m/

# Ensure compatible version in use
pyenv local 3.12.12
poetry env use 3.12.12

# Start shell which has all the packages
poetry shell

# Start notebook to access jupyter notebook(s)
jupyter-notebook

