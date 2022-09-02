CREATE TABLE turmas (
    codigo        INTEGER       PRIMARY KEY AUTOINCREMENT,
    dt_inicio     DATE          NOT NULL,
    dt_fim        DATE          NOT NULL,
    turno         VARCHAR (255) NOT NULL,
    mat_professor INTEGER       REFERENCES professores (matricula) 
);
