"""
- settings  for the flask aplication 
"""

class BaseConfig(object):
    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:example@db/main'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'itsmysecretkey'