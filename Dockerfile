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

WORKDIR /home/oppia/django-oppia

COPY requirements.txt .

RUN cd /home/oppia/ && virtualenv -p /usr/bin/python3 env && . env/bin/activate && pip install -r django-oppia/requirements.txt && pip install tzdata && deactivate

COPY . .

RUN echo '<VirtualHost *:80>\n\
    ServerName localhost.oppia\n\
    WSGIDaemonProcess localhost.oppia python-path=/home/oppia/django-oppia:/home/oppia/env/lib/python3.10/site-packages\n\
    WSGIProcessGroup localhost.oppia\n\
    WSGIScriptAlias / /home/oppia/django-oppia/oppiamobile/wsgi.py\n\
    WSGIPassAuthorization On\n\
    <Directory /home/oppia/django-oppia/oppiamobile/>\n\
        <Files wsgi.py>\n\
            Require all granted\n\
        </Files>\n\
    </Directory>\n\
    Alias /media /home/oppia/media/\n\
    <Directory "/home/oppia/media/">\n\
        Options MultiViews FollowSymLinks\n\
        AllowOverride None\n\
        Require all granted\n\
    </Directory>\n\
    Alias /static /home/oppia/static/\n\
    <Directory "/home/oppia/static/">\n\
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
