#!/bin/bash
# Nav to Data Science dir
cd ~/code/comp5122m/labs

# Ensure compatible version in use
pyenv local 3.12.12

# Start shell which has all the packages
poetry shell

# Start notebook to access jupyter notebook(s)
jupyter-notebook

