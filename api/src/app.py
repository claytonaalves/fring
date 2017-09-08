#coding: utf8
import database

from flask import Flask, g

from cidade import cidades
from categoria import categorias
from anunciante import anunciantes
from publicacao import publicacoes

app = Flask(__name__, static_url_path='')

database.register(app, g)

app.register_blueprint(cidades, url_prefix="/cidades")
app.register_blueprint(categorias, url_prefix="/categorias")
app.register_blueprint(anunciantes, url_prefix="/anunciantes")
app.register_blueprint(publicacoes, url_prefix="/publicacoes")

@app.route('/')
def index():
    return 'ok!'

