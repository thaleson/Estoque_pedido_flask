"""
Inicializa a aplicação Flask e configura as extensões.

Este módulo configura a aplicação Flask com as seguintes extensões:
- SQLAlchemy para interações com o banco de dados.
- Flask-Migrate para migrações de banco de dados.
- Flask-WTF para proteção contra CSRF (Cross-Site Request Forgery).

O módulo também carrega a configuração da aplicação a partir do arquivo de configuração
definido em `config.Config`.

Imports:
- `Flask`: O objeto principal da aplicação Flask.
- `SQLAlchemy`: Extensão para SQLAlchemy que fornece um ORM (Object Relational Mapper).
- `Migrate`: Extensão para gerenciar migrações de banco de dados.
- `CSRFProtect`: Extensão para proteção contra ataques CSRF.

Atributos:
- `app`: Instância da aplicação Flask configurada com as extensões.
- `db`: Instância do SQLAlchemy configurada para trabalhar com a aplicação Flask.
- `migrate`: Instância do Flask-Migrate para gerenciar migrações do banco de dados.
- `csrf`: Instância do Flask-WTF para proteção contra CSRF.

O módulo importa os módulos `models` e `routes` que definem os modelos de dados e as rotas da aplicação, respectivamente.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)
from app import models, routes
