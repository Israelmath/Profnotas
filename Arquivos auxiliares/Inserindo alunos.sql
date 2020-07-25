INSERT INTO Aluno 
	( Nome, Sobrenome, Turma, Serie, Numero)
VALUES 
	('Israel', 'Alves', 'A', 3, 15),
	('Joice', 'Moreli', 'B', 2, 14),
	('Rafaela', 'Gomes', 'C', 1, 24),
	('Ismael', 'Lucena', 'D', 8, 15);

INSERT INTO Notas1tri (R1) VALUES (3);
INSERT INTO Notas2tri (R1) VALUES (3);
INSERT INTO Notas3tri (R1) VALUES (3);

INSERT INTO Notas1tri (R1) VALUES (2);
INSERT INTO Notas2tri (R1) VALUES (2);
INSERT INTO Notas3tri (R1) VALUES (2);

INSERT INTO Notas1tri (R1) VALUES (1);
INSERT INTO Notas2tri (R1) VALUES (1);
INSERT INTO Notas3tri (R1) VALUES (1);

INSERT INTO Notas1tri (R1) VALUES (8);
INSERT INTO Notas2tri (R1) VALUES (8);
INSERT INTO Notas3tri (R1) VALUES (8);

/*
SELECT * FROM Aluno;

SELECT * FROM Notas1tri;
SELECT * FROM Notas2tri;
SELECT * FROM Notas3tri;
*/

SELECT Nome, R1, R2, R3, R4, Participacao, Prova, Rec, Qtd 
FROM Aluno A
RIGHT JOIN Notas1tri B
ON A.Id = B.Id
WHERE A.Id = 4;

