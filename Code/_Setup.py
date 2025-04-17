### _setup.py ###
# This file is used to handle the imports of the notebooks for ease of use and consistency with 
# variable names. Should be called at the top of the notebooks.

# @author AL, TP

import subprocess
import os
import sys
from pathlib import Path


# Function to install dependencies
def install_requirements(requirements_file="requirements.txt"):
    """Installs dependencies from a requirements.txt file."""
    if os.path.exists(requirements_file):
        print(f"Installing dependencies from {requirements_file}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
            print("All dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
            sys.exit(1)
    else:
        print(f"Error: {requirements_file} not found!")
        sys.exit(1)


# Call the function to install requirements.txt

# install_requirements()

# Get the current script directory
script_dir = Path(__file__).parent.resolve()

# get project root directory
project_root = script_dir.parent.resolve()

# Construct path to data
data_path = project_root / "Data"

test_path = data_path / "test.json"
train_path = data_path / "train.json"
submission_path = data_path / "sample_submission.csv"

# Path to external datasets
external1 = data_path / "external_dataset_1.json"
external2 = data_path / "external_dataset_2.json"
external3 = data_path / "external_dataset_3.json"
external4 = data_path / "external_dataset_4.csv"

# Import necessary libraries
import pandas as pd
import numpy as np