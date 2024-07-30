from flask import Flask, render_template, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-palavra-secreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():

    pizzas = [{'sabor': 'Camarão', 'preco': '150', 'imagem': 'camarao.webp'},
              {'sabor': 'Calabreza', 'preco': '50', 'imagem': 'calabreza.jfif'},
              {'sabor': 'Nordestina', 'preco': '60', 'imagem': 'nordestina.jpg'},
              {'sabor': 'Frango com Catupiry', 'preco': '55', 'imagem': 'pizza.jpg'},
              {'sabor': 'Quatro queijos', 'preco': '70', 'imagem': 'pizza.jpg'},
              {'sabor': 'Marguerita', 'preco': '60', 'imagem': 'pizza.jpg'},
              {'sabor': 'Havaiana', 'preco': '65', 'imagem': 'pizza.jpg'},
              {'sabor': 'Três quejos', 'preco': '45', 'imagem': 'pizza.jpg'}, 
              {'sabor': 'Portugesa', 'preco': '60', 'imagem': 'pizza.jpg'},
              {'sabor': 'Doce de leite', 'preco': '50', 'imagem': 'pizza.jpg'},
              {'sabor': 'Chocolate', 'preco': '50', 'imagem': 'pizza.jpg'},
            ]

    return render_template('cardapio.html', pizzas=pizzas)

@app.route('/login')
def login():
    return render_template('login.html')