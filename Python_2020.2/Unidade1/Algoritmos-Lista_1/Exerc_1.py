#Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) e quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de combustível o usuário obterá com esses valores.

combustivel = float(input('valor do litro de combustivel:'))
dinheiro = float(input('dinheiro gasto:'))
total = dinheiro/combustivel
print('o valor que o usuario obterar será', total)
