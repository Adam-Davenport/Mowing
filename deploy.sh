#!/bin/bash
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
gunicorn mowing.wsgi