#!/bin/bash

if [ ! -f /var/www/fring/core/settings.py ]; then
    make decrypt_conf
    chmod 644 /var/www/fring/core/settings.py
fi

if [ ! -d /srv/images/anunciantes ]; then
    mkdir -p /srv/images/anunciantes 
    mkdir -p /srv/images/publicacoes
    chown -R apache:apache /srv/images
fi

npm install
npm run postinstall

echo "testando 12342"

exec "$@"
