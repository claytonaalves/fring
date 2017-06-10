#coding: utf8
import database

from flask import Flask, g

from categoria import categoria
from anunciante import anunciante
from anuncio import anuncio

app = Flask(__name__, static_url_path='')

database.register(app, g)

app.register_blueprint(categoria, url_prefix="/categoria")
app.register_blueprint(anunciante, url_prefix="/anunciante")
app.register_blueprint(anunciante, url_prefix="/anuncio")

@app.route('/')
def index():
    return 'ok!'

