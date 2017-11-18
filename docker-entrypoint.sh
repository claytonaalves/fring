#!/bin/bash

if [ ! -f /var/www/fring/core/settints.py ]; then
    make decrypt_conf
fi

if [ ! -d /srv/images/anunciantes ]; then
    mkdir -p /srv/images/anunciantes 
    mkdir -p /srv/images/publicacoes
    chown -R apache:apache /srv/images
fi

exec "$@"
