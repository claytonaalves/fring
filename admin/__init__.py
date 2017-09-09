#coding: utf8
import os
import uuid

from flask import Flask, Markup, url_for
from flask_admin import Admin, form
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel
from werkzeug.utils import secure_filename
from core.database import init_database

images_base_path = os.path.join(os.getcwd(), 'images')

app = Flask(__name__, static_folder=images_base_path)
app.config.from_object('config')

db = init_database(app)

from core.cidades.models import Cidade
from core.categorias.models import Categoria
from core.anunciantes.models import Anunciante
from core.publicacoes.models import Publicacao

admin = Admin(app, name=u"Manutenção")
babel = Babel(app)

def _imagename_uuid1_gen(obj, file_data):
    _, ext = os.path.splitext(file_data.filename)
    uid = uuid.uuid1()
    return secure_filename('{}{}'.format(uid, ext))

def _list_thumbnail(view, context, model, name):
    if not model.imagem:
        return ''

    return Markup(
        '<img src="/images/categorias/{imagem}" style="width: 150px;">'.format(imagem=model.imagem)
    )

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
    form_excluded_columns = ['anunciantes', 'imagem']
    column_formatters = {
        'imagem': _list_thumbnail
    }
    form_extra_fields = {
        'filename': form.ImageUploadField(
            'Imagem',
            base_path=os.path.join(images_base_path, 'categorias'),
            url_relative_path='images/',
            namegen=_imagename_uuid1_gen,
        )
    }

    def on_model_change(self, form, model, is_created=False):
        super(CategoriaView, self).on_model_change(form, model, is_created)
        model.imagem = form.filename.data.filename

@babel.localeselector
def get_locale():
    return 'pt_BR'

admin.add_view(CidadeView(Cidade, db.session, name="Cidades"))
admin.add_view(CategoriaView(Categoria, db.session, name="Categorias"))

