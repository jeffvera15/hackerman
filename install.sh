#!/bin/bash

echo "Installing dependencies..."
pip3 install -r requirements.txt

echo "Making script executable..."
chmod +x gui.py

echo "Run the program using: python3 gui.py"
