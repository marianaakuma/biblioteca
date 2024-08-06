from flask import Flask, render_template, flash, redirect, request, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-palavra-secreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generos')
def generos():

    Livros = [{'titulos': 'Dom Casmurro','1899','imagem': 'camarao.webp'},
              {'titulos': ' George Orwell ','1984','imagem':'calabreza.jfif'},
              {'titulos': 'O Sol é para Todos','1960','imagem':'nordestina.jpg'},
              {'titulos': 'Cem Anos de Solidão','(1967','imagem': 'pizza.jpg'},
              {'titulos': 'O Senhor dos Anéis: A Sociedade do Anel','1954','imagem': 'pizza.jpg'},
              {'titulos': 'The Great Gatsby','1925','imagem': 'pizza.jpg'},
              {'titulos': 'Orgulho e Preconceito','1813','imagem': 'pizza.jpg'},
              {'titulos': 'O Apanhador no Campo de Centeio','1951','imagem': 'pizza.jpg'}, 
              {'titulos': 'A Revolução dos Bichos','1945','imagem': 'pizza.jpg'},
              {'titulos': 'O Pequeno Príncipe','1943','imagem': 'pizza.jpg'},
              {'titulos': 'A Menina que Roubava Livros','2005','imagem': 'pizza.jpg'},
            ]

    return render_template('generos.html', livros=livros)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    if usuario == 'admin' and senha == 'senha123':
        return 'Bem vindo!'
    else:
        flash('Dados incorretos. Login ou senha inválidos', 'danger')
        flash('Tente novamente', 'warning')
        return redirect(url_for('login'))