#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

valor = int(input('Valor para calcular o fatorial: '))
fatorial = 1
num = valor
while num > 1:
  fatorial = fatorial * num
  num = num - 1
print('O fatorial de',valor,'é',fatorial)
