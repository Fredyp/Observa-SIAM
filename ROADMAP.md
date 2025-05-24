# 🗺 OBSERVA Technical Roadmap

This document outlines the prioritized development plan for OBSERVA, the SOC Incident & Alert Manager.

---

## ✅ Completed Features

- User login with hashed password storage (SQLite)
- Admin-only registration panel
- Deployment automation (`deploy.sh`)
- Flask app styled with Milligram
- Logo and branding integrated

---

## 🚧 In Progress / Next Priorities

### 1. 🎫 Ticketing System

- [ ] Model: `Ticket`
- [ ] Fields: title, description, status (received, analyzed, escalated, resolved, closed)
- [ ] Assigned user, creation timestamps

### 2. 🕒 Timeline & Evidence Tracking

- [ ] Model: `IncidentEvent`
- [ ] Relation to `Ticket`
- [ ] Evidence upload support (PDFs, screenshots, logs)
- [ ] Timestamped updates

### 3. 🧠 Classification & Risk

- [ ] Fields: incident type (phishing, malware, etc.), severity level
- [ ] Filtering and color-coded severity indicators

### 4. 👥 User Roles & Shift Control

- [ ] Roles: `admin`, `analyst`, `csirt`
- [ ] Permissions for each role
- [ ] User filtering by shift/turno
- [ ] Add to registration form and admin UI

---

## 🔮 Future Features

- [ ] SIEM integration (syslog or API)
- [ ] Dashboards (MTTD, MTTR, open/closed tickets)
- [ ] Email/webhook notifications
- [ ] Threat Intel ingestion
- [ ] Knowledge Base: playbooks and incident library
