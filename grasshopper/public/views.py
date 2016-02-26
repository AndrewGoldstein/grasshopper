# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for, g
from flask_login import login_required, login_user, logout_user

from grasshopper.extensions import login_manager
from grasshopper.public.forms import LoginForm
from grasshopper.user.forms import RegisterForm
from grasshopper.user.models import User
from grasshopper.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            with open("foo.py", "w") as f:
                f.write("X=" + str(form.user.id))
            #flash('You are logged in.', 'success')
            #redirect_url = request.args.get('next') or url_for('user.jumbo')
            return redirect(url_for('user.jumbo'))
        else:
            flash_errors(form)
    return render_template('public/home.html', form=form)


@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    #flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
        print form.username.data
        print form.email.data
        print form.password.data
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)


@blueprint.route('/about/')
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template('public/about.html', form=form)

"""
@blueprint.route('/db')
def dbtest():
    try:
        #User.create(username="aaaa", email="aaaa@gmail.com", password="aaaa", active=True)
        print "hey"
        User.create(username='John1', email='Foo1@bar.com', password="aaaa1", active=True)
        #db.session.add(user)
        #db.session.commit()
        print "success"
    except Exception as e:
        f = open('/tmp/error.log', 'w')
        f.write(e.message)
        f.close()
        return 'done'
    return 'done2'
"""