# Book Review API

A simple Book Review service built using **Flask**, **SQLite**, **SQLAlchemy**, and **Redis (mocked)**.  
It provides endpoints to manage books and their reviews, demonstrates caching, error handling, migrations, and testing.

## 🚀 Features

- **RESTful API** with Flask-RESTful
- **SQLite** with SQLAlchemy ORM
- **API documentation** using Swagger (via Flasgger)
- **Caching** using Redis (mocked in tests with `fakeredis`)
- **Proper error handling**
- **Unit & Integration tests** using `pytest`
- **Database migrations** via SQLAlchemy (manual)
- **Indexing** on `book_id` in reviews for optimized queries


## 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Anurag1111111/book_review_service.git
cd book-review-service

python -m venv venv
source venv/bin/activate   

pip install -r requirements.txt


# Run app

python run.py

The app will be available at: http://localhost:5000
Swagger docs: http://localhost:5000/apidocs


# Migrations commands

flask db init
flask db migrate -m "Initial migration"
flask db upgrade


# Run all tests:

pytest
