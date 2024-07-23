from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired

class DeleteOrderForm(FlaskForm):
    """
    Formulário para excluir um pedido.

    Attributes:
        submit (SubmitField): Botão para confirmar a exclusão do pedido.
    """
    submit = SubmitField('Apagar')


class AddProductForm(FlaskForm):
    """
    Formulário para adicionar um novo produto.

    Attributes:
        name (StringField): Nome do produto. Campo obrigatório.
        description (StringField): Descrição do produto. Opcional.
        price (FloatField): Preço do produto. Campo obrigatório.
        quantity_in_stock (IntegerField): Quantidade em estoque do produto. Campo obrigatório.
        category_id (IntegerField): Identificador da categoria à qual o produto pertence. Campo obrigatório.
        image (FileField): Imagem do produto. Opcional.
        submit (SubmitField): Botão para confirmar a adição do produto.
    """
    name = StringField('Nome', validators=[DataRequired()])
    description = StringField('Descrição')
    price = FloatField('Preço', validators=[DataRequired()])
    quantity_in_stock = IntegerField('Quantidade em Estoque', validators=[DataRequired()])
    category_id = IntegerField('Categoria ID', validators=[DataRequired()])
    image = FileField('Imagem')
    submit = SubmitField('Adicionar Produto')
