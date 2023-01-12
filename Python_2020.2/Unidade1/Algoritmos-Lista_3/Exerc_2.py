#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input('Nome do usuário: ')
senha = input('Senha: ')
while nome == senha:
  print('Nome e senha não podem ser iguais')
  senha = input('Senha:')
