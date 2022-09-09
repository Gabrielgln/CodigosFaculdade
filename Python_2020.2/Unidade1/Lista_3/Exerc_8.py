#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

valor1 = int(input('digite um numero:'))
valor2 = int(input('digite um numero:'))
for i in range(valor1,valor2+1,1):
  print(i,end=' ')
