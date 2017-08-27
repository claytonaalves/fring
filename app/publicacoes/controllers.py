from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.publicacoes.models import Publicacao

# Define the blueprint: 'auth', set its url prefix: app.url/auth
blueprint = Blueprint('publicacoes', __name__, url_prefix='/publicacoes')

@blueprint.route('/', methods=['GET'])
def publicacoes_index():
    publicacoes = Publicacao.query.all()
    return render_template("publicacoes/index.html")

