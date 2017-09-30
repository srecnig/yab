#!/bin/bash

echo "Installing dependencies"
pip install -r requirements.txt

echo "Starting up webserver"
su backend -c "python webserver.py"
