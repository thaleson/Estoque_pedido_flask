from flask import flash, render_template, request, redirect, url_for
from app import app, db
from app.forms import DeleteOrderForm
from app.models import Category, Order, OrderedItem, Product
from datetime import datetime

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/categories')
def categories():
    try:
        categories = Category.query.all()
        return render_template('categorias.html', categories=categories)
    except Exception as e:
        return f"Erro ao carregar categorias: {e}", 500


@app.route('/category/<int:category_id>')
def category(category_id):
    try:
        category = Category.query.get_or_404(category_id)
        products = Product.query.filter_by(category_id=category_id).all()
        return render_template('category_products.html', category=category, products=products)
    except Exception as e:
        return f"Erro ao carregar a categoria: {e}", 500


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    orders = Order.query.all()
    delete_form = DeleteOrderForm()  # Cria uma instância do formulário
    if request.method == 'POST':
        if delete_form.validate_on_submit():
            order_id = request.form.get('order_id')
            if order_id:
                delete_order(order_id)  # Chama a função de exclusão
                flash('Pedido removido com sucesso!', 'success')
                return redirect(url_for('orders'))

    return render_template('pedidos.html', orders=orders, delete_form=delete_form)


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
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

        # Criar pedido
        client = request.form.get('client')
        status = request.form.get('status')
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')

        if client and status and product_id and quantity:
            product = Product.query.get_or_404(product_id)
            total_price = float(product.price) * int(quantity)
            new_order = Order(data=datetime.now(), client=client, status=status)
            db.session.add(new_order)
            db.session.commit()
            
            ordered_item = OrderedItem(order_id=new_order.id, product_id=product_id, amount=quantity, unit_price=total_price)
            db.session.add(ordered_item)
            db.session.commit()

        return redirect(url_for('index'))
    
    categories = Category.query.all()
    products = Product.query.all()
    return render_template('add_product.html', categories=categories, products=products)

@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        # Antes de remover o produto, remova ou atualize as referências
        ordered_items = OrderedItem.query.filter_by(product_id=product_id).all()
        for item in ordered_items:
            db.session.delete(item)  # ou ajuste conforme necessário

        db.session.delete(product)
        db.session.commit()
        flash('Produto removido com sucesso!', 'success')
    else:
        flash('Produto não encontrado.', 'error')
        return redirect(url_for('index'))

    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash('Produto removido com sucesso!', 'success')
    else:
        flash('Produto não encontrado.', 'error')
        return redirect(url_for('index'))

    product = Product.query.get(product_id)
    if product:
        # Remover item das ordens (opcional)
        OrderedItem.query.filter_by(product_id=product_id).delete()
        # Remover o produto
        db.session.delete(product)
        db.session.commit()
        flash('Produto removido com sucesso!', 'success')
    else:
        flash('Produto não encontrado.', 'error')
        return redirect(url_for('index'))

    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Erro ao remover o produto: {e}", 500


@app.route('/delete_order/<int:order_id>', methods=['POST'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
    return redirect(url_for('pedidos'))



def requests():
    orders = Order.query.all()
    delete_form = DeleteOrderForm()
    return render_template('pedidos.html', orders=orders, delete_form=delete_form)

@app.route('/create_order', methods=['POST'])
def create_order():
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

        return redirect(url_for('orders'))
    except Exception as e:
        return f"Erro ao criar o pedido: {e}", 500
