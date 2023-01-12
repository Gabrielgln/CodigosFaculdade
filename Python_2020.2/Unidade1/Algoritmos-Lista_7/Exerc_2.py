#2 - Faça um programa que leia um vetor de caracteres de tamanho N, contendo as respostas de um candidato em uma prova
#de concurso. A seguir, leia outro vetor, dessa vez contendo o gabarito da prova. Gere um terceiro vetor,
#de booleanos, indicando os erros e acertos do candidato. Com base nesse vetor,
#imprima o percentual de questões acertadas pelo candidato.

def r_aluno(lista,tamanho):
  for i in range(tamanho):
    print('questão',i+1,':')
    lista[i] = int(input())

def gabarito(gab,tamanho):
  for i in range(tamanho):
    print('gabarito questão',i+1,':')
    gab[i] = int(input())

def comparação(tamanho):
  for i in range(tamanho):
    if lista2[i] == lista1[i]:
      lista3.append(lista1[i])
      
n = 4
lista1 = [0] * n
r_aluno(lista1,n)
print(lista1)
print()

lista2 = [0] * n
gabarito(lista2,n)
print(lista2)
print()

lista3 = []
comparação(n)
print(lista3,'todas as respostas que estão nessa lista foram certas!')
print('o total de acertos foram:',len(lista3))