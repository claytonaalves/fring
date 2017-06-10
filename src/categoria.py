import json

import database 

from flask import Blueprint, Response

categoria = Blueprint("categoria", __name__)

@categoria.route('/')
def categoria_index():
    categorias = database.todas_categorias()
    return Response(json.dumps(categorias), mimetype='application/json')

@categoria.route('/<int:id_categoria>')
def categoria_por_id(id_categoria):
    anunciantes = database.anunciantes_por_categoria(id_categoria)
    return Response(json.dumps(anunciantes), mimetype='application/json')


