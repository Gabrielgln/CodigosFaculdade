#Fa�a um programa que fa�a 5 perguntas para uma pessoa sobre um crime. As perguntas s�o:
#"Telefonou para a v�tima?"
#"Esteve no local do crime?"
#"Mora perto da v�tima?"
#"Devia para a v�tima?"
#"J� trabalhou com a v�tima?"
#O programa deve no final emitir uma classifica��o sobre a participa��o da pessoa no crime. Se a pessoa responder positivamente a 2 quest�es ela deve ser classificada como "Suspeita", entre 3 e 4 como "C�mplice" e 5 como "Assassino". Caso contr�rio, ele ser� classificado como "Inocente".

print('digite 1 para sim e 0 para n�o')
tel = int(input('telefonou para vitima ?'))
local = int(input('esteve no local do crime ?'))
mora = int(input('mora perto da vitima ?'))
deve = int(input('devia para a vitima ?'))
trab = int(input('ja trabalhou com a vitima ?'))

total_ = tel + local + mora + deve + trab

if (total_ == 2):
  print('suspeita')

elif (total_ == 3 or total_ == 4):
  print('cumplice')

elif (total_ == 5):
  print('assasino')

else:
  print('inocente')   
