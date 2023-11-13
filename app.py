from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class cadesports:
    def __init__(self, nome, jogoInteresse, funcaoJogo, ranking):
        self.nome = nome
        self.jogoInteresse = jogoInteresse
        self.funcaoJogo = funcaoJogo
        self.ranking = ranking


Lista = []


@app.route('/esports')
def eSports():
    return render_template('Esports.html', Titulo = 'Torneio de eSports: ', ListaJogadores = Lista)


@app.route('/')
def inicio():
    return 'Começando'


@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = 'Cadastro de Jogadores')


@app.route("/criar", methods = ['POST'])
def criar():
    nome = request.form['nome']
    jogoInteresse = request.form['jogoInteresse']
    funcaoJogo = request.form['funcaoJogo']
    ranking = request.form['ranking']

    obj = cadesports(nome, jogoInteresse, funcaoJogo, ranking)

    Lista.append(obj)

    return redirect('/esports')


if __name__ == '__main__':
    app.run()
