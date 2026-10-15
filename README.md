# Enterprise API & Database Quality Assurance Suite

[![API Integration Tests](https://github.com/aishwaryyaa12/api-testing-postman-python-sql/actions/workflows/api-ci.yml/badge.svg)](https://github.com/aishwaryyaa12/api-testing-postman-python-sql/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Postman/Newman](https://img.shields.io/badge/Postman-Newman-orange.svg)](https://www.postman.com/)

A comprehensive backend testing and data validation suite combining **Postman / Newman CLI**, **Python (requests)**, and **SQL / PostgreSQL data verification**.

Developed by **[Aishwarya Shanmugam](https://linkedin.com/in/aishwaryyaa12)** (QA Engineer).

---

## 🌟 Key Features

- **Postman REST API Collection**: Pre-request scripts, dynamic environment variables, JSON schema validation, and status code assertions.
- **Newman CLI Automated Execution**: Command-line execution integrated into GitHub Actions CI/CD workflows.
- **Python & SQL Database Validation**: Automated Python scripts verifying database record integrity, foreign key constraints, and query performance.
- **CI/CD Pipeline**: Continuous test execution on every commit with HTML test run summaries.

---

## 🚀 Getting Started

### 1. Run Postman Tests via Newman
```bash
npm install -g newman newman-reporter-htmlextra
newman run postman/ecommerce_api_collection.json -e postman/env_staging.json -r htmlextra
```

### 2. Run Python & SQL Data Verification
```bash
pip install -r requirements.txt
python scripts/verify_db_api.py
```

---

## 👩‍💻 Author
**Aishwarya Shanmugam** — QA Engineer | Test Automation Specialist  
📍 Steinenbronn (Stuttgart Region), Germany  
🔗 [LinkedIn Profile](https://linkedin.com/in/aishwaryyaa12)
