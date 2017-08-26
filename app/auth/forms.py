from flask_wtf import Form # , RecaptchaField
from wtforms import TextField, PasswordField # BooleanField
from wtforms.validators import Required, Email, EqualTo

class LoginForm(Form):
    email    = TextField('E-mail', [Email(),
                Required(message='Forgot your email address?')])
    password = PasswordField('Senha', [
                Required(message='Must provide a password. ;-)')])
