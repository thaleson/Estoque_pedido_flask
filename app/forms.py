from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired

class DeleteOrderForm(FlaskForm):
    submit = SubmitField('Apagar')



class AddProductForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    description = StringField('Descrição')
    price = FloatField('Preço', validators=[DataRequired()])
    quantity_in_stock = IntegerField('Quantidade em Estoque', validators=[DataRequired()])
    category_id = IntegerField('Categoria ID', validators=[DataRequired()])
    image = FileField('Imagem')
    submit = SubmitField('Adicionar Produto')