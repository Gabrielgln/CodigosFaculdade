#Fa�a um programa que solicite ao usu�rio o valor do litro de combust�vel (ex. 4,75) e quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de combust�vel o usu�rio obter� com esses valores.

combustivel = float(input('valor do litro de combustivel:'))
dinheiro = float(input('dinheiro gasto:'))
total = dinheiro/combustivel
print('o valor que o usuario obterar ser�', total)
