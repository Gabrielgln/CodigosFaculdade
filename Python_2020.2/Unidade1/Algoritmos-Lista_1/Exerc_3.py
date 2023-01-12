#Faça um programa que calcule o valor a ser pago por uma dívida em atraso. O usuário deve informar o valor original da dívida (ex. 50,00), a quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. 0,25).

original = float(input('valor da divida inicial:'))
dias = float(input('dias em atraso:'))
juros = float(input('juros por dia:'))
cobrado = (juros*dias) + original
print('o valor da divida em atraso é:', cobrado)
