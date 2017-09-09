#coding: utf8
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel
from core.database import init_database

app = Flask(__name__)
app.config.from_object('config')

db = init_database(app)

from core.cidades.models import Cidade
from core.categorias.models import Categoria
from core.anunciantes.models import Anunciante
from core.publicacoes.models import Publicacao

admin = Admin(app, name=u"Manutenção")
babel = Babel(app)

class CidadeView(ModelView):
    column_exclude_list = ['categorias']
    form_excluded_columns = ['categorias']
    form_choices = {
        'uf': [
            ('AC', u'AC - Acre'),
            ('AL', u'AL - Alagoas'),
            ('AP', u'AP - Amapá'),
            ('AM', u'AM - Amazonas'),
            ('BA', u'BA - Bahia'),
            ('CE', u'CE - Ceará'),
            ('DF', u'DF - Distrito Federal'),
            ('ES', u'ES - Espírito Santo'),
            ('GO', u'GO - Goiás'),
            ('MA', u'MA - Maranhão'),
            ('MT', u'MT - Mato Grosso'),
            ('MS', u'MS - Mato Grosso do Sul'),
            ('MG', u'MG - Minas Gerais'),
            ('PA', u'PA - Pará'),
            ('PB', u'PB - Paraíba'),
            ('PR', u'PR - Paraná'),
            ('PE', u'PE - Pernambuco'),
            ('PI', u'PI - Piauí'),
            ('RJ', u'RJ - Rio de Janeiro'),
            ('RN', u'RN - Rio Grande do Norte'),
            ('RS', u'RS - Rio Grande do Sul'),
            ('RO', u'RO - Rondônia'),
            ('RR', u'RR - Roraima'),
            ('SC', u'SC - Santa Catarina'),
            ('SP', u'SP - São Paulo'),
            ('SE', u'SE - Sergipe'),
            ('TO', u'TO - Tocantins')
        ]
    }

class CategoriaView(ModelView):
    column_exclude_list = ['anunciantes']
    form_excluded_columns = ['anunciantes']

@babel.localeselector
def get_locale():
    return 'pt_BR'

admin.add_view(CidadeView(Cidade, db.session))
admin.add_view(CategoriaView(Categoria, db.session))

