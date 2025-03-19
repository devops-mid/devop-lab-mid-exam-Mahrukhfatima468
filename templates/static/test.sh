#!/bin/bash

# Exit script on error
set -e

echo "Running tests..."

# Check if tests directory exists
if [ ! -d "tests" ]; then
    echo "Error: tests directory not found!"
    exit 1
fi

# Run unit tests
python3 -m unittest discover -s tests -p "*.py"

echo "All tests passed successfully!"
