# API Testing & Database Data Reconciliation Engine

[![API Integration CI](https://github.com/aishwaryyaa12/api-testing-postman-python-sql/actions/workflows/api-ci.yml/badge.svg)](https://github.com/aishwaryyaa12/api-testing-postman-python-sql/actions)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Postman/Newman](https://img.shields.io/badge/Postman-Newman-FF6C37?logo=postman&logoColor=white)](https://www.postman.com/)
[![SQLite/SQL](https://img.shields.io/badge/SQL-PostgreSQL%20%7C%20SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)

A backend testing and financial data reconciliation suite combining **Postman / Newman CLI**, **Python (requests)**, and **SQL transactional verification**. Designed to catch data drift, float rounding issues, and contract mismatches across distributed microservices.

**Author:** [Aishwarya Shanmugam](https://linkedin.com/in/aishwaryyaa12) (QA Automation Engineer)

---

## Why I Built This & The Engineering Problem

In distributed architectures (such as order management, payment gateways, and billing platforms), verifying HTTP `200 OK` status codes is insufficient. A common critical failure mode is **silent data drift**:

1. **Floating-Point Rounding Discrepancies:**  
   In financial systems, calculating order totals using floating-point types (`0.1 + 0.2 = 0.30000000000000004`) causes subtotal mismatches between the API presentation layer and the database ledger. This project demonstrates strict reconciliation using integer cent math / exact decimal precision (`abs(calculated - reported) < 0.01`).

2. **Database vs. API Discrepancies:**  
   When caching layers (e.g., Redis) or message queues sit between backend databases and customer-facing APIs, cache invalidation delays can cause users to see stale pricing or outdated inventory. The Python reconciliation script queries the transactional database mirror, re-aggregates line items, and asserts strict equality with the live API payload.

3. **CI/CD Regression Automation via Newman:**  
   Rather than keeping Postman collections isolated in a desktop GUI, this framework exports them into version control and executes them headlessly in GitHub Actions using the Newman CLI and HTML reporter.

---

## Repository Structure

```text
├── .github/workflows/
│   └── api-ci.yml                           # GitHub Actions CI running Newman and Python scripts
├── postman/
│   ├── ecommerce_api_collection.json        # Postman Collection v2.1 with schema & subtotal assertions
│   └── env_staging.json                     # Environment configuration (base URLs, auth tokens)
├── scripts/
│   └── verify_db_api.py                     # Python engine reconciling database ledger with API payloads
├── requirements.txt                         # Python dependencies (requests, pydantic)
└── README.md
```

---

## What the Tests Validate

### 1. Postman / Newman Suite (`postman/ecommerce_api_collection.json`)
* **Status & Response Time:** Asserts HTTP `200 OK` and response latency under 1500ms.
* **Schema Adherence:** Asserts required keys (`id`, `title`, `price`, `quantity`) and data types for each catalog item.
* **Negative Paths:** Verifies that requesting non-existent records (`GET /products/999999`) returns a clean `404 Not Found` rather than an unhandled `500 Server Error`.
* **Subtotal Mathematical Integrity:** Ingests dynamic cart items and iterates over line items (`price * quantity`), asserting that the summed subtotal equals the API's reported total.

### 2. Python & SQL Reconciliation Script (`scripts/verify_db_api.py`)
* Seeds an in-memory transactional database simulating line-item orders.
* Computes database gross totals via `SUM(unit_price * quantity)`.
* Calls the live REST API endpoint (`https://dummyjson.com/carts/1`).
* Reconciles the database aggregation against the live API response and asserts zero data drift (`delta < 0.01`).

---

## Setup & Local Execution

### 1. Run Python Reconciliation Engine
```bash
# Clone the repository
git clone https://github.com/aishwaryyaa12/api-testing-postman-python-sql.git
cd api-testing-postman-python-sql

# Set up virtual environment
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# Install dependencies and execute reconciliation
pip install -r requirements.txt
python scripts/verify_db_api.py
```

### 2. Run Postman Collection via Newman CLI
```bash
# Install Newman and HTML reporter
npm install -g newman newman-reporter-htmlextra

# Run test collection against staging environment
newman run postman/ecommerce_api_collection.json -e postman/env_staging.json -r cli,htmlextra --reporter-htmlextra-export report.html
```

---

## Continuous Integration (GitHub Actions)

On every `push` to `main`, `.github/workflows/api-ci.yml`:
1. Executes `scripts/verify_db_api.py` to ensure zero database-to-API discrepancy.
2. Runs the Newman CLI test suite against the collection.
3. Generates and uploads the comprehensive HTML test execution report.
