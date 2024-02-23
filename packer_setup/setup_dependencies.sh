#!/bin/bash

# Install the required packages
sudo groupadd csye6225
sudo useradd -g csye6225 -s /usr/sbin/nologin csye6225

sudo dnf install -y zip unzip

sudo unzip /tmp/csye6225.zip -d /home/packer/csye6225
sudo chown -R csye6225:csye6225 /home/packer/csye6225

# Install dependencies
pip3 install pipenv --user
cd /home/packer/csye6225 && pipenv install --python 3.11 
pipenv run python manage.py migrate

#move the service file to /etc/systemd/system
sudo mv /home/packer/csye6225/packer_setup/webapp.service /etc/systemd/system
sudo chown root:root /etc/systemd/system/webapp.service
sudo chmod 644 /etc/systemd/system/webapp.service

# Check the validation of service file
sudo systemd-analyze verify webapp.service

# Reload the systemd daemon
sudo systemctl daemon-reload

# Start the webapp service
sudo systemctl enable webapp.service
sudo systemctl start webapp.service
sudo systemctl status webapp.service
