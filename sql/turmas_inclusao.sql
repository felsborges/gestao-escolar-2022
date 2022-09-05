-- Comando para inclusão de registros em uma tabela
INSERT INTO turmas
-- Dentro dos parenteses é necessário listar as colunas que serão
--   utilizadas para inserir os registros
( dt_inicio, dt_fim, turno, mat_professor )
-- O values são os valores que será associados as colunas
-- O valores estão entre parenteses
VALUES
-- A coluna mat_professor se refere a uma matrícula disponível
--   na tabela professores
( '2022-09-01', '2022-09-30', 'NOITE', 1 )
