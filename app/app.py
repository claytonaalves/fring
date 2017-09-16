# encoding: utf8

from flask import Flask
from flask_simplelogin import SimpleLogin

from .auth import login_checker
from .base.controllers import base_blueprint
from .auth.controllers import auth_blueprint
from .publicacoes.controllers import publicacoes_blueprint

from core.database import db


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    login_manager = SimpleLogin(app, login_checker=login_checker)
    login_manager.config['home_url'] = '/login/'
    login_manager.messages['login_failure'] = u'Credenciais inválidas!'
    login_manager.messages['logout'] = u''


def register_blueprints(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(base_blueprint)
    app.register_blueprint(publicacoes_blueprint)
