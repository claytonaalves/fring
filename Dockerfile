FROM centos:6.9

RUN yum install -y gcc httpd mod_wsgi python-devel mysql-devel \
    && yum clean all \
    && (curl "https://bootstrap.pypa.io/get-pip.py" | python)

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /var/www/fring

COPY httpd/wsgi.conf /etc/httpd/conf.d/

ENV TZ=America/Cuiaba
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
