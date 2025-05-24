# 📦 OBSERVA Installation Guide

This guide installs and runs OBSERVA on a fresh Ubuntu server.

---

## 🔧 Requirements

- Python 3.10+
- pip
- wkhtmltopdf (for PDF reports)
- unzip

---

## 🚀 Steps

```bash
unzip OBSERVA.zip
cd OBSERVA_webapp_v1_release

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch (development mode)
flask run --host=0.0.0.0 --port=5000
```

---

## 🔐 Default Login

- **User**: `admin`
- **Pass**: `admin`

Use `/register` to create more users.

---

## ⚙ Optional systemd setup

Use `deploy.sh` to automate install + service creation.
