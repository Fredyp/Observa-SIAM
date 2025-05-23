#!/bin/bash
sudo apt update
sudo apt install -y python3-venv wkhtmltopdf
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Run with: source venv/bin/activate && flask run --host=0.0.0.0 --port=5000"
