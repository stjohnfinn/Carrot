#!/bin/bash

###################
# Set up code dependencies
###################

# Create virtual environment, if it doesn't exist
if [ ! -d "venv" ]; then
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

###################
# Create directories
###################

# Create screenshots directory
mkdir -p screenshots

# Create sound_files directory
mkdir -p sound_files
