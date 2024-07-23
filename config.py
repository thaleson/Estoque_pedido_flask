import os 



class Config:

    SECRET_KEY = os.environ.get('Secret_key') or 'Key very securition'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False