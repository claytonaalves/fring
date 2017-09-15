#coding: utf8
import os

from flask import Flask

from core.database import db

from cidade import cidades_blueprint
from categoria import categorias_blueprint
from anunciante import anunciantes_blueprint
from publicacao import publicacoes_blueprint


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
    app.register_blueprint(cidades_blueprint, url_prefix="/cidades")
    app.register_blueprint(categorias_blueprint, url_prefix="/categorias")
    app.register_blueprint(anunciantes_blueprint, url_prefix="/anunciantes")
    app.register_blueprint(publicacoes_blueprint, url_prefix="/publicacoes")
