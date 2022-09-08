#Faça um programa que leia um valor inteiro e mostre na tela uma sequência incluindo os dois números que vem antes, o número digitado, e os dois números que vem depois dele. Ex.: digitou 5; o programa mostra 3 4 5 6 7.

n = int(input('digite o numero:'))
resultado = n-2, n-1, n, n+1, n+2
print('o resultado é:', resultado)
