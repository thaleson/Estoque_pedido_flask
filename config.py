import os 



class Config:

    SECRET_KEY = os.environ.get('83b1b438fbf15272efd7ce9a8759a9d1007f4d2a227c570e') or 'Key very securition'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False