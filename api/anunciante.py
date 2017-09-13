import json

import database

from flask import Blueprint, Response, request

anunciantes = Blueprint("anunciantes", __name__)

@anunciantes.route('/', methods=['GET', 'POST'])
def salva_perfil_anunciante():
    anunciante = request.json
    database.salva_anunciante(anunciante)
    return Response(json.dumps(anunciante), mimetype='application/json')

#@anunciantes.route('/', methods=["GET"])
#def obtem_publicacoes_desde():
#    guid = request.args.get("guid", "") 
#    inicio = request.args.get("desde", "")
#    categorias = request.args.get("categorias", "").split(",")
#    guid_anunciante = request.args.get("guid_anunciante", "")
#    if guid:
#        anunciantes = database.obtem_publicacao(guid)
#    elif inicio:
#        anunciantes = database.obtem_publicacoes_desde(inicio, categorias)
#    elif guid_anunciante:
#        anunciantes = database.obtem_publicacoes_por_anunciante(guid_anunciante)
#    return Response(json.dumps(anunciantes), mimetype="application/json")
#
#@anunciantes.route('/<guid_publicacao>')
#def obtem_publicacao(guid_publicacao):
#    publicacao = database.obtem_publicacao(guid_publicacao)
#    return Response(json.dumps(publicacao), mimetype='application/json')

