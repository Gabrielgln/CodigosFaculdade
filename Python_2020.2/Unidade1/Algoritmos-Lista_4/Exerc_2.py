# questão 2 
#Faça um programa para tabular a função:

#f(x,y)=(x4+3xy+y3)/(2xy+3x+4y+2)

#para x = 2, 4, 6, 8 e y = 1, 3, 5, 7, 9, para cada valor de x. Devem ser impressos os valores de x, de y e de f(x,y).

for x in range(2,9,2):
  for y in range(1,10,2):
    f = (x**4 + 3*x*y + y**3) / (2*x*y + 3*x + 4*y + 2)
    print('f(',x,',',y,') = ',f,sep='')