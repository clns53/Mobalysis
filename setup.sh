#!/bin/bash
sudo apt update
sudo apt install postgresql postgresql-contrib -y
sudo -u postgres psql -c "CREATE USER mob_db_user PASSWORD 'mob_db_pass'"
sudo useradd -m -d /home/mob_app_usr mob_app_usr