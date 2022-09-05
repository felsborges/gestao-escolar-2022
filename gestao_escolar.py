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

# Rota para a página de cadastro de turmas
@app.route('/turmas/cadastro', methods=('GET', 'POST'))
def turmas_cadastro():
    # Verificar se o método de envio é o POST
    if request.method == 'POST':
        # Caso seja POST, significa que foi enviado um formário

        # Capturar os dados que foram enviados pelo formulário
        # Para este formulário foram enviadas os seguintes campos:
        #   dt_inicio
        #   dt_fim
        #   turno
        #   professor <- A matrícula do professor
        #   alunos <- Uma lista de matrículas dos alunos

        # Para os casos de listas, utilizamos o método .getlist (captura de listas), aonde é necessário
        #   passar por parâmetro o nome do campo
        alunos = request.form.getlist('alunos')

        # Captura dos campos simples do formulário
        dt_inicio = request.form['dt_inicio']
        dt_fim = request.form['dt_fim']
        turno = request.form['turno']
        mat_professor = request.form['professor']

        con = sqlite3.connect('gestao-escolar.db')
        cur = con.cursor()

        sql = f"INSERT INTO turmas ( dt_inicio, dt_fim, turno, mat_professor ) VALUES ( '{dt_inicio}', '{dt_fim}', '{turno}', {mat_professor} )"
        cur.execute( sql )

        # O código da turma é gerado pelo banco de dados, sendo assim é preciso captura-lo utilizando
        #   o atributo .lastrowid, disponível no objeto cursor
        codigo_turma = cur.lastrowid

        # O método .commit é utilizado para confirmar as alterações que acontecem nas tabelas
        #   por exemplo um comando de inserção
        con.commit()

        # A variável alunos contém uma lista de alunos captura pelo método .getlist
        # Uma maneira de navegar na lista de alunos é utilizar a estrutura for
        for aluno in alunos:
            sql = f"INSERT INTO matriculas VALUES ( {codigo_turma}, {aluno} )"
            cur.execute( sql )

            con.commit()

        con.close()
        
        return redirect(url_for('alunos'))

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