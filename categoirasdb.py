from app import app, db
from app.models import Category

# Lista de categorias a serem adicionadas
categories = [
    'Eletrônicos', 'Roupas', 'Calçados', 'Móveis', 'Livros', 'Brinquedos', 'Alimentos',
    'Beleza', 'Saúde', 'Esportes', 'Automóveis', 'Casa e Jardim', 'Ferramentas', 'Computadores',
    'Celulares', 'Cozinha', 'Jóias', 'Relógios', 'Materiais de Escritório', 'Cameras', 'Acessórios',
    'Hobbies', 'Vestuário', 'Decoração', 'Artigos para Festa', 'Instrumentos Musicais', 'Fitness',
    'Saúde e Bem-Estar', 'Pets', 'Outdoors', 'Bebês', 'Gastronomia', 'Eletrônicos de Consumo', 'Ciclismo'
]

# Cria um contexto de aplicação e adiciona as categorias
with app.app_context():
    for name in categories:
        category = Category(name=name)
        db.session.add(category)

    db.session.commit()

print("30 categorias adicionadas com sucesso!")
