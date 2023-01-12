#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto

r = int(input('digite um ano:'))
if r % 4 == 0:
  print('é bissexto')
else:
  print ('não é bissexto')

