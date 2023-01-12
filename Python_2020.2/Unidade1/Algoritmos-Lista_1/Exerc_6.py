#Faça um programa que calcula o novo valor do salário de um funcionário. O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).

salario = float(input('qual o salario atual:'))
reajuste = float(input('total do reajuste:'))
ajustado = salario*reajuste / 100 + salario
print('o salario ajustado é de:', ajustado)
