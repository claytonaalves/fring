FROM centos:6.9

# Packages installation
RUN yum install -y gcc httpd mod_wsgi python-devel mysql-devel xz \
    && yum clean all

# pip and python packages installation
RUN (curl "https://bootstrap.pypa.io/get-pip.py" | python) \
    && pip install MySQL-python==1.2.5 \
    && pip install SQLAlchemy==1.1.13 \
    && pip install Flask==0.12.2 \
    && pip install Flask-SQLAlchemy==2.2 \
    && pip install Flask-WTF==0.14.2 \
    && pip install flask-simplelogin==0.0.6 \
    && pip install Flask-Admin==1.5.0 \
    && pip install Flask-BabelEx==0.9.3 \
    && pip install requests==2.18.4 \
    && pip install Pillow==2.7.0

# Node.js installation
WORKDIR /tmp
RUN curl -O https://nodejs.org/dist/v8.9.0/node-v8.9.0-linux-x64.tar.xz \
    && tar -xvf node-v8.9.0-linux-x64.tar.xz \
    && ln -s /tmp/node-v8.9.0-linux-x64/bin/node /usr/bin/node \
    && ln -s /tmp/node-v8.9.0-linux-x64/bin/npm /usr/bin/npm \
    && rm -f node-v8.9.0-linux-x64.tar.xz

# Application install
COPY httpd/wsgi.conf /etc/httpd/conf.d/
COPY . /var/www/fring

VOLUME /srv/images

WORKDIR /var/www/fring
RUN chmod 777 /var/www/fring/docker-entrypoint.sh \
    && npm install

ENV DATABASE_HOST=mysql \
    DATABASE_NAME=fring \
    DATABASE_USER=fring \
    DATABASE_PASS=fring \
    TZ=America/Cuiaba

EXPOSE 8080

ENTRYPOINT ["/var/www/fring/docker-entrypoint.sh"]
CMD ["apachectl", "-D", "FOREGROUND"]

