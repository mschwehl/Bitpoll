#!/bin/sh
export USER=www-data HOME=/app

python3 manage.py compilemessages
python3 manage.py migrate
python3 manage.py collectstatic --noinput

chmod a+w _static/scss/*.css

uwsgi docker/uwsgi.ini
