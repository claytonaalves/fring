from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from flask_simplelogin import login_required

# Define the blueprint: 'auth', set its url prefix: app.url/auth
teste = Blueprint('teste', __name__, url_prefix='/teste')

@teste.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return "ok"



