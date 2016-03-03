# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request, redirect, url_for, g, flash
from flask_login import login_required, LoginManager
from grasshopper.extensions import login_manager
from grasshopper.user.forms import CreditcardForm
from grasshopper.user.models import User
from grasshopper.utils import flash_errors

from foo import X

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))

@blueprint.route('/')
def jumbo():
    """Flight start page."""
    return render_template('users/testingjumbotron.html')

@blueprint.route('/members')
def members():
    """members page."""
    return render_template('users/members.html')

@blueprint.route('/testing')
def tst():
    """members page."""
    return render_template('users/testing2.html')


@blueprint.route('/flights')
def flights():
    """Flights select page."""
    return render_template('users/flights.html')

@blueprint.route('/settings', methods=['GET', 'POST'])
def settings():
    """Personal settings page."""

    form = CreditcardForm(request.form, csrf_enabled=False)
    if request.method == 'POST':
        if form.validate_on_submit():
            User.update(load_user(X), commit=True, card_number=form.number.data, expiration=form.expiry.data, cvc=form.cvc.data, address_line1=form.address_line1.data, address_line2=form.address_line2.data, address_zip=form.address_zip.data, address_city=form.address_city.data, address_state=form.address_state.data, address_country=form.address_country.data, date_of_birth=form.date_of_birth.data, phone=form.phone.data, full_name=form.full_name.data, active=True) # full_name=form.full_name.data
            return redirect(url_for('user.summary'))
        else:
            print "error"
            flash_errors(form)
            #flash('Invalid password provided', 'error')
    return render_template('users/settings.html', form=form)

@blueprint.route('/summary')
def summary():
    """members page."""
    return render_template('users/summary.html')



