# OBSERVA - SOC Incident & Alert Manager (SIAM)

**OBSERVA** is a lightweight open
![Python Version](https://img.shields.io/badge/python-3.12-blue)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Fredyp/Observa-SIAM)
![GitHub last commit](https://img.shields.io/github/last-commit/Fredyp/Observa-SIAM)
![GitHub issues](https://img.shields.io/github/issues/Fredyp/Observa-SIAM)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Fredyp/Observa-SIAM)
 source web application designed to help Security Operations Center (SOC) teams manage alerts, incidents, and client reporting workflows with efficiency and transparency.

## 🚀 Core Features
- Web-based interface styled with [Milligram CSS](https://milligram.io/) for a minimalist responsive design
- Client management and alert tracking
- Calendar-based email log tracking per client
- PDF report generation
- Email delivery system
- Modular structure for extensibility

## 🛠 Tech Stack
- Python 3.x
- Flask
- Jinja2
- SQLite
- pdfkit & wkhtmltopdf (for PDF generation)
- Milligram (CSS framework)

## 🔧 Setup Instructions
```bash
git clone https://github.com/Fredyp/Observa-SIAM.git
cd Observa-SIAM
bash scripts/install.sh
```

## 🙌 Author
Created by [Fredy Peralta](https://www.linkedin.com/in/fredyperaltagaleano/)

---

## ✅ Requirements

- Python 3.10+
- pip
- wkhtmltopdf installed and available in PATH (for PDF generation)
- Linux/Ubuntu-based environment recommended
- Docker (optional, for containerized deployments)

---

## 🗺 Roadmap

- [x] MVP release with PDF generation and client alert tracking
- [ ] Add user authentication
- [ ] Add role-based access control (RBAC)
- [ ] Implement API for integration with SIEM
- [ ] Alert classification by severity
- [ ] Email delivery and scheduling system
- [ ] Real-time dashboard with alert KPIs
- [ ] Docker and Kubernetes deployment support
