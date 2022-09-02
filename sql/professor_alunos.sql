SELECT
    prof.matricula AS mat_professor,
    prof.nome AS prof_nome,
    tur.codigo,
    tur.dt_inicio,
    tur.turno,
    mat.mat_aluno,
    alu.nome AS alu_nome
FROM
    professores AS prof
INNER JOIN
    turmas AS tur ON prof.matricula = tur.mat_professor
INNER JOIN
    matriculas AS mat ON tur.codigo = mat.cod_turma
INNER JOIN
    alunos AS alu ON mat.mat_aluno = alu.matricula
WHERE
    prof.nome = 'Felipe'