#!/bin/bash
# Install Conda if needed (or use apt-get for other system dependencies)
curl -LO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -f -p /app/miniconda

# Set Conda path
export PATH="/app/miniconda/bin:$PATH"

# Install Conda environment from environment.yml
conda env create -f environment.yaml

# Activate the Conda environment
source activate pkaani

python setup.py install
