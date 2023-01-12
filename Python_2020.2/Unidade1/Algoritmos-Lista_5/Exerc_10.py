#10 - Faça um programa que leia uma quantidade de números determinada pelo usuário e armazene em uma lista.
#Crie outras duas listas, uma para os valores pares e outra para os ímpares.

lista = []
pares = []
impares = []
q = int(input('digite a quantidade de valores para comparação: '))
for i in range(q):
  n = int(input('digite um numero: '))  # vetor[i] = int(input('digite um numero: '))
  lista.append(n)
  if n % 2 == 0:  # vetor[i] % 2 == 0:
    pares.append(n)              
  elif n % 2 != 0:
    impares.append(n)
print('os numeros digitados foram: ',lista)
print('os numeros pares são: ',pares)
print('os numeros impares são: ',impares) 