# encoding: utf8
import os
import time

from flask import Blueprint, request, send_from_directory, redirect, url_for, jsonify, flash
from werkzeug.utils import secure_filename
from sqlalchemy import and_

from core.firebase import publica_anuncio_firebase
from core.database import db
from core.publicacoes.models import Publicacao

PASTA_FOTOS_PUBLICACOES = "/home/clayton/working/fring-backend/fotos"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

publicacoes_blueprint = Blueprint("publicacoes", __name__)


@publicacoes_blueprint.route('/<guid_publicacao>')
def obtem_publicacao(guid_publicacao):
    publicacao = Publicacao.query.filter_by(guid_publicacao=guid_publicacao).first()
    return jsonify(publicacao.serialize)


# /publicacoes?desde=12345678
# /publicacoes?desde=12345678&categorias=1,2,3
@publicacoes_blueprint.route('/', methods=['GET', 'POST'])
def index_publicacoes():
    if request.method == 'GET':
        inicio = request.args.get("desde", "")
        categorias = request.args.get("categorias", "").split(",")
        guid_anunciante = request.args.get("guid_anunciante", "")
        if inicio:
            return obtem_publicacoes_desde(float(inicio), categorias)
        elif guid_anunciante:
            return obtem_publicacoes_por_anunciante(guid_anunciante)
        elif categorias:
            return obtem_publicacoes_por_categorias(categorias)
    else:
        return salva_publicacao()


def obtem_publicacoes_desde(inicio_epoch, categorias):
    """ Retorna a lista de publicações das categorias solicitadas
        desde a última requisição.
    """
    inicio = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(inicio_epoch))
    publicacoes = Publicacao.query.filter(
        and_(
            Publicacao.data_publicacao >= inicio,
            Publicacao.id_categoria.in_(categorias)
        )
    ).order_by(Publicacao.data_publicacao.desc())
    return jsonify([publicacao.serialize for publicacao in publicacoes])


def obtem_publicacoes_por_anunciante(guid_anunciante):
    publicacoes = Publicacao.query.filter_by(guid_anunciante=guid_anunciante)
    return jsonify([publicacao.serialize for publicacao in publicacoes])


def obtem_publicacoes_por_categorias(categorias):
    publicacoes = Publicacao.query.filter(Publicacao.id_categoria.in_(categorias))
    return jsonify([publicacao.serialize for publicacao in publicacoes])


def salva_publicacao():
    json = request.json
    publicacao = Publicacao()
    publicacao.guid_publicacao = json['guid_publicacao']
    publicacao.guid_anunciante = json['guid_anunciante']
    publicacao.id_categoria = json['id_categoria']
    publicacao.titulo = json['titulo']
    publicacao.descricao = json['descricao']
    publicacao.data_validade = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(json.get('data_validade', '0'))))
    publicacao.imagem = json.get('imagem', '')
    db.session.add(publicacao)
    db.session.commit()
    # Talvez ao invés de publicar diretamente no firebase fosse interessante iniciar uma task paralela
    publica_anuncio_firebase(publicacao)
    return jsonify(publicacao.serialize)


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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
