import os 



class Config:

    SECRET_KEY = os.environ.get('7d94d6ed1a2248e318ca19a5c65eed325f68a24e8a9356ba') or 'Key very securition'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False