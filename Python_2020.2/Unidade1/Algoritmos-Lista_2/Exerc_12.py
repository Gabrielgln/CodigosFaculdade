#Fa�a um Programa para um caixa eletr�nico. O programa dever� perguntar ao usu�rio o valor do saque e depois informar quantas notas de cada valor ser�o fornecidas. As notas dispon�veis ser�o as de 1, 5, 10, 50 e 100 reais.
#O valor m�nimo � de 10 reais e o m�ximo de 600 reais. O programa n�o deve se preocupar com a quantidade de notas existentes na m�quina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece tr�s notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

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
