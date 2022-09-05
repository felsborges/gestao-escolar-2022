from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

import sqlite3

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return redirect(url_for('alunos'))

@app.route('/alunos/')
def alunos():
    con = sqlite3.connect('gestao-escolar.db')
    cur = con.cursor()

    cur.execute('SELECT matricula, nome FROM alunos')

    alunos = cur.fetchall()

    con.close()

    return render_template('alunos.html', alunos=alunos)

@app.route('/alunos/<matricula>/editar', methods=('GET', 'POST'))
def aluno_editar(matricula):
    con = sqlite3.connect('gestao-escolar.db')
    cur = con.cursor()

    if request.method == 'POST':
        matricula = request.form['txt_matricula']
        nome = request.form['txt_nome']

        cur.execute(
            'UPDATE alunos SET nome = ? WHERE matricula = ?',
            (nome, matricula)
        )

        con.commit()

        con.close()

        return redirect(url_for('alunos'))

    cur.execute(
        'SELECT matricula, nome, ativo FROM alunos WHERE matricula = ?',
        (matricula,)
    )

    aluno = cur.fetchone()

    con.close()

    return render_template('aluno_editar.html', aluno=aluno)

# Rota para a página de cadastro de turmas
@app.route('/turmas/cadastro', methods=('GET', 'POST'))
def turmas_cadastro():
    if request.method == 'POST':
        alunos = request.form.getlist('alunos')

        return alunos

    con = sqlite3.connect('gestao-escolar.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    sql_professores = 'SELECT matricula, nome FROM professores ORDER BY nome'
    cur.execute(sql_professores)
    professores = cur.fetchall()

    sql_alunos = 'SELECT matricula, nome FROM alunos WHERE ativo=1 ORDER BY nome'
    cur.execute(sql_alunos)
    alunos = cur.fetchall()

    con.close()

    # A função render_template tem o propósito de ler os arquivos
    #   que estão disponíveis na pasta 'templates' e apresentar no
    #   navegado do usuário
    # NOTE: o nome do arquivo é um texto
    return render_template(
        'turmas_cadastro.html',
        professores=professores,
        alunos=alunos
    )