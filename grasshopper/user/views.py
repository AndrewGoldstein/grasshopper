# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

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
def flightt():
    """Flights select page."""
    return render_template('users/flights.html')

@blueprint.route('/settings')
def setting():
    """Personal settings page."""
    return render_template('users/settings.html')