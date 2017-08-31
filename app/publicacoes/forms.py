#coding: utf8
from flask_wtf import FlaskForm # , RecaptchaField
from wtforms import TextField, TextAreaField, DateField, DateTimeField
from wtforms.validators import Required, Email, EqualTo

class PublicacaoForm(FlaskForm):
    titulo = TextField(u'Título')
    descricao = TextAreaField(u'Descrição')
    data_validade = DateField()

