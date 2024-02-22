#!/bib/bash

sudo groupadd csye6225
sudo useradd -g csye6225 -s /usr/sbin/nologin csye6225

# Unzip project
sudo dnf install -y zip unzip
sudo unzip /tmp/csye6225.zip -d /home/csye6225
sudo chown -R csye6225:csye6225 /home/csye6225

# Install dependencies
cd /home/csye6225/csye6225 && pipenv install -python 3.11
pipenv run python manage.py migrate

#systemd setup
