#!/bin/bash
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py createstatic
gunicorn mowing.wsgi