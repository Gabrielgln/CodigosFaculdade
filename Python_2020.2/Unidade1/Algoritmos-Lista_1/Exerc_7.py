#Fa�a um programa que calcula o tempo (em anos) que uma pessoa ir� demorar para poupar R$ 1.000.000,00 (Um Milh�o de Reais). O usu�rio informa o sal�rio mensal e o total de despesas mensais.

mensal = float(input('qual salario mensal:'))
despesa = float(input('total de despesas:'))
salarioReajustado = (mensal-despesa) * 12
ano = 1000000 / (salarioReajustado)
print('voc� ir� demorar', ano, 'anos para poupar 1000000 R$')
