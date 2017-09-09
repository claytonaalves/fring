from flask_sqlalchemy import SQLAlchemy

db = None

def init_database(app):
    global db
    db = SQLAlchemy(app)
    db.create_all()
    return db


