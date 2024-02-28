#!/bin/bash

# Install the required packages
sudo groupadd csye6225
sudo useradd -g csye6225 -s /usr/sbin/nologin csye6225

sudo dnf install -y zip unzip

sudo unzip /tmp/csye6225.zip -d /opt/app
sudo mkdir -p /opt/app/.venv
sudo chmod 777 /opt/app/.venv
sudo chown -R csye6225:csye6225 /opt/app

# Install dependencies
cd /opt/app && pipenv install --python 3.11

#move the service file to /etc/systemd/system
sudo mv /opt/app/packer_setup/webapp.service /etc/systemd/system
sudo chown root:root /etc/systemd/system/webapp.service

# Reload the systemd daemon
sudo systemctl daemon-reload

# Start the webapp service
sudo systemctl enable webapp.service
sudo systemctl start webapp.service
# sudo systemctl status webapp.service
