#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

soma = 0
turma = int(input('digite o numero de turmas:'))
for i in range(turma):
  aluno = int(input('digite o numero de alunos'))
  soma = aluno + soma
  media = soma // turma
print('a media de alunos por turma é',media)  
