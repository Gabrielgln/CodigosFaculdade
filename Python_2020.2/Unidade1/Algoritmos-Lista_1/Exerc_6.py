#Fa�a um programa que calcula o novo valor do sal�rio de um funcion�rio. O usu�rio informa o sal�rio atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).

salario = float(input('qual o salario atual:'))
reajuste = float(input('total do reajuste:'))
ajustado = salario*reajuste / 100 + salario
print('o salario ajustado � de:', ajustado)
