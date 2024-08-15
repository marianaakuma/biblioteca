from flask import Flask, render_template, flash, redirect, request, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-palavra-secreta'


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/integrantes')
def integrantes():
    return render_template('integrates.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if email == "usuario@example.com" and senha == "senha123":
            return redirect(url_for('usuario')) 
        else:
            return "Credenciais inválidas", 
        
    return render_template('logi.html')


@app.route('/usuario')
def usuario():
    return render_template('biblioteca.html')


@app.route('/pagina-inicial')
def pagina_inicial():
    return render_template('pagina_inicial.html')


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar-senha']
    
    if senha != confirmar_senha:
        flash('As senhas não coincidem. Tente novamente.')
        return redirect(url_for('cadastro'))

    flash('Cadastro realizado com sucesso!')
    return redirect(url_for('cadastro'))


@app.route('/adm')
def adm():
    return render_template('adm.html')


if __name__ == '__main__':
    app.run(debug=True)




