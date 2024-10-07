FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3-mysqldb python3-dev libpython3-dev \
    libjpeg-dev zlib1g-dev \
    ffmpeg \
    apache2 \
    libapache2-mod-wsgi-py3 \
    virtualenv \
    libmysqlclient-dev \
    pkg-config \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt .

RUN cd /opt/ && virtualenv -p /usr/bin/python3 venv && . venv/bin/activate && pip install -r /code/requirements.txt && pip install tzdata && deactivate

COPY . .

RUN echo '<VirtualHost *:80>\n\
    ServerName localhost.oppia\n\
    WSGIDaemonProcess localhost.oppia python-path=/code:/opt/venv/lib/python3.10/site-packages\n\
    WSGIProcessGroup localhost.oppia\n\
    WSGIScriptAlias / /code/oppiamobile/wsgi.py\n\
    WSGIPassAuthorization On\n\
    <Directory /code/oppiamobile/>\n\
        <Files wsgi.py>\n\
            Require all granted\n\
        </Files>\n\
    </Directory>\n\
    Alias /media /media/\n\
    <Directory "/media/">\n\
        Options MultiViews FollowSymLinks\n\
        AllowOverride None\n\
        Require all granted\n\
    </Directory>\n\
    Alias /static /static/\n\
    <Directory "/static/">\n\
        Options MultiViews FollowSymLinks\n\
        AllowOverride None\n\
        Require all granted\n\
    </Directory>\n\
    LogLevel warn\n\
    ErrorLog /var/log/apache2/oppia-error.log\n\
    CustomLog /var/log/apache2/oppia-access.log combined\n\
</VirtualHost>' > /etc/apache2/sites-available/000-default.conf

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
