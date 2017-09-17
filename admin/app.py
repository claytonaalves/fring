# encoding: utf8
import os

from flask import Flask, Blueprint, redirect
from flask_admin import Admin
from flask_babelex import Babel

from core.database import db
from .views import register_admin_views


root_blueprint = Blueprint('root', __name__)


@root_blueprint.route('/')
def index():
    return redirect('/admin/admin')


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    app.register_blueprint(root_blueprint)
    return app


def register_extensions(app):
    db.init_app(app)
    babel = Babel(app)
    admin = Admin(app, name=u"Manutenção")
    register_admin_views(admin)
