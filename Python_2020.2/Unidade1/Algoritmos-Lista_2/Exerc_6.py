#Fa�a um Programa que pergunte em que turno voc� estuda.
#Pe�a para digitar
#M-matutino
#V-Vespertino
#N-Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inv�lido!", conforme o caso.

turno = input('qual o seu turno? (m, V ou N)')
if turno == 'M':
  print('bom dia!')
elif turno == 'V':
  print('boa tarde!')
elif turno == 'N':
  print('boa noite!')
else:
  print('op��o inv�lida.') 
