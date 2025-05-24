#!/bin/bash
set -e

echo "🔧 Installing system dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip python3-venv wkhtmltopdf unzip

echo "📁 Setting up directory..."
sudo mkdir -p /opt/observa
sudo unzip OBSERVA.zip -d /opt/
sudo mv /opt/OBSERVA_webapp_v1_release/* /opt/observa
sudo rm -r /opt/OBSERVA_webapp_v1_release
cd /opt/observa

echo "🐍 Creating venv..."
python3 -m venv venv
source venv/bin/activate

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "🛠 Enabling systemd service..."
cat <<EOF | sudo tee /etc/systemd/system/observa.service
[Unit]
Description=OBSERVA - SOC Alert Manager WebApp
After=network.target

[Service]
User=root
WorkingDirectory=/opt/observa
ExecStart=/opt/observa/venv/bin/python app.py
Restart=always
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable observa
sudo systemctl start observa

echo "✅ Running at http://<your-server-ip>:5000"
