#!/bin/sh
sudo apt update
sudo apt upgrade -y
# upgrade to python 3.10
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10 -y
sudo apt install python3.10-venv -y
sudo apt install python3.10-dev -y
sudo apt install apache2 -y

sudo python3.10 -m ensurepip --upgrade



