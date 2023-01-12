#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
#O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

numero = int(input('saque um valor [ 10 - 600 ]:'))
valor = numero

cem = numero // 100
numero = numero % 100

cinquenta = numero//50
numero = numero % 50

dez = numero // 10
numero = numero % 10

cinco = numero // 5

um = numero 

print('notas de 100:', cem)
print('notas de 50:', cinquenta)
print('notas de 10:', dez)
print('notas de 5:', cinco)
print('notas de 1:', um)
