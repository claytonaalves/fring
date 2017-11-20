from flask import Blueprint, request, jsonify, current_app, send_from_directory

from core.database import db
from core.anunciantes.models import Anunciante
from core.image_upload import handle_image_upload

anunciantes_blueprint = Blueprint("anunciantes", __name__)


@anunciantes_blueprint.route('/', methods=['GET', 'POST'])
def index_anunciantes():
    if request.method == 'POST':
        anunciante = save_advertiser_profile(request.json)
        return jsonify(anunciante.serialize)
    id_categoria = int(request.args.get('id_categoria', '0'))
    if id_categoria == 0:
        anunciantes = Anunciante.query.all()
    else:
        anunciantes = Anunciante.query.filter_by(id_categoria=id_categoria)
    return jsonify([anunciante.serialize for anunciante in anunciantes])


@anunciantes_blueprint.route('/fotos', methods=["GET", "POST"])
def image_upload():
    return handle_image_upload(request, 
                               save_path=current_app.config['ADVERTISER_MEDIA_PATH'],
                               success_path='.get_advertiser_image')


@anunciantes_blueprint.route('/foto/<filename>')
def get_advertiser_image(filename):
    return send_from_directory(current_app.config['ADVERTISER_MEDIA_PATH'], filename)


def save_advertiser_profile(json):
    new_advertiser = False
    advertiser = Anunciante.query.filter_by(guid_anunciante=json["guid_anunciante"]).first()
    if not advertiser:
        advertiser = Anunciante()
        new_advertiser = True
    advertiser.guid_anunciante = json["guid_anunciante"]
    advertiser.nome_fantasia = json["nome_fantasia"]
    advertiser.logradouro = json["logradouro"]
    advertiser.numero = json["numero"]
    advertiser.bairro = json["bairro"]
    advertiser.telefone = json["telefone"]
    advertiser.celular = json["celular"]
    advertiser.email = json["email"]
    advertiser.id_cidade = json['id_cidade']
    advertiser.id_categoria = json["id_categoria"]
    advertiser.picture_file = json.get("picture_file", None)
    if new_advertiser:
        db.session.add(advertiser)
    db.session.commit()
    return advertiser
