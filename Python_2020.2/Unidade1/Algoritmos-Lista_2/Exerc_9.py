#Fa�a um programa que calcule as ra�zes de uma equa��o do segundo grau, na forma ax2 + bx + c. O programa dever� pedir os valores de a, b e c e fazer as consist�ncias, informando ao usu�rio nas seguintes situa��es:
#Se o usu�rio informar o valor de A igual a zero, a equa��o n�o � do segundo grau e o programa n�o deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equa��o n�o possui raizes reais. Informe ao usu�rio e encerre o programa;
#Se o delta calculado for igual a zero a equa��o possui apenas uma raiz real; informe-a ao usu�rio;
#Se o delta for positivo, a equa��o possui duas raiz reais; informe-as ao usu�rio;

a = float(input('digite o valor de A:'))
b = float(input('digite o valor de B:'))
c = float(input('digite o valor de C:'))
delta = b*b - 4*a*c
if a == 0:
  print('encerrado')
if delta <= -1: 
  print('encerrado')
elif delta == 0:
  print('possui uma raiz real')
elif delta >= 1:
  print('possui duas raizes')    
