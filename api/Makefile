.PHONY: decrypt_conf encrypt_conf
 
CONF_FILE=src/settings.py
 
decrypt_conf:
	openssl cast5-cbc -d -base64 -in ${CONF_FILE}.cast5 -out ${CONF_FILE}
	chmod 600 ${CONF_FILE}
 
encrypt_conf:
	openssl cast5-cbc -e -base64 -in ${CONF_FILE} -out ${CONF_FILE}.cast5

