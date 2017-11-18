#!/bin/bash

if [ ! -f /tmp/system_installed ]; then
    make decrypt_conf
    chmod 644 /var/www/fring/core/settings.py

    mkdir -p /srv/images/anunciantes 
    mkdir -p /srv/images/publicacoes
    chown -R apache:apache /srv/images

    npm install
    npm run postinstall

    python fixtures.py

    touch /tmp/system_installed
fi

exec "$@"
