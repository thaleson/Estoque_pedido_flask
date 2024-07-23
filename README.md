
# Estoque e Pedidos

**Estoque e Pedidos** é um sistema web para gerenciamento de estoque e pedidos. Ele permite adicionar produtos, criar pedidos, e visualizar categorias e pedidos. Desenvolvido com Flask e Bootstrap, oferece uma interface moderna e funcional.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
estoquepedidosflask/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
│       ├── base.html
│       ├── add_product.html
│       ├── categorias.html
│       ├── pedidos.html
│       └── ...
│
├── instance/
│   └── config.py
│
├── migrations/
│   └── ...
│
├── static/
│   ├── styles.css
│   └── favicon.ico
│
├── .gitignore
├── config.py
├── requirements.txt
└── run.py
```

### Descrição dos Arquivos e Diretórios

- **app/**: Contém a lógica principal do aplicativo.
  - `__init__.py`: Configura o Flask e as extensões (SQLAlchemy, Migrate, CSRFProtect).
  - `models.py`: Define os modelos de dados.
  - `routes.py`: Define as rotas e a lógica para as páginas.
  - `templates/`: Contém os arquivos de template HTML.
- **instance/**: Contém arquivos de configuração específicos da instância.
  - `config.py`: Configurações específicas, como a chave secreta.
- **migrations/**: Armazena os arquivos de migração do banco de dados.
- **static/**: Contém arquivos estáticos, como CSS e ícones.
  - `styles.css`: Estilos personalizados.

- **.gitignore**: Lista arquivos e pastas a serem ignorados pelo Git.
- **config.py**: Configurações gerais do projeto.
- **requirements.txt**: Lista de dependências do projeto.
- **run.py**: Script para iniciar o aplicativo Flask.

## Como Funciona

### Página Inicial (Início)

A página inicial fornece uma visão geral do sistema e links para as principais funcionalidades.

### Categorias

Nesta página, você pode visualizar e gerenciar categorias de produtos. É possível adicionar, editar e excluir categorias.

### Pedidos

Esta página lista todos os pedidos feitos. Você pode visualizar detalhes dos pedidos e seu status.

### Adicionar Produto

Aqui você pode adicionar novos produtos ao estoque. Inclua informações como nome, descrição, preço, quantidade em estoque e categoria.

### Criar Pedido

Permite criar novos pedidos. Inclua informações sobre o cliente, status do pedido, produto e quantidade.

## Como Executar o Projeto

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/thaleson/Estoque_pedido_flask
    cd estoque-e-pedidos
    ```

2. **Crie um ambiente virtual e ative-o:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados e aplique as migrações:**

    ```bash
    flask db upgrade
    ```

5. **Execute o aplicativo:**

    ```bash
    python run.py
    ```

6. **Acesse o aplicativo em:**

    ```
    http://127.0.0.1:5000
    ```

## Contribuindo

Se você deseja contribuir com melhorias ou correções, por favor, faça um fork do repositório, crie uma branch para suas mudanças, e envie um pull request. 

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

