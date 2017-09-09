#coding: utf8
from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_simplelogin import SimpleLogin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

admin = Admin(app)
babel = Babel(app)

from app.auth import login_checker

login_manager = SimpleLogin(app, login_checker=login_checker)
login_manager.config['home_url'] = '/login/'
login_manager.messages['login_failure'] = u'Credenciais inválidas!'
login_manager.messages['logout'] = u''

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/', methods=['GET'])
def index():
    return redirect('/publicacoes')

@babel.localeselector
def get_locale():
    return 'pt_BR'

from app.teste.controllers import teste
from app.publicacoes.controllers import blueprint as publicacoes
from app.auth.controllers import auth

# remover depois
from app.cidades.models import Cidade
from app.categorias.models import Categoria
from app.anunciantes.models import Anunciante
from app.publicacoes.models import Publicacao

admin.add_view(ModelView(Cidade, db.session))
admin.add_view(ModelView(Categoria, db.session))

app.register_blueprint(teste)
app.register_blueprint(auth)
app.register_blueprint(publicacoes)

db.create_all()
