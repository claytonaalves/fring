# encoding: utf8
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from core.database import db
from core.cidades.models import Cidade


class CadastroForm(FlaskForm):
    nome_fantasia = TextField(u"Nome Fantasia", validators=[DataRequired(message=u"Este campo é obrigatório")])
    razao_social = TextField(u"Razão Social")
    telefone = TextField(u"Telefone")
    celular = TextField(u"Celular")
    logradouro = TextField(u"Rua")
    numero = TextField(u"Número")
    bairro = TextField(u"Bairro")
    email = TextField(u"E-mail")
    senha = PasswordField(u"Senha")
    cidade = SelectField(u'Cidade', validators=[DataRequired(message="Informe uma cidade")], coerce=int)
    categoria = SelectField(u'Categoria', validators=[DataRequired(message="Informe uma categoria")], coerce=int)
