#!/bin/sh
python3 manage.py makemigrations playlist
python3 manage.py migrate
python3 manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL
#pyhton3 manage.py shell << playlist/fixture.py
python3 manage.py runserver 0.0.0.0:80
