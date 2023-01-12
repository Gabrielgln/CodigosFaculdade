#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input('digite um numero:'))
n2 = int(input('digite um numero:'))
n3 = int(input('digite um numero:'))

if (n1 > n2 > n3):
  print('a sequencia é:', n1, n2, n3)

elif (n1 > n3 > n2):
  print('a sequencia é:',n1, n3, n2)

elif (n2>n3>n1):
  print('a sequencia é:', n2, n3, n1) 

elif (n2>n1>n3):
  print('a sequencia é:', n2, n1, n3)

elif (n3>n1>n2):
  print('a sequencia é:', n3, n1, n2)

elif (n3>n2>n1):
  print('a sequencia é:', n3, n2, n1)
