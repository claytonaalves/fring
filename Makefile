.PHONY: install
 
install:
	npm install
	cp node_modules/jquery/dist/* app/static/js
	cp node_modules/bootstrap/dist/css/* app/static/css
	cp node_modules/bootstrap/dist/js/* app/static/js
	cp node_modules/jquery-ui-dist/*.js app/static/js
	cp node_modules/jquery-ui-dist/*.css app/static/css
 
