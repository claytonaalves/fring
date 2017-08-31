from flask import session
from app.anunciantes.models import Anunciante

def login_checker(user):
    anunciante = Anunciante.query.filter_by(email=user.get('username')).first()
    if not anunciante:
        return False
    valid_credentials = user.get('password')==anunciante.senha
    if valid_credentials:
        session['guid_anunciante'] = anunciante.guid_anunciante
    return valid_credentials

