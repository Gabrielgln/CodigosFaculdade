#14 - Faça um programa que leia N valores para um vetor, com N informado pelo usuário.
#Em seguida o usuário deve inserir mais um valor, em uma posição por ele determinada. Não use o método insert do python.

vetor = []
q = 5
for i in range(q):
  num = int(input('digite um valor: '))
  vetor.append(num)
print(vetor)  
for i in range(q):
  print('digite um valor para substituir a posição',i,':')
  vetor[i] = int(input())
  
vetor.append(vetor[i])
vetor.pop()
print(vetor)