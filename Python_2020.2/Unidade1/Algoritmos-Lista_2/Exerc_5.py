#Fa�a um Programa que leia tr�s n�meros e mostre-os em ordem decrescente.

n1 = int(input('digite um numero:'))
n2 = int(input('digite um numero:'))
n3 = int(input('digite um numero:'))

if (n1 > n2 > n3):
  print('a sequencia �:', n1, n2, n3)

elif (n1 > n3 > n2):
  print('a sequencia �:',n1, n3, n2)

elif (n2>n3>n1):
  print('a sequencia �:', n2, n3, n1) 

elif (n2>n1>n3):
  print('a sequencia �:', n2, n1, n3)

elif (n3>n1>n2):
  print('a sequencia �:', n3, n1, n2)

elif (n3>n2>n1):
  print('a sequencia �:', n3, n2, n1)
