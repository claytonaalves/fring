.PHONY: decrypt_conf encrypt_conf
 
CONF_FILE=settings.py
 
encrypt_conf:
	openssl cast5-cbc -e -base64 -in ${CONF_FILE} -out ${CONF_FILE}.cast5 -md md5

decrypt_conf:
	openssl cast5-cbc -d -base64 -in ${CONF_FILE}.cast5 -out ${CONF_FILE} -md md5
	chmod 600 ${CONF_FILE}
