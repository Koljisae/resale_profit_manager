#!/bin/bash

apt-get install python3-pip
echo "Building the project..."
pip install --no-cache-dir -r requirements.txt

echo "Make Migration..."
python3.9 manage.py makemigrations --no-input
python3.9 manage.py migrate --no-input

echo "Collect Static..."
python3.9 manage.py collectstatic --no-input

echo "Add Settings to Model..."
python3.9 manage.py command_settings_query
