# SmartPort Gateway - API SOAP

## 📌 Présentation

SmartPort Gateway est une API SOAP développée en Python permettant la gestion et le suivi des dossiers de transit portuaire. Elle offre des services web conformes au protocole SOAP pour créer, consulter et suivre les dossiers de transit au sein de la plateforme SmartPort.

L'application est connectée à une base de données PostgreSQL hébergée sur Render afin d'assurer la persistance et la disponibilité des données.

---

## 🚀 Fonctionnalités

* Création d'un dossier de transit
* Consultation d'un dossier via sa référence métier
* Suivi du statut d'un dossier
* Génération automatique du contrat WSDL
* Réponses conformes au standard SOAP
* Initialisation automatique de la base de données

---

## 🏗️ Architecture du Projet

Le projet est organisé en plusieurs couches afin de garantir une bonne séparation des responsabilités.

### `server.py`

Serveur HTTP principal chargé de :

* Servir le fichier WSDL via les requêtes GET
* Recevoir les requêtes SOAP via les requêtes POST
* Transmettre les données aux services métier
* Retourner les réponses SOAP appropriées

### `services.py`

Contient la logique métier de l'application :

* Analyse du contenu XML SOAP
* Validation des données reçues
* Appel des fonctions de gestion des dossiers
* Construction des réponses SOAP

### `db.py`

Responsable de :

* La connexion à PostgreSQL
* La création automatique de la table `dossiers`
* L'exécution des requêtes SQL
* La gestion des erreurs liées à la base de données

### `templates.py`

Contient :

* Les modèles XML SOAP
* Les enveloppes SOAP (SOAP Envelope)
* La définition du contrat WSDL

---

## 🗄️ Structure de la Base de Données

Lors du premier appel à l'opération `CreateDossier`, l'application vérifie automatiquement l'existence de la table `dossiers`.

Si celle-ci n'existe pas, elle est créée avec la structure suivante :

```sql
CREATE TABLE dossiers (
    id SERIAL PRIMARY KEY,
    reference_metier VARCHAR(255) NOT NULL UNIQUE,
    statut VARCHAR(50) NOT NULL,
    type_operation VARCHAR(100) NOT NULL
);
```

### Description des colonnes

| Colonne          | Description                        |
| ---------------- | ---------------------------------- |
| id               | Identifiant unique du dossier      |
| reference_metier | Référence métier unique du dossier |
| statut           | État actuel du dossier             |
| type_operation   | Type d'opération de transit        |

---

## ⚙️ Prérequis

* Python 3.10 ou supérieur
* PostgreSQL
* Connexion Internet (si utilisation de Render)

---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/votre-compte/smartport-gateway.git

cd smartport-gateway
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
```

### 3. Activer l'environnement

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 🔧 Configuration

Créer un fichier `.env` à la racine du projet :

```env
DB_HOST=xxxxx
DB_PORT=5432
DB_NAME=xxxxx
DB_USER=xxxxx
DB_PASSWORD=xxxxx
```

---

## ▶️ Lancement du serveur

```bash
python server.py
```

Le serveur démarre par défaut sur :

```text
http://localhost:8000
```

---

## 📄 Accès au WSDL

Le contrat WSDL est accessible via :

```text
GET /?wsdl
```

Exemple :

```text
http://localhost:8000/?wsdl
```

---

## 🔗 Services SOAP Disponibles

### CreateDossier

Permet de créer un nouveau dossier.

#### Paramètres

| Paramètre        | Type   |
| ---------------- | ------ |
| reference_metier | String |
| statut           | String |
| type_operation   | String |

---

### GetDossier

Permet de consulter les informations d'un dossier.

#### Paramètre

| Paramètre        | Type   |
| ---------------- | ------ |
| reference_metier | String |

---

## 📬 Exemple de Requête SOAP

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
   <soapenv:Body>
      <CreateDossierRequest>
         <reference_metier>REF001</reference_metier>
         <statut>EN_COURS</statut>
         <type_operation>IMPORT</type_operation>
      </CreateDossierRequest>
   </soapenv:Body>
</soapenv:Envelope>
```

---

## 📤 Exemple de Réponse SOAP

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
   <soapenv:Body>
      <CreateDossierResponse>
         <message>Dossier créé avec succès</message>
      </CreateDossierResponse>
   </soapenv:Body>
</soapenv:Envelope>
```

---

## 🛡️ Gestion des Erreurs

L'application gère notamment :

* Les références métier dupliquées
* Les données manquantes
* Les erreurs de connexion PostgreSQL
* Les requêtes SOAP invalides
* Les erreurs internes du serveur

---

## 📚 Technologies Utilisées

* Python
* PostgreSQL
* SOAP
* XML
* HTTP Server (Python Standard Library)
* Render

---

## 👨‍💻 Auteur

Développé dans le cadre du projet **SmartPort Gateway**.

**Groupe 1**

Supervisé par **Mr Osias TOSSOU**.
