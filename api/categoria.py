from flask import Blueprint, request, jsonify, abort
from core.categorias.models import Categoria, serializa

categorias_blueprint = Blueprint("categorias", __name__)


@categorias_blueprint.route('/')
def categorias_index():
    id_cidade = request.args.get("id_cidade", "")
    if not id_cidade:
        abort(412)
    categorias = Categoria.query.filter_by(id_cidade=id_cidade)
    return jsonify(serializa(categorias))
