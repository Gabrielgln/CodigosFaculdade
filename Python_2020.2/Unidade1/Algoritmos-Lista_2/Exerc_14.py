#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print('digite 1 para sim e 0 para não')
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
