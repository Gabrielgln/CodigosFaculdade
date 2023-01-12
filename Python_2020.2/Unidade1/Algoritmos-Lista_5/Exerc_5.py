#5 - Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento
#e a posição que ele se encontra.

vetor = []
maior = 0
for i in range(10):
  num = int(input('digite um numero: '))
  vetor.append(num)
  x = max(vetor)
print('o maior valor digitado pelo o usuario é: ',x)