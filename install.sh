#!/bin/bash

# Install script for Linux/WSL

MINICONDA_DIR="./miniconda3"
ENV_NAME="youpuller_env"

echo "Starting installation for Linux/WSL..."

# Check if Miniconda is already installed
if [ ! -d "$MINICONDA_DIR" ]; then
  echo "Downloading Miniconda installer..."
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
  echo "Installing Miniconda locally..."
  bash miniconda.sh -b -p $MINICONDA_DIR
  rm miniconda.sh
else
  echo "Miniconda already installed."
fi

# Initialize conda
source "$MINICONDA_DIR/etc/profile.d/conda.sh"

# Create environment if it doesn't exist
if conda info --envs | grep $ENV_NAME; then
  echo "Conda environment $ENV_NAME already exists."
else
  echo "Creating conda environment $ENV_NAME..."
  conda create -y -p $MINICONDA_DIR/envs/$ENV_NAME python=3.9
fi

# Activate environment
conda activate $MINICONDA_DIR/envs/$ENV_NAME

# Install required packages
echo "Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Installation complete. To activate the environment, run:"
echo "source $MINICONDA_DIR/etc/profile.d/conda.sh"
echo "conda activate $MINICONDA_DIR/envs/$ENV_NAME"
