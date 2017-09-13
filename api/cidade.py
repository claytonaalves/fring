from flask import Blueprint, Response, jsonify

from core.cidades.models import Cidade, serializa

blueprint_cidades = Blueprint("cidades", __name__)

@blueprint_cidades.route('/')
def cidades_index():
    cidades = Cidade.query.all()
    return jsonify(serializa(cidades))

