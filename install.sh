#!/bin/bash

#3: Clone the repository into the home directory of mob_app_usr:
cd /home/mob_app_usr
sudo git clone https://github.com/AzubiAfrica/Mobalysis.git
cd ~

#4:Install python3-venv:
sudo apt update
sudo apt install -y python3-venv

#Create an empty database with the name mobalytics:
sudo -u postgres psql -c "create database mobalytics"

#Set the owner of the mobalytics database to mob_db-user:
sudo -u postgres psql -c "ALTER DATABASE mobalytics OWNER TO mob_db_user"
sudo -u postgres psql -c "CREATE ROLE root LOGIN;"

#5: Adding environment variables and values to mob_app_usr's bashrc file:
sudo chmod 777 /home/mob_app_usr/.bashrc
sudo echo -e "export DBNAME=mobalytics
export DBUSER=mob_db_user
export DBPASS=mob_db_pass
export DBHOST=localhost
export DBPORT=5432  " >> /home/mob_app_usr/.bashrc
source /home/mob_app_usr/.bashrc

#6: Install application packages for backend in virtual environment:
#Create a virtual environment called env:
sudo apt update
sudo apt install python3-pip -y
sudo python3 -m venv /home/mob_app_usr/env

#Activate the virtual environment:
source /home/mob_app_usr/env/bin/activate

#Install application packages in the virtual environment:
sudo pip3 install -r /home/mob_app_usr/Mobalysis/backend/requirements.txt

#Make any new migrations by executing:
sudo python3 /home/mob_app_usr/Mobalysis/backend/manage.py makemigrations

#Install the backend migrations
sudo python3 /home/mob_app_usr/Mobalysis/backend/manage.py migrate