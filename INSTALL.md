# 📦 Installation Guide – OBSERVA

This guide walks you through setting up OBSERVA on a local server.

---

## ✅ Prerequisites

- Python 3.10+
- pip
- wkhtmltopdf (`sudo apt install wkhtmltopdf`)
- git (optional)

---

## ⚙️ Installation

### 1. Clone or extract the project

```bash
unzip OBSERVA_v1.0.0_release.zip
cd OBSERVA_webapp_v1_release
```

### 2. Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
bash run.sh
```

Then visit: `http://<your-server-ip>:5000`

---

## 🧪 Optional

To enable PDF generation:

```bash
sudo apt install wkhtmltopdf
```

---

## 🆘 Need help?

Open an issue here: [https://github.com/Fredyp/Observa-SIAM/issues](https://github.com/Fredyp/Observa-SIAM/issues)
