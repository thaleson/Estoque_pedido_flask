# from datetime import datetime, timedelta
# from random import randint, choice
# from app import app, db
# from app.models import Category, Product, Order, OrderedItem

# with app.app_context():
#     # Limpar dados antigos
#     db.session.query(OrderedItem).delete()
#     db.session.query(Order).delete()
#     db.session.commit()

#     # Criar alguns dados básicos
#     categories = Category.query.all()
#     products = Product.query.all()

#     # Adicionar 50 pedidos
#     for i in range(50):
#         order_date = datetime.now() - timedelta(days=randint(1, 30))
#         client_name = f"Cliente_{i + 1}"
#         status = choice(["Pendente", "Concluído", "Cancelado"])
#         order = Order(data=order_date, client=client_name, status=status)
#         db.session.add(order)
#         db.session.commit()

#         # Adicionar itens ao pedido
#         num_items = randint(1, 5)  # Cada pedido tem entre 1 a 5 itens
#         for _ in range(num_items):
#             product = choice(products)
#             amount = randint(1, 10)
#             unit_price = product.price
#             ordered_item = OrderedItem(order_id=order.id, product_id=product.id, amount=amount, unit_price=unit_price)
#             db.session.add(ordered_item)
        
#     db.session.commit()
#     print("50 pedidos foram adicionados com sucesso!")



# # from app import app, db

# with app.app_context():
#     db.drop_all()  # Remove todas as tabelas
#     db.create_all()  # Cria as tabelas novamente
#     print("Banco de dados reiniciado com sucesso!")




# @app.route('/add_product', methods=['GET', 'POST'])
# def add_product():
#     if request.method == 'POST':
#         # Adicionar produto
#         name = request.form['name']
#         description = request.form['description']
#         price = request.form['price']
#         quantity_in_stock = request.form['quantity_in_stock']
#         category_id = request.form['category_id']
#         new_product = Product(name=name, description=description, price=price, quantity_in_stock=quantity_in_stock, category_id=category_id)
#         db.session.add(new_product)
#         db.session.commit()

#         # Criar pedido
#         client = request.form.get('client')
#         status = request.form.get('status')
#         product_id = request.form.get('product_id')
#         quantity = request.form.get('quantity')

#         if client and status and product_id and quantity:
#             product = Product.query.get_or_404(product_id)
#             total_price = float(product.price) * int(quantity)
#             new_order = Order(data=datetime.now(), client=client, status=status)
#             db.session.add(new_order)
#             db.session.commit()
            
#             ordered_item = OrderedItem(order_id=new_order.id, product_id=product_id, amount=quantity, unit_price=total_price)
#             db.session.add(ordered_item)
#             db.session.commit()

#         return redirect(url_for('index'))
    
#     categories = Category.query.all()
#     products = Product.query.all()
#     return render_template('add_product.html', categories=categories, products=products)
