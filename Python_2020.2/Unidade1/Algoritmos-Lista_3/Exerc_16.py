#Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

soma = 0
for i in range(10):
  idade = int(input('digite sua idade:'))
  soma = idade + soma
media = soma/10
if media > 0 and media <= 26:
  print('jovem')
elif media < 60:
  print('adulta')
elif media > 60:
  print('idosa')

