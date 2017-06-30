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
# Categorias
# ====================================================
# ====================================================

def todas_categorias():
    db = get_connection()
    cur = db.cursor()
    cur.execute("SELECT _id, descricao, imagem, (SELECT COUNT(*) FROM anunciante WHERE id_categoria=a._id) AS qtde_anunciantes FROM categoria a")
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
        "INSERT INTO anunciante (nome_fantasia, logradouro, numero, bairro, cidade, uf, telefone, celular, email, id_categoria, guid) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
        (anunciante["nome"], anunciante["endereco"], anunciante["numero"], anunciante["bairro"], 
         anunciante["cidade"], anunciante["estado"], anunciante["telefone"], anunciante["celular"], 
         anunciante["email"], anunciante["id_categoria"], anunciante["guid"]))
    db.commit()

def anunciantes_por_categoria(id_categoria):
    db = get_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM anunciante WHERE id_categoria=?", (id_categoria,))
    return convert_to_dict_list(cur)

def anunciante_por_id(idanunciante):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM anunciante WHERE _id=?", (idanunciante,))
    row = cursor.fetchone()
    return dict(row)

# ====================================================
# ====================================================
# Publicações
# ====================================================
# ====================================================

QUERY_PUBLICACOES = (
    "SELECT guid, guid_anunciante, id_categoria, titulo, descricao, data_publicacao, data_validade, imagem "
    "FROM publicacao "
)

def salva_publicacao(publicacao):
    db = get_connection()
    cursor = db.cursor()

    # Convertendo datas para epoch
    data_publicacao = datetime.strptime(publicacao["data_publicacao"], "%Y-%m-%d %H:%M:%S").strftime("%s")
    data_validade   = datetime.strptime(publicacao["data_validade"], "%Y-%m-%d %H:%M:%S").strftime("%s")

    cursor.execute(
        "INSERT INTO publicacao (guid, guid_anunciante, id_categoria, titulo, descricao, data_publicacao, data_validade) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)", 
        (publicacao["guid"], 
         publicacao["guid_anunciante"], 
         publicacao["id_categoria"], 
         publicacao["titulo"], 
         publicacao["descricao"], 
         data_publicacao,
         data_validade)
    )
    db.commit()

def obtem_publicacoes_desde(data_inicio, ids_categorias):
    params = [data_inicio]
    params.extend(ids_categorias)
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(
        QUERY_PUBLICACOES + 
        "WHERE data_publicacao>=? "
        "AND id_categoria IN ({0})".format(','.join('?'*len(ids_categorias))), params)
    return convert_to_dict_list(cursor)

def obtem_publicacoes_por_anunciante(guid_anunciante):
    db = get_connection()
    cur = db.cursor()
    cur.execute(QUERY_PUBLICACOES + "WHERE guid_anunciante=?", (guid_anunciante,))
    return convert_to_dict_list(cur)

def obtem_publicacao(guid):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(QUERY_PUBLICACOES + "WHERE guid=?", (guid,))
    return dict(cursor.fetchone())

