#Fa�a um programa que leia um nome de usu�rio e a sua senha e n�o aceite a senha igual ao nome do usu�rio, mostrando uma mensagem de erro e voltando a pedir as informa��es.

nome = input('Nome do usu�rio: ')
senha = input('Senha: ')
while nome == senha:
  print('Nome e senha n�o podem ser iguais')
  senha = input('Senha:')
