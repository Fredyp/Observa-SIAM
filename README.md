# SIAM - SOC Incident & Alert Manager (MVP)

**SIAM** es una aplicación web ligera desarrollada en Flask para equipos SOC (Security Operations Center). Permite crear reportes en PDF de eventos o alertas de seguridad para clientes, y llevar un historial de reportes enviados.

> 🧪 Este es un MVP (Producto Mínimo Viable). Fue diseñado para ser funcional, simple y servir de base para agregar nuevas características como autenticación, calendario, y más.

---

## ✨ Características

- Gestión de clientes (nombre, contacto de email)
- Creación de reportes en formato PDF por cliente
- Plantillas HTML listas para personalizar
- Generación de historial de envíos
- Aplicación ligera, ideal para servidores con pocos recursos

---

## 🧰 Requisitos

- Ubuntu 20.04 o superior
- Python 3.10+
- 2 CPU y 1 GB RAM mínimo
- Acceso a Internet para instalar dependencias

---

## 🚀 Instalación rápida

```bash
# 1. Clona el repositorio o descarga el ZIP
git clone https://github.com/tuusuario/siam_webapp.git
cd siam_webapp

# 2. Da permisos y ejecuta el instalador
chmod +x install.sh
./install.sh

# 3. Activa el entorno virtual
source venv/bin/activate

# 4. Ejecuta la aplicación
flask run --host=0.0.0.0 --port=5000
```

La aplicación estará disponible en `http://<IP_DE_TU_SERVIDOR>:5000`.

---

## 📝 Estructura del proyecto

```
siam_webapp/
├── app.py                  # Aplicación principal Flask
├── install.sh              # Instalador de dependencias y PDFKit
├── requirements.txt        # Dependencias de Python
├── templates/
│   ├── index.html
│   ├── create_report.html
│   └── report_template.html
├── static/                 # (opcional para CSS)
├── reports/                # Carpeta para los PDFs generados
└── README.md
```

---

## 🔧 Próximas funciones (roadmap)

- [ ] Autenticación de usuarios (login/logout)
- [ ] Sistema de historial y calendario de envíos
- [ ] Clasificación de alertas por tipo (Malware, Phishing, etc.)
- [ ] Envío automatizado de reportes por email
- [ ] KPIs del SOC en tiempo real
- [ ] Dockerfile para contenedorizar la aplicación

---

## 📖 Licencia

Este proyecto es open-source y se publica bajo la licencia [MIT](LICENSE).

---

## 🤝 Contribuciones

¡Contribuciones son bienvenidas! Si tienes ideas o mejoras, por favor crea un issue o un pull request.

---

## 🙌 Autor

Desarrollado por un analista SOC con experiencia práctica en gestión de alertas, incidentes y necesidades reales del equipo.