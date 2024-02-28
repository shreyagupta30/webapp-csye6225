#!/bin/bash

# Update and upgrade system
echo "System update in progress..."
sudo dnf update -y && sudo dnf upgrade -y

# Install Python 3.11
echo "Installing Python 3.11..."
sudo dnf install -y python3.11
python3.11 -m ensurepip --default-pip
pip3.11 install pipenv

