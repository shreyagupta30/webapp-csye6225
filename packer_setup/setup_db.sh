#!/bin/bash

# Update and upgrade system
echo "System update in progress..."
sudo dnf update -y && sudo dnf upgrade -y

# Check and install pip
if ! command -v pip &> /dev/null; then
    echo "Installing pip..."
    sudo dnf install -y python3-pip
else
    echo "pip is already present."
fi

# Install pipenv
echo "Setting up pipenv..."
pip3 install pipenv

# Install Python 3.11
echo "Installing Python 3.11..."
sudo dnf install -y python3.11

# Install PostgreSQL 16 if it's not installed
if ! command -v psql &> /dev/null; 
then
    echo "PostgreSQL 16 not found. Installing now..."
    sudo dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
    # Disable the built-in PostgreSQL module
    sudo dnf -qy module disable postgresql
    sudo dnf install -y postgresql16-server

    sudo /usr/pgsql-16/bin/postgresql-16-setup initdb
    sudo systemctl enable postgresql-16
    sudo systemctl start postgresql-16
else
    echo "PostgreSQL 16 is already present."

echo "Setup process completed."
fi
