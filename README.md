# OBSERVA: SOC Incident & Alert Manager

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen)
![Made with Flask](https://img.shields.io/badge/made%20with-Flask-blue)
![Uses Milligram](https://img.shields.io/badge/CSS%20Framework-Milligram-lightgrey)
![Python Version](https://img.shields.io/badge/python-3.12-blue)

![OBSERVA Logo](static/img/observa_logo.png)

---

## 🧩 Overview

**OBSERVA** is a lightweight SOC alert and report manager designed for security teams. Built with Flask, it supports user access, PDF reports, evidence tracking, and operational dashboards.

---

## ✅ Features

- 👥 Multi-user login with secure password hashing
- 🧾 Ticket creation with status, category, and severity
- 🕒 Incident timeline with evidence upload (PCAP, PDF, logs, etc.)
- 📊 Dashboard metrics (Total/Open/Closed, MTTR, Category Breakdown)
- 🎨 Responsive UI with Milligram CSS + branding
- 🛡 Secure headers, session policies, filename sanitization
- 📦 Automated deployment (`deploy.sh`) and systemd service

---

## 📂 Functional Pages

- `/login` – User login
- `/register` – Admin-only user registration
- `/tickets` – Ticket listing, creation, filters
- `/timeline` – View incident timeline, upload evidence
- `/dashboard` – Visual KPIs for SOC operations

---

## 📇 Author

Developed by [Fredy Peralta](https://www.linkedin.com/in/fredyperaltagaleano/)

---
