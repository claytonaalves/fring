# encoding: utf8
import os

from flask import Flask
from flask_admin import Admin
from flask_babelex import Babel

from core.database import db
from .views import register_admin_views


def create_app(config):
    images_base_path = os.path.join(os.getcwd(), 'images')
    app = Flask(__name__, static_folder=images_base_path)
    app.config.from_object(config)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    babel = Babel(app)
    admin = Admin(app, name=u"Manutenção")
    register_admin_views(admin)
