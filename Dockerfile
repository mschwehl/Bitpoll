FROM python:3-buster

RUN apt update \
    && apt install -y --no-install-recommends uwsgi g++ make python3-psycopg2 python3-ldap3 gettext gcc python3-dev libldap2-dev libsasl2-dev  \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
#ENV UID=2008
#RUN usermod -u $UID -g nogroup -d /app www-data

COPY . .

RUN pip install -r requirements-production.txt

# for postgres
# RUN pip install psycopg2

RUN mkdir _static && ln -s . _static/static
RUN ln -s /data data
RUN ln -s /config/settings_local.py bitpoll/settings_local.py
RUN chmod o+r -R .

EXPOSE 3008
VOLUME /data
VOLUME /config

CMD docker/entrypoint.sh
