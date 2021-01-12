#!/bin/bash

echo "UBUNTU POST-INSTALL SCRIPT"

echo "Updating APT..."

sudo aptget update
sudo aptget upgrade

echo"Installing SNAPD"
sudo apt install snapd

clear

echo "Installing base packages"

sudo apt-get install --yes git git-extras build-essential python3-pip htop glances

echo "Installing vscode as a Snap package"

sudo snap install --classic code
sudo snap install teams-for-linux
sudo snap install discord
