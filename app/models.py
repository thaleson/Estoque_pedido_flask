from app import db

class Category(db.Model):
    """
    Representa a tabela 'categories' no banco de dados.

    Attributes:
        id (int): Identificador único da categoria.
        name (str): Nome da categoria.
        products (relationship): Relação com a tabela 'products', onde uma categoria pode ter muitos produtos.
    """
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    """
    Representa a tabela 'products' no banco de dados.

    Attributes:
        id (int): Identificador único do produto.
        name (str): Nome do produto.
        description (str): Descrição do produto.
        price (float): Preço do produto.
        quantity_in_stock (int): Quantidade disponível em estoque.
        category_id (int): Identificador da categoria a qual o produto pertence.
        image_url (str): URL da imagem do produto.
        ordered_items (relationship): Relação com a tabela 'ordered_items', onde um produto pode ter muitos itens de pedido.
    """
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)
    quantity_in_stock = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    image_url = db.Column(db.String(255))

    ordered_items = db.relationship('OrderedItem', backref='product', cascade='all, delete-orphan')


class Order(db.Model):
    """
    Representa a tabela 'orders' no banco de dados.

    Attributes:
        id (int): Identificador único do pedido.
        data (datetime): Data e hora do pedido.
        client (str): Nome do cliente que fez o pedido.
        status (str): Status do pedido (ex. 'Pendente', 'Concluído', 'Cancelado').
        items (relationship): Relação com a tabela 'ordered_items', onde um pedido pode ter muitos itens.
    """
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=False)
    client = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    items = db.relationship('OrderedItem', backref='order', lazy=True)


class OrderedItem(db.Model):
    """
    Representa a tabela 'ordered_items' no banco de dados.

    Attributes:
        id (int): Identificador único do item de pedido.
        order_id (int): Identificador do pedido ao qual o item pertence.
        product_id (int): Identificador do produto que foi pedido.
        amount (int): Quantidade do produto no pedido.
        unit_price (float): Preço unitário do produto no momento do pedido.
    """
    __tablename__ = 'ordered_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
