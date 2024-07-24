from flask import flash, render_template, request, redirect, url_for
from app import app, db
from app.forms import DeleteOrderForm
from app.models import Category, Order, OrderedItem, Product
from datetime import datetime

@app.route('/')
def index():
    """
    Renderiza a página inicial com a lista de produtos disponíveis.
    """
    delete_form = DeleteOrderForm()
    products = Product.query.all()
    return render_template('index.html', products=products, delete_form=delete_form)

@app.route('/categories')
def categories():
    """
    Renderiza a página de categorias com a lista de categorias disponíveis.
    """
    try:
        categories = Category.query.all()
        return render_template('categorias.html', categories=categories)
    except Exception as e:
        return f"Erro ao carregar categorias: {e}", 500

@app.route('/category/<int:category_id>')
def category(category_id):
    """
    Renderiza a página de produtos de uma categoria específica.
    """
    try:
        category = Category.query.get_or_404(category_id)
        products = Product.query.filter_by(category_id=category_id).all()
        return render_template('category_products.html', category=category, products=products)
    except Exception as e:
        return f"Erro ao carregar a categoria: {e}", 500

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    """
    Renderiza a página de pedidos com a lista de pedidos existentes e um formulário para deletar pedidos.
    """
    orders = Order.query.all()
    delete_form = DeleteOrderForm()

    if request.method == 'POST':
        if delete_form.validate_on_submit():
            order_id = request.form.get('order_id')
            if order_id:
                delete_order(order_id)
                flash('Pedido removido com sucesso!', 'success')
                return redirect(url_for('orders'))

    return render_template('pedidos.html', orders=orders, delete_form=delete_form)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """
    Adiciona um novo produto e cria um pedido (se informações do pedido forem fornecidas).
    """
    if request.method == 'POST':
        # Adicionar produto
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        quantity_in_stock = request.form['quantity_in_stock']
        category_id = request.form['category_id']
        new_product = Product(name=name, description=description, price=price, quantity_in_stock=quantity_in_stock, category_id=category_id)
        db.session.add(new_product)
        db.session.commit()

        # Criar pedido, se informações do pedido forem fornecidas
        client = request.form.get('client')
        status = request.form.get('status')
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')

        if client and status and product_id and quantity:
            try:
                product = Product.query.get_or_404(product_id)
                total_price = float(product.price) * int(quantity)
                new_order = Order(data=datetime.now(), client=client, status=status)
                db.session.add(new_order)
                db.session.commit()

                ordered_item = OrderedItem(order_id=new_order.id, product_id=product_id, amount=quantity, unit_price=total_price)
                db.session.add(ordered_item)
                db.session.commit()

                flash('Produto e pedido adicionados com sucesso!', 'success')
            except Exception as e:
                db.session.rollback()
                flash(f'Erro ao criar o pedido: {e}', 'error')

        return redirect(url_for('index'))
    
    categories = Category.query.all()
    products = Product.query.all()
    return render_template('add_product.html', categories=categories, products=products)

@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    """
    Remove um produto do banco de dados e suas referências em itens de pedidos.
    """
    product = Product.query.get(product_id)
    if product:
        try:
            # Remover itens relacionados ao produto
            OrderedItem.query.filter_by(product_id=product_id).delete()
            db.session.delete(product)
            db.session.commit()
            flash('Produto removido com sucesso!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao remover o produto: {e}', 'error')
    else:
        flash('Produto não encontrado.', 'error')

    return redirect(url_for('index'))

@app.route('/delete_order/<int:order_id>', methods=['POST'])
def delete_order(order_id):
    """
    Remove um pedido do banco de dados.
    """
    order = Order.query.get(order_id)
    if order:
        try:
            # Remover itens associados ao pedido
            OrderedItem.query.filter_by(order_id=order_id).delete()
            db.session.delete(order)
            db.session.commit()
            flash('Pedido removido com sucesso!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao remover o pedido: {e}', 'error')
    else:
        flash('Pedido não encontrado.', 'error')

    return redirect(url_for('orders'))

@app.route('/create_order', methods=['POST'])
def create_order():
    """
    Cria um novo pedido com os detalhes fornecidos e adiciona itens ao pedido.
    """
    try:
        client = request.form['client']
        status = request.form['status']
        product_id = request.form['product_id']
        quantity = int(request.form['quantity'])

        product = Product.query.get_or_404(product_id)
        total_price = product.price * quantity

        new_order = Order(data=datetime.now(), client=client, status=status)
        db.session.add(new_order)
        db.session.commit()

        ordered_item = OrderedItem(order_id=new_order.id, product_id=product_id, amount=quantity, unit_price=total_price)
        db.session.add(ordered_item)
        db.session.commit()

        flash('Pedido criado com sucesso!', 'success')
        return redirect(url_for('orders'))
    except Exception as e:
        db.session.rollback()
        return f"Erro ao criar o pedido: {e}", 500
