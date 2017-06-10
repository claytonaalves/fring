import json

import database
import firebase

from flask import Blueprint, Response, request

anuncio = Blueprint("anuncio", __name__)

@anuncio.route('/', methods=['POST'])
def save_anuncio():
    anuncio = request.json
    database.salva_anuncio(anuncio)
    firebase.publica_anuncio_test(anuncio)
    return Response(json.dumps(anuncio), mimetype='application/json')

@anuncio.route('/<guid_anuncio>')
def obtem_anuncio(guid_anuncio):
    anuncio = database.obtem_anuncio(guid_anuncio)
    return Response(json.dumps(anuncio), mimetype='application/json')

