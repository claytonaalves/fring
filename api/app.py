#coding: utf8
import os

from flask import Flask

from core.database import db
from core.cidades.models import Cidade
from core.categorias.models import Categoria
from core.anunciantes.models import Anunciante
from core.publicacoes.models import Publicacao

from cidade import blueprint_cidades
from categoria import categorias_blueprint
#from anunciante import anunciantes
#from publicacao import publicacoes

def create_app(config):
    images_base_path = os.path.join(os.getcwd(), 'images')
    app = Flask(__name__, static_folder=images_base_path)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    app.register_blueprint(blueprint_cidades, url_prefix="/cidades")
    app.register_blueprint(categorias_blueprint, url_prefix="/categorias")
    #app.register_blueprint(anunciantes, url_prefix="/anunciantes")
    #app.register_blueprint(publicacoes, url_prefix="/publicacoes")
