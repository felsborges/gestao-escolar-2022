CREATE TABLE matriculas (
    cod_turma INTEGER REFERENCES turmas (codigo) 
                      NOT NULL,
    mat_aluno INTEGER REFERENCES alunos (matricula) 
                      NOT NULL
);
