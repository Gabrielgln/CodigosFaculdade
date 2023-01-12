#questão 1

#Implemente um programa que exiba a tabuada do 2 ao 9.

for valor in range(2,10,1):
  print('Tabuada do',valor)
  for i in range(1,11,1):
    print(valor,'x',i,'=',valor*i) 
  print()