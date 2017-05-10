import sqlite3

DATABASE = 'database.db'

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

def todas_categorias():
    db = get_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM categoria")
    return convert_to_dict_list(cur)

def anunciantes_por_categoria(idcategoria):
    db = get_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM anunciante WHERE idcategoria=?", (idcategoria,))
    return convert_to_dict_list(cur)

def anunciante_por_id(idanunciante):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM anunciante WHERE _id=?", (idanunciante,))
    row = cursor.fetchone()
    return dict(row)

def salva_anuncio(anuncio):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO anuncio (titulo, descricao, valido_ate, idcategoria) "
        "VALUES (?, ?, ?, ?)", 
        (anuncio["titulo"], anuncio["descricao"], anuncio["valido_ate"], anuncio["id_categoria"]))
    db.commit()

def convert_to_dict_list(cursor):
    r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r


