#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor pago em cada um.

CD = int(input('qual a quantidade de CDs?'))
v = 0
for i in range(CD):
  valor = float(input('qual o valor pago?'))
  v = v + valor
m = v / CD
print('o valor gasto na coleção de CD´s foi de: ',v,'e o valor medio dos CD´s é: ',m)  
