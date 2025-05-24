# Installation Guide – OBSERVA

This guide will help you get OBSERVA up and running on a local server (Ubuntu recommended).

---

## 🖥 Prerequisites

Make sure the following are installed:

- Python 3.10 or higher
- pip
- wkhtmltopdf (`sudo apt install wkhtmltopdf`)
- git (optional for cloning)

---

## 🚀 Installation Steps

### 1. Clone or download the repository

```bash
git clone https://github.com/Fredyp/Observa-SIAM.git
cd Observa-SIAM
```

Or download the ZIP release and extract it:

```bash
unzip OBSERVA_v1.0.0_release_complete.zip
cd OBSERVA_webapp_v1_release
```

---

### 2. Create a virtual environment and activate it

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the application

```bash
python app.py
```

Then access it via your browser at:

```
http://localhost:5000
```

---

## 🧪 Optional

To generate PDFs, make sure `wkhtmltopdf` is installed and accessible in your system PATH.

```bash
sudo apt install wkhtmltopdf
```

---

## 📬 Questions or issues?

Feel free to open an issue on the GitHub repository:
[https://github.com/Fredyp/Observa-SIAM/issues](https://github.com/Fredyp/Observa-SIAM/issues)
