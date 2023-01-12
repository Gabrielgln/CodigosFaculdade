#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.

cont_pares = 0
cont_impares = 0
for i in range(10):
  valor = int(input('digite um valor:'))
  if valor % 2 == 0:
    cont_pares = cont_pares + 1
  else:
    cont_impares = cont_impares + 1
print('foram', cont_pares, 'pares', cont_impares, 'impares')
