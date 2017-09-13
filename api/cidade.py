import json

import database 

from flask import Blueprint, Response

cidades = Blueprint("cidades", __name__)

@cidades.route('/')
def cidades_index():
    cidades = database.todas_cidades()
    return Response(json.dumps(cidades), mimetype='application/json')

