from flask import Flask, render_template, redirect, url_for, request

import sqlite3

app = Flask(__name__)

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
