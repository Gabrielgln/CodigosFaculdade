#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer n�mero inteiro entre 1 a 10. O usu�rio deve informar de qual n�mero ele deseja ver a tabuada. A sa�da deve ser conforme o exemplo abaixo: Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

valor = int(input('digite um valor:'))
for i in range(1,11):
  t = valor * i
  print(valor,'x',i,'=',t)
