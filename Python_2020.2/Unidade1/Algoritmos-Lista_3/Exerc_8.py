#Fa�a um programa que receba dois n�meros inteiros e gere os n�meros inteiros que est�o no intervalo compreendido por eles.

valor1 = int(input('digite um numero:'))
valor2 = int(input('digite um numero:'))
for i in range(valor1,valor2+1,1):
  print(i,end=' ')
