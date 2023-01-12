#13 - Faça um programa que leia um total de 10 valores para um vetor.
#Substitua todas as ocorrências de valores negativos por 0 e imprima o vetor final.

vetor = []
for i in range(10):
  print('digite valor',i+1,': ')
  num = int(input())
  vetor.append(num)
  if num < 0:
    vetor.remove(num)
    vetor.append(0)
print(vetor)  