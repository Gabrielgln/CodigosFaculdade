#1 - Faça um programa que leia números inteiros para uma lista. O usuário irá informar esses números até que informe zero 
(que não deve ser inserido na lista). Imprima a lista e exclua todas as ocorrências de um valor informado pelo usuário.

vetor = []
num = int(input('digite um numero: '))
while num != 0:
  vetor.append(num)
  num = int(input('digite um numero: '))
print(vetor)
num = int(input('digite um valor para apagar: '))

while num in vetor:
  vetor.remove(num)
print(vetor)  