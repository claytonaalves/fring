import json

import database
import firebase

from flask import Blueprint, Response, request

publicacoes = Blueprint("publicacoes", __name__)

@publicacoes.route('/', methods=['POST'])
def salva_publicacao():
    publicacao = request.json
    database.salva_publicacao(publicacao)
    #firebase.publica_anuncio_test(anuncio)
    return Response(json.dumps(publicacao), mimetype='application/json')

# publicacoes?desde=12345678
@publicacoes.route('/', methods=["GET"])
def obtem_publicacoes_desde():
    guid = request.args.get("guid", "") 
    inicio = request.args.get("desde", "")
    categorias = request.args.get("categorias", "").split(",")
    guid_anunciante = request.args.get("guid_anunciante", "")
    if guid:
        publicacoes = database.obtem_publicacao(guid)
    elif inicio:
        publicacoes = database.obtem_publicacoes_desde(inicio, categorias)
    elif guid_anunciante:
        publicacoes = database.obtem_publicacoes_por_anunciante(guid_anunciante)
    return Response(json.dumps(publicacoes), mimetype="application/json")

@publicacoes.route('/<guid_publicacao>')
def obtem_publicacao(guid_publicacao):
    publicacao = database.obtem_publicacao(guid_publicacao)
    return Response(json.dumps(publicacao), mimetype='application/json')

