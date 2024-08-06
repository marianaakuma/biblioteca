from flask import Flask, render_template, flash, redirect, request, url_for

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

#Página de login onde o usuário pode inserir suas credenciais
@app.route('/login')
def login():
    return render_template('login.html')

#Autenticação do usuário. Verifica se o nome de usuário e senha estão corretos.
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


#Página de pesquisa de livros. Exibe resultados com base no termo de pesquisa fornecido
@app.route('/pesquisa', methods=['GET', 'POST'])
def pesquisa():
    resultados = []
    if request.method == 'POST':
        termo = request.form.get('termo', '').lower()
        resultados = [livro for livro in livros if termo in livro['titulo'].lower()]
    return render_template('pesquisa.html', resultados=resultados)


#Marcar um livro como favorito, adicionando seu ID à sessão do usuário
@app.route('/marcar_favorito/<int:livro_id>')
def marcar_favorito(livro_id):
    favoritos = session.get('favoritos', [])
    if livro_id not in favoritos:
        favoritos.append(livro_id)
        session['favoritos'] = favoritos
    return redirect(url_for('detalhes', livro_id=livro_id))

#Remover um livro dos favoritos, removendo seu ID da sessão do usuário
@app.route('/remover_favorito/<int:livro_id>')
def remover_favorito(livro_id):
    favoritos = session.get('favoritos', [])
    if livro_id in favoritos:
        favoritos.remove(livro_id)
        session['favoritos'] = favoritos
    return redirect(url_for('detalhes', livro_id=livro_id))


#Exibir a descrição de um livro específico, incluindo a informação se ele está nos favoritos.
@app.route('/descricao/<int:livro_id>')
def descricao(livro_id):
    livro = next((livro for livro in livros if livro['id'] == livro_id), None)
    favorito = livro_id in session.get('favoritos', [])
    return render_template('descricao.html', livro=livro, favorito=favorito)

#Exibir a lista de livros que o usuário marcou como favoritos
@app.route('/favoritos')
def lista_favoritos():
    favoritos = session.get('favoritos', [])
    livros_favoritos = [livro for livro in livros if livro['id'] in favoritos]
    return render_template('favoritos.html', livros=livros_favoritos)

# Rotas de Administração
@app.route('/admin')
def admin():
    return render_template('admin/index.html', livros=livros)


#Página para adicionar um novo livro ao catálogo
@app.route('/admin/adicionar', methods=['GET', 'POST'])
def adicionar_livro():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        ano = int(request.form.get('ano'))
        descricao = request.form.get('descricao')
        novo_id = max(livro['id'] for livro in livros) + 1
        livros.append({
            'id': novo_id,
            'titulo': titulo,
            'autor': autor,
            'ano': ano,
            'descricao': descricao
        })
        return redirect(url_for('admin'))
    return render_template('admin/adicionar.html')


#Página para editar as informações de um livro existente
@app.route('/admin/editar/<int:livro_id>', methods=['GET', 'POST'])
def editar_livro(livro_id):
    livro = next((livro for livro in livros if livro['id'] == livro_id), None)
    if request.method == 'POST':
        livro['titulo'] = request.form.get('titulo')
        livro['autor'] = request.form.get('autor')
        livro['ano'] = int(request.form.get('ano'))
        livro['descricao'] = request.form.get('descricao')
        return redirect(url_for('admin'))
    return render_template('admin/editar.html', livro=livro)


#Excluir um livro do catálogo com base no ID fornecido
@app.route('/admin/excluir/<int:livro_id>')
def excluir_livro(livro_id):
    global livros
    livros = [livro for livro in livros if livro['id'] != livro_id]
    return redirect(url_for('admin'))

    if __name__ == '__main__':
    app.run(debug=True)