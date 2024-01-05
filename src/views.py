from src import app, db
from flask import render_template, url_for, request, redirect
from src.models import Contato
from src.forms import ContatoForm

@app.route('/')
def homepage():
    usuario = 'Henrique'
    idade = 20

    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template('index.html', context=context)

@app.route('/nova', methods=['GET', 'POST'])
def newRoute():
    context = {}

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa-get')
        context.update({'pesquisa-get': pesquisa})

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        contato = Contato(
            nome = nome,
            email = email,
            assunto = assunto,
            mensagem = mensagem
        )

        db.session.add(contato)
        db.session.commit()
        
    return render_template('contato.html', context=context)

@app.route('/conta')
def conta():
    #replicando um vídeo que eu vi na internet
    context = {}
    soma = ''
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 and num2:
        
        soma = num1+num2

    context.update({'soma': soma})

    return render_template('conta.html', context=context)



@app.route('/contato', methods=['GET', 'POST'])
def contatoCerto():
    form = ContatoForm()
    context = {}

    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
            
    return render_template('contato2.html', context=context, form = form)