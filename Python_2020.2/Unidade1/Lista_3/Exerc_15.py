#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

primo = True
numero = int(input('Digite um valor pra saber se é primo: '))
for i in range(2,numero,1):
  if numero % i == 0:
    primo = False

if primo:
  print('É primo.')
else:
  print('Não é primo.')
