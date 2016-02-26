# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask, render_template, g
import public, user
from assets import assets
from extensions import bcrypt, cache, db, debug_toolbar, login_manager, migrate
from settings import ProdConfig

from flask.ext.sqlalchemy import SQLAlchemy
import os
import psycopg2
import urlparse


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/users'
#'postgres://hkwdxzsksohoae:mi4SH7b8_4fB4RhENknqsDj-A3@ec2-54-83-198-111.compute-1.amazonaws.com:5432/de336vejtlpkej'
db = SQLAlchemy(app)
"""
#urlparse.uses_netloc.append("postgres")
#url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database='de336vejtlpkej',
    user='hkwdxzsksohoae',
    password='mi4SH7b8_4fB4RhENknqsDj-A3',
    host='ec2-54-83-198-111.compute-1.amazonaws.com',
    port=5432
)
"""
def create_app(config_object=ProdConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    assets.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
