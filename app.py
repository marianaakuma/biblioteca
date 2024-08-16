from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-palavra-secreta'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['post'])
def login():
    nome = request.form.get('nome')
    nome = request.form.get('senha')

    if nome == 'igor' and senha =='123':
         return render_template("usuario.html")

    print('nome')
    print('senha')
    return redirect('/')


@app.route('/')
def cadastro():
    return render_template('cadastro.html')

@app.route('/')
def usuario():
    return render_template('usuario.html')

@app.route('/')
def paginainicial():
    return render_template('paginainicial.html')

@app.route('/')
def adm():
    return render_template('adm.html')


@app.route('/')
def integrate():
    return render_template('integrate.html')






if __name__ == '__main__':
    app.run(debug=True)

