# DjangoCRM

## Introduction
This Django project is designed to demonstrate a robust web application framework setup. It's ideal for rapid development and clean, pragmatic design.

## Features
- User authentication (login, logout, signup)
- Profile management
- CRUD operations on one model
- Responsive admin interface

## Technology Stack
- **Framework**: Django 5.0.6
- **Programming Language**: Python 3.12
- **Database**: sqlite3
- **Frontend**: Bootstrap, HTML5, CSS3

### Prerequisites
- Python 3.9+
- pip
- Virtualenv (recommended)

### Installation
```bash
git clone https://github.com/marc-rifat/DjangoCRM.git

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # default[sqlite3] username: admin password: admin

python manage.py runserver 
```


