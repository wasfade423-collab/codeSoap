# SmartPort Gateway - API SOAP (Python Pur)

Ce composant fait partie du système SmartPort Gateway du Port Autonome de Cotonou. Il s'agit d'une API SOAP développée exclusivement en Python 3 sans framework externe. Elle interagit avec la base de données MySQL pour exposer les services d'extraction de données de fret.

---

## Architecture Spécifique

```text
smartport/
│
├── config.py
├── db.py
├── server.py
├── services.py
├── templates.py
└── requirements.txt