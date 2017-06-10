import sqlite3

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
# Anuncios
# ====================================================
# ====================================================

def salva_anuncio(anuncio):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO anuncio (guid, titulo, descricao, valido_ate, id_categoria, guid_anunciante) "
        "VALUES (?, ?, ?, ?, ?, ?)", 
        (anuncio["guid"], anuncio["titulo"], anuncio["descricao"], 
         anuncio["valido_ate"], anuncio["id_categoria"],
         anuncio["guid_anunciante"]))
    db.commit()

def anuncios_por_anunciante(guid_anunciante):
    db = get_connection()
    cur = db.cursor()
    cur.execute(
        "SELECT titulo, descricao, valido_ate, id_categoria, imagem "
        "FROM anuncio "
        "WHERE guid_anunciante=?", (guid_anunciante,))
    return convert_to_dict_list(cur)


def obtem_anuncio(guid_anuncio):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM anuncio WHERE guid=?", (guid_anuncio,))
    return dict(cursor.fetchone())

