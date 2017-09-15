from flask import Blueprint, request, jsonify

from core.database import db
from core.anunciantes.models import Anunciante

anunciantes_blueprint = Blueprint("anunciantes", __name__)


@anunciantes_blueprint.route('/', methods=['GET', 'POST'])
def index_anunciantes():
    if request.method == 'POST':
        salva_anunciante(request.json)
        return jsonify('')
    id_categoria = int(request.args.get('id_categoria', '0'))
    if id_categoria == 0:
        anunciantes = Anunciante.query.all()
    else:
        anunciantes = Anunciante.query.filter_by(id_categoria=id_categoria)
    return jsonify([anunciante.serialize for anunciante in anunciantes])


def salva_anunciante(json):
    anunciante = Anunciante()
    anunciante.guid_anunciante = json["guid_anunciante"]
    anunciante.nome_fantasia = json["nome_fantasia"]
    anunciante.endereco = json["endereco"]
    anunciante.numero = json["numero"]
    anunciante.bairro = json["bairro"]
    anunciante.telefone = json["telefone"]
    anunciante.celular = json["celular"]
    anunciante.email = json["email"]
    anunciante.id_cidade = json['id_cidade']
    anunciante.id_categoria = json["id_categoria"]
    db.session.add(anunciante)
    db.session.commit()
