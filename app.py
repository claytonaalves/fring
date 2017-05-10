#coding: utf8
import json
from flask import Flask, Response, send_from_directory, request, g

import database

app = Flask(__name__, static_url_path='')
app.debug=True

database.register(app, g)

@app.route('/')
def index():
    return 'AnunciosApp'

@app.route('/images/<path:path>')
def img_route(path):
    return send_from_directory('images', path)

@app.route('/categoria')
def categoria_index():
    categorias = database.todas_categorias()
    return Response(json.dumps(categorias), mimetype='application/json')

@app.route('/categoria/<int:id_categoria>')
def categoria_por_id(id_categoria):
    anunciantes = database.anunciantes_por_categoria(id_categoria)
    return Response(json.dumps(anunciantes), mimetype='application/json')

@app.route('/anunciante/<int:id_anunciante>')
def get_anunciante(id_anunciante):
    anunciante = database.anunciante_por_id(id_anunciante)
    if anunciante:
        return Response(json.dumps(anunciante), mimetype='application/json')
    else:
        return 'Anunciante não encontrado'

@app.route('/anuncio', methods=['POST'])
def save_anuncio():
    anuncio = request.json
    print(anuncio)
    database.salva_anuncio(anuncio)
    return Response(json.dumps(anuncio), mimetype='application/json')

app.run(host='0.0.0.0')

