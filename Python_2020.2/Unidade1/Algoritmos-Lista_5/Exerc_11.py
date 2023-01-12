#11 - Faça um programa que leia um vetor de 10 posições e verifique se existem valores repetidos e os escreva na tela.

nValores = 10
vetor = [0] * nValores
for i in range(nValores):
  print('Valor',i+1)
  vetor[i] = int(input())
print(vetor)

nValores = 10
vetor = [6,5,4,5,7,9,1,1,4,9]

for i in range(0,nValores-1,1):
  j = i + 1
  while j < nValores and vetor[i] != vetor[j]:
    j = j + 1
  if vetor[i] == vetor[j]:
    print(vetor[i])