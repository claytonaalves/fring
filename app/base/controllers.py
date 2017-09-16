from flask import Blueprint, render_template, redirect, url_for
from jinja2 import TemplateNotFound

base_blueprint = Blueprint('base', __name__)


@base_blueprint.app_errorhandler(404)
def not_found(error):
    try:
        return render_template('404.html'), 404
    except TemplateNotFound:
        print("nao achou template")
        abort(404)


@base_blueprint.route('/', methods=['GET'])
def index():
    return redirect(url_for('publicacoes.index_publicacoes'))
