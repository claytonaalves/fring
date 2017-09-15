from flask import Blueprint, jsonify

from core.cidades.models import Cidade, serializa

cidades_blueprint = Blueprint("cidades", __name__)


@cidades_blueprint.route('/')
def cidades_index():
    cidades = Cidade.query.all()
    return jsonify(serializa(cidades))


@cidades_blueprint.route('/<int:id_cidade>')
def cidade_por_id(id_cidade):
    cidade = Cidade.query.filter_by(id_cidade=id_cidade).first()
    return jsonify(cidade.serialize)
