#!/bin/bash

# Exit script on any error
set -e

echo "Starting build process..."

# Ensure Python3 and pip3 are installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 not found. Installing..."
    sudo apt update && sudo apt install -y python3 python3-pip
fi

# Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip3 install --upgrade pip
    pip3 install -r requirements.txt
else
    echo "Error: requirements.txt not found!"
    exit 1
fi

echo "Build process completed successfully!"
