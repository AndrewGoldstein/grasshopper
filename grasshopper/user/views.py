# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request
from flask_login import login_required, LoginManager
from grasshopper.extensions import login_manager
from grasshopper.user.forms import CreditcardForm
from grasshopper.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route('/')
#@login_required
def jumbo():
    """Flight start page."""
    return render_template('users/jumbotron.html')

@blueprint.route('/members')
def members():
    """members page."""
    return render_template('users/members.html')

@blueprint.route('/flights')
def flights():
    """Flights select page."""
    return render_template('users/flights.html')

@blueprint.route('/settings', methods=['GET', 'POST'])
def settings():
    """Personal settings page."""
    form = CreditcardForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        print form.number.data
        print form.expiry.data
        print form.cvc.data
        User.update(load_user(1), commit=True, card_number=form.number.data, expiration=form.expiry.data, cvc=form.cvc.data, active=True)
    return render_template('users/settings.html', form=form)




