#!/bin/bash
/venv/bin/python manage.py makemigrations
/venv/bin/python manage.py migrate
/venv/bin/python manage.py runserver 0.0.0.0:8000