# DevOps-Project-Two-Tier-Flask-App-using-AWS

## How to Test Locally (Without Docker)

1. Go to the **app** directory:

```bash
   pip install -r requirements.txt
   http://127.0.0.1:5000
```

## 🏗 High-Level Architecture (ASCII Diagram)

```
Developer
    |
    v
GitHub Repository (DevOps-Project-Two-Tier-Flask-App)
    |
    v
CI/CD Tool (Jenkins / GitHub Actions)
    |
    v
Build & Push Docker Images
    |
    v
Deployment Environment
    |
    v
---------------------------------------------------------
|                 Web Tier (Flask App)                  |
| ----------------------------------------------------- |
|  - Python Flask Application                           |
|  - Communicates with DB via internal network          |
|    (private subnet / docker bridge)                   |
---------------------------------------------------------
                            |
                            v
---------------------------------------------------------
|             Database Tier (MySQL/Postgres)            |
| ----------------------------------------------------- |
|  - Runs as Container or Managed DB                    |
|  - Stores application data securely                   |
---------------------------------------------------------

```
