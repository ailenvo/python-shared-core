# python-shared-core

Shared core library for Python microservices.

This repository provides **reusable, framework-agnostic core components** that can be shared across multiple services, such as:

- Authentication & JWT utilities
- Database contexts (Postgres, MongoDB)
- Common models, exceptions, and utilities

> ⚠️ This package intentionally **does NOT depend on FastAPI or any web framework**.

---

## 📦 Installation

### Using HTTPS (recommended for simplicity)

```bash
pip install git+https://github.com/ailenvo/python-shared-core.git

## dependencies database

mongo = [
  "motor>=3.6.0",
  "pymongo>=4.9.2",
]

postgres = [
  "SQLAlchemy>=2.0.44",
  "asyncpg>=0.29.0",
]
