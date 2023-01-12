#Faça um programa que calcula o tempo (em anos) que uma pessoa irá demorar para poupar R$ 1.000.000,00 (Um Milhão de Reais). O usuário informa o salário mensal e o total de despesas mensais.

mensal = float(input('qual salario mensal:'))
despesa = float(input('total de despesas:'))
salarioReajustado = (mensal-despesa) * 12
ano = 1000000 / (salarioReajustado)
print('você irá demorar', ano, 'anos para poupar 1000000 R$')
