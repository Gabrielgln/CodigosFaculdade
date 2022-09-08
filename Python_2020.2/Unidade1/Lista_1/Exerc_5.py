#Faça um programa que calcule a conversão monetária de Real para Dólar. O usuário informa o valor da cotação do dólar (ex.: 3,78) e quanto em real deseja converter (ex. 150,00). O programa exibe quantos dólares valem os reais informados.

dolar = float(input('qual o valor da cotação do dolar:'))
real = float(input('valor que vai ser convertido:'))
valor = dolar*real
print('o valor convertido para dolar sera de:', valor)
