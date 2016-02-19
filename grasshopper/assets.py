# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment

css = Bundle(
    'libs/bootstrap/dist/css/bootstrap.css',
    'css/style.css',
    'bootstrap/css/bootstrap.min.css',
    'css/accordion_demo.css',
    'css/jumbotron_narrow.css',
    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
    'libs/jQuery/dist/jquery.js',
    'js/jquery.min.js',
    'libs/bootstrap/dist/js/bootstrap.js',
    'bootstrap/js/bootstrap.js',
    'js/javascript_commons.js',
    'js/plugins.js',
    'js/flight_list.js',
    'js/accordion.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)




 
