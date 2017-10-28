# encoding: utf8
import os
import time
from datetime import datetime

from flask import Blueprint, request, send_from_directory, redirect, url_for, jsonify, flash
from werkzeug.utils import secure_filename
from sqlalchemy import and_

from core.firebase import publica_anuncio_firebase
from core.database import db
from core.publicacoes.models import Publicacao
from core.device.models import Device

PASTA_FOTOS_PUBLICACOES = "/var/www/fring-webapp/images/publicacoes"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

publicacoes_blueprint = Blueprint("publicacoes", __name__)


@publicacoes_blueprint.route('/<guid_publicacao>')
def obtem_publicacao(guid_publicacao):
    publicacao = Publicacao.query.filter_by(guid_publicacao=guid_publicacao).first()
    return jsonify(publicacao.serialize)


@publicacoes_blueprint.route('/', methods=['GET', 'POST'])
def index_publicacoes():
    if request.method == 'GET':
        return get_publications_list(request)
    else:
        publicacao = salva_publicacao(request.json)
        # Talvez ao invés de publicar diretamente no firebase fosse interessante iniciar uma task paralela
        #publica_anuncio_firebase(publicacao)
        return publicacao


@publicacoes_blueprint.route('/fotos', methods=["GET", "POST"])
def foto_upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(PASTA_FOTOS_PUBLICACOES, filename))
            return redirect(url_for('.foto_publicacao', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
    <p><input type=file name=file>
     <input type=submit value=Upload>
    </form>
    '''


@publicacoes_blueprint.route('/foto/<filename>')
def foto_publicacao(filename):
    return send_from_directory(PASTA_FOTOS_PUBLICACOES, filename)


def get_publications_list(request):
    """ Returns a list of publications based on request params
    """
    device_id = request.args.get("device_id", "")
    categories = request.args.get("categorias", "").split(",")

    device = Device.query.filter_by(device_id=device_id).first()
    if not device:
        device = Device(device_id)

    publications = get_publications_since(device.last_query, categories)

    device.last_query = datetime.now()
    db.session.add(device)
    db.session.commit()

    return publications


def get_publications_since(last_query, categories):
    """ Returns a list of publications since last_query
        filtering by categories
    """
    from_date = last_query.strftime('%Y-%m-%d %H:%M:%S')
    publications = Publicacao.query.filter(
        and_(
            Publicacao.data_publicacao >= from_date,
            Publicacao.id_categoria.in_(categories)
        )
    ).order_by(Publicacao.data_publicacao.desc())
    return jsonify([publication.serialize for publication in publications])


def obtem_publicacoes_por_anunciante(guid_anunciante):
    publicacoes = Publicacao.query.filter_by(guid_anunciante=guid_anunciante)
    return jsonify([publicacao.serialize for publicacao in publicacoes])


def obtem_publicacoes_por_categorias(categorias):
    publicacoes = Publicacao.query.filter(Publicacao.id_categoria.in_(categorias))
    return jsonify([publicacao.serialize for publicacao in publicacoes])


def salva_publicacao(json):
    publicacao = Publicacao()
    publicacao.guid_publicacao = json['guid_publicacao']
    publicacao.guid_anunciante = json['guid_anunciante']
    publicacao.id_categoria = json['id_categoria']
    publicacao.titulo = json['titulo']
    publicacao.descricao = json['descricao']
    publicacao.data_validade = datetime.strptime(json.get('data_validade', '0'), '%Y-%m-%d %H:%M:%S')
    publicacao.imagem = json.get('imagem', None)
    db.session.add(publicacao)
    db.session.commit()
    return jsonify(publicacao.serialize)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
