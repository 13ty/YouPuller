#!/bin/bash

MINICONDA_DIR="./miniconda3"
ENV_NAME="youpuller_env"

echo "Uruchamianie aplikacji na Linux/WSL..."

# Initialize conda
source "$MINICONDA_DIR/etc/profile.d/conda.sh"

# Activate environment
conda activate $MINICONDA_DIR/envs/$ENV_NAME

# Run the Flask app
python frontend/app.py
