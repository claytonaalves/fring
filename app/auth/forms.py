#coding: utf8
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField
from wtforms.validators import DataRequired, Required

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
    cidade = SelectField(u'Cidade', choices=[('1', u'Alta Floresta - MT'), ('2', u'Apiacás - MT')])
    categoria = SelectField(u'Categoria', choices=[('1', u'Oficina'), ('2', u'Imobiliárias')])


