#!/bin/sh
export USER=www-data HOME=/app

python3 manage.py compilemessages
python3 manage.py migrate
python3 manage.py collectstatic --noinput

chown 2008 -R _static
chown 2008 data/db.sqlite3
chown 2008 data

uwsgi docker/uwsgi.ini
