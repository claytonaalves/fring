import json

import database 

from flask import Blueprint, Response, request, abort, send_from_directory

categorias = Blueprint("categorias", __name__)

@categorias.route('/')
def categorias_index():
    id_cidade = request.args.get("id_cidade", "")
    if not id_cidade:
        abort(412)
    categorias = database.categorias_por_cidade(id_cidade)
    return Response(json.dumps(categorias), mimetype='application/json')

@categorias.route('/images/<path:path>')
def img_route(path):
    return send_from_directory('../images/categorias', path)

