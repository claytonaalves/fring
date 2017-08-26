from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.auth.forms import LoginForm
from app.auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('auth.home'))
        flash('Wrong email or password', 'error-message')
    return render_template("auth/signin.html", form=form)

