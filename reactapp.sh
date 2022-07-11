#!/bin/bash
sudo apt-get update
sudo apt-get install curl -y
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install nginx -y
sudo git clone https://github.com/AzubiAfrica/Mobalysis.git
cd Mobalysis/frontend
sudo npm install
sudo npm run build
sudo rm -rf /var/www/html/*
sudo cp -r /home/ubuntu/Mobalysis/frontend/build/* /var/www/html/.