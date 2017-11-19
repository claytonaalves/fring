#!/bin/bash

function wait_mysql_startup {
    echo "Waiting for mysql"
    until mysql -h $DATABASE_HOST -u $DATABASE_USER -p$DATABASE_PASS &> /dev/null
    do
      printf "."
      sleep 1
    done
}

if [ ! -f /tmp/system_installed ]; then
    make decrypt_conf
    chmod 644 /var/www/fring/core/settings.py

    mkdir -p /srv/images/anunciantes 
    mkdir -p /srv/images/publicacoes
    chown -R apache:apache /srv/images

    npm install
    npm run postinstall

    wait_mysql_startup

    python fixtures.py

    touch /tmp/system_installed
fi

exec "$@"
