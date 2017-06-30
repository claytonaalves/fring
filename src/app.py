#coding: utf8
import database

from flask import Flask, g

#from cidade import cidade
#from categoria import categoria
#from anunciante import anunciante
from publicacao import publicacoes

app = Flask(__name__, static_url_path='')

database.register(app, g)

#app.register_blueprint(cidade, url_prefix="/cidade")
#app.register_blueprint(categoria, url_prefix="/categoria")
#app.register_blueprint(anunciante, url_prefix="/anunciante")
app.register_blueprint(publicacoes, url_prefix="/publicacoes")

@app.route('/')
def index():
    return 'ok!'

