import os
import json
import uuid

import database

from flask import Blueprint, Response, request, send_from_directory

anunciante = Blueprint("anunciante", __name__)

PASTA_FOTOS_ANUNCIANTE = 'images/fotos_anunciante'

@anunciante.route('/', methods=['POST'])
def grava_anunciante():
    anunciante = request.json
    database.salva_anunciante(anunciante)
    return Response(json.dumps(anunciante), mimetype='application/json')

@anunciante.route('/<int:id_anunciante>')
def obtem_anunciante(id_anunciante):
    anunciante = database.anunciante_por_id(id_anunciante)
    if anunciante:
        return Response(json.dumps(anunciante), mimetype='application/json')
    else:
        return 'Anunciante não encontrado'

@anunciante.route('/<guid_anunciante>/anuncios', methods=['GET'])
def anuncios_por_anunciante(guid_anunciante):
    anuncios = database.anuncios_por_anunciante(guid_anunciante)
    return Response(json.dumps(anuncios), mimetype='application/json')

@anunciante.route('/imagem/<path:path>')
def obtem_imagem_perfil_anunciante(path):
    return send_from_directory('../'+PASTA_FOTOS_ANUNCIANTE, path)

@anunciante.route('/imagem_upload', methods=['POST'])
def imagem_perfil_upload():
    arquivo_foto = request.files['foto']
    if arquivo_foto and arquivo_permitido(arquivo_foto.filename):
        extension = arquivo_foto.filename.rsplit('.', 1)[1].lower()
        filename = "{0}.{1}".format(uuid.uuid4(), extension)
        arquivo_foto.save(os.path.join(PASTA_FOTOS_ANUNCIANTE, filename))
        return filename
    else:
        return 'Formato nao permitido'

def arquivo_permitido(nome_arquivo):
    return '.' in nome_arquivo and nome_arquivo.rsplit('.', 1)[1].lower() in ['png', 'jpeg', 'jpg']

