import json

import database

from flask import Blueprint, Response, request

anunciante = Blueprint("anunciante", __name__)

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

