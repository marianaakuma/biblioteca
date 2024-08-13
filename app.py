from flask import Flask, render_template, flash, redirect, request, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-palavra-secreta'


#Página inicial do site
@app.route('/')
def index():
    return render_template('index.html')

#Página que exibe a lista de livros disponíveis
@app.route('/generos')
def generos():

    livros = [
    {'id': 1, 'titulo': 'Dom Casmurro', 'ano': '1899', 'imagem': 'Dom Casmurro.jpg'},
    {'id': 2, 'titulo': '1984', 'ano': '1949', 'imagem': 'George Orwell.jpg'},
    {'id': 3, 'titulo': 'O Sol é para Todos', 'ano': '1960', 'imagem': 'O Sol é para Todos.jpg'},
    {'id': 4, 'titulo': 'Cem Anos de Solidão', 'ano': '1967', 'imagem': 'Cem Anos de Solidão.jpg'},
    {'id': 5, 'titulo': 'O Senhor dos Anéis: A Sociedade do Anel', 'ano': '1954', 'imagem': 'O Senhor dos Anéis.jpg'},
    {'id': 6, 'titulo': 'The Great Gatsby', 'ano': '1925', 'imagem': 'The Great Gatsby.jpg'},
    {'id': 7, 'titulo': 'Orgulho e Preconceito', 'ano': '1813', 'imagem': 'Orgulho e Preconceito.jpg'},
    {'id': 8, 'titulo': 'O Apanhador no Campo de Centeio', 'ano': '1951', 'imagem': 'O Apanhador no Campo de Centeio.jpg'},
    {'id': 9, 'titulo': 'A Revolução dos Bichos', 'ano': '1945', 'imagem': 'A Revolução dos Bichos.jpg'},
    {'id': 10, 'titulo': 'O Pequeno Príncipe', 'ano': '1943', 'imagem': 'O Pequeno Príncipe.jpg'},
    {'id': 11, 'titulo': 'A Menina que Roubava Livros', 'ano': '2005', 'imagem': 'A Menina que Roubava Livros.jpg'},
]

    return render_template('generos.html', livros=livros)


@app.route('/logi')
def logi():
    return render_template('logi.html')





