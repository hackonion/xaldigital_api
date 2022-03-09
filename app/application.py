""" 
- flask app instance and registers the database object
"""

from flask import Flask
from routes.DwRoutes import api
from model.DwModel import db

def create_app(app_name='DW_API'):
    
    app = Flask(app_name)
    app.config.from_object('config.config.BaseConfig')
    app.register_blueprint(api, url_prefix="/api")
    
    db.init_app(app)
    
    return app