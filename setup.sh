#!/bin/bash

# Check if python is installed:
if ! command -v python3.12 &> /dev/null
then
	echo "[SETUP] Python3 not installed. Start installation..."
	
	# Install correct python version using apt.
	sudo apt update
	sudo apt upgrade
	sudo add-apt-repository ppa:deadsnakes/ppa -y
	sudo apt install python3.12-{tk,dev,dbg,venv,gdbm,distutils}
	sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1

	echo "[SETUP] Python3 installation done."
else
	echo "[SETUP] Python3 found."
fi

# Check if pip3 is installed.
if ! command -v pip3 &> /dev/null
then
	echo "[SETUP] pip3 not installed. Start installation..."

	# Install pip3.
	sudo apt update
	sudo apt install python3-pip
	echo "[SETUP] pip3 installation done."
else
	echo "[SETUP] pip3 found."
fi

# Check if venv installed:
if dpkg -s python3-venv &> /dev/null; then
    echo "[SETUP] venv found."
else
    echo "[SETUP] venv non installed. Start installation..."
    # Install venv. 
    sudo apt update
    sudo apt install python3-venv
    echo "[SETUP] venv installation done."
fi

# Set env name.
env_name="env"

# Build virtual environment.
python3 -m venv ${env_name}

# Activate venv and launch setup.
${env_name}/bin/pip3 install -r requirements.txt

echo "[SETUP] Done."

sleep 5s
