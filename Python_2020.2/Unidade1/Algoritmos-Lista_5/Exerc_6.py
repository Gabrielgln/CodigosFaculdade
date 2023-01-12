#6 - Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A prova consta de 10 questões,
#cada uma com cinco alternativas identificadas por A, B, C, D e E. Para isso são dados:

#o cartão gabarito;

#o número de alunos da turma;

#o cartão de respostas para cada aluno, contendo o seu número e suas respostas.

nQuestoes = 3

gabarito = [0] * nQuestoes
for i in range(nQuestoes):
  print('Questão',i+1)
  gabarito[i] = input()

nAlunos = int(input('Número de alunos da turma: '))

for aluno in range(nAlunos):
  print('Aluno',aluno+1)
  respostas = [0] * nQuestoes
  for questao in range(nQuestoes):
    print('Questão',questao+1)
    respostas[questao] = input()
  cont = 0
  for questao in range(nQuestoes):
    if respostas[questao] == gabarito[questao]:
      cont = cont + 1
  print('O aluno',aluno+1,'acertou',cont,'questões.')