#!/bin/bash

echo "Installing dependencies"
pip install -r requirements.txt

echo "Starting up webserver"
flask run --host=0.0.0.0
