# coding: utf8
from datetime import datetime

from core.cidades.models import Cidade
from core.categorias.models import Categoria
from core.anunciantes.models import Anunciante
from core.publicacoes.models import Publicacao

def convert_to_dict_list(cursor):
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r

# ====================================================
# ====================================================
# Publicações
# ====================================================
# ====================================================

QUERY_PUBLICACOES = (
    "SELECT guid_publicacao, guid_anunciante, id_categoria, titulo, descricao, data_publicacao, data_validade, imagem "
    "FROM publicacao "
)

def salva_publicacao(publicacao):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO publicacao (guid_publicacao, guid_anunciante, id_categoria, titulo, descricao, data_publicacao, data_validade) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)", 
        (publicacao["guid_publicacao"], 
         publicacao["guid_anunciante"], 
         publicacao["id_categoria"], 
         publicacao["titulo"], 
         publicacao["descricao"], 
         publicacao["data_publicacao"],
         publicacao["data_validade"])
    )
    db.commit()

def obtem_publicacoes():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(QUERY_PUBLICACOES + " ORDER BY data_publicacao DESC")
    return convert_to_dict_list(cursor)

def obtem_publicacoes_desde(data_inicio, ids_categorias):
    params = [data_inicio]
    params.extend(ids_categorias)
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(
        QUERY_PUBLICACOES + 
        "WHERE data_publicacao>=? "
        "AND id_categoria IN ({0})"
        "ORDER BY data_publicacao DESC".format(','.join('?'*len(ids_categorias))), params)
    return convert_to_dict_list(cursor)

def obtem_publicacoes_por_anunciante(guid_anunciante):
    db = get_connection()
    cur = db.cursor()
    cur.execute(QUERY_PUBLICACOES + "WHERE guid_anunciante=?", (guid_anunciante,))
    return convert_to_dict_list(cur)

def obtem_publicacao(guid):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(QUERY_PUBLICACOES + "WHERE guid_publicacao=?", (guid,))
    publicacao = dict(cursor.fetchone())
    anunciante = obtem_anunciante(publicacao["guid_anunciante"])
    publicacao["anunciante"] = anunciante
    return publicacao

