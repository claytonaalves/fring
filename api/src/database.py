#coding: utf8
import sqlite3

from datetime import datetime

DATABASE = 'database/database.db'

context = None

def register(app, g):
    global context
    context = g

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

def get_connection():
    global context
    db = getattr(context, '_database', None)
    if db is None:
        db = context._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def convert_to_dict_list(cursor):
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r

# ====================================================
# ====================================================
# Cidades
# ====================================================
# ====================================================

def todas_cidades():
    db = get_connection()
    cur = db.cursor()
    cur.execute("SELECT id_cidade, nome, uf FROM cidade")
    return convert_to_dict_list(cur)

# ====================================================
# ====================================================
# Categorias
# ====================================================
# ====================================================

def categorias_por_cidade(id_cidade):
    db = get_connection()
    cur = db.cursor()
    cur.execute(
        "SELECT "
        "   id_categoria, descricao, imagem, "
        "   (SELECT COUNT(*) FROM anunciante WHERE id_categoria=a.id_categoria) AS qtde_anunciantes "
        "FROM categoria a "
        "WHERE id_cidade=?", (id_cidade,))
    return convert_to_dict_list(cur)

# ====================================================
# ====================================================
# Anunciantes
# ====================================================
# ====================================================

def salva_anunciante(anunciante):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO anunciante (guid_anunciante, nome_fantasia, logradouro, numero, bairro, telefone, celular, email, id_cidade, id_categoria) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
        (anunciante["guid_anunciante"], anunciante["nome_fantasia"], anunciante["endereco"], 
         anunciante["numero"], anunciante["bairro"], anunciante["telefone"], anunciante["celular"], 
         anunciante["email"], anunciante['id_cidade'], anunciante["id_categoria"]))
    db.commit()

def anunciantes_por_categoria(id_categoria):
    db = get_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM anunciante WHERE id_categoria=?", (id_categoria,))
    return convert_to_dict_list(cur)

def obtem_anunciante(guid_anunciante):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM anunciante WHERE guid_anunciante=?", (guid_anunciante,))
    row = cursor.fetchone()
    return dict(row)

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

