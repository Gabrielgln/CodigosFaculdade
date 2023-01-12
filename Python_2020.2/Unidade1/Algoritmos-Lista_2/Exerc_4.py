#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input('quanto custa o café:'))
p2 = float(input('quanto custa o leite:'))
p3 = float(input('quanto custa o cereal:'))
if (p1 > p2 and p1 > p3 and p2 > p3):
  b = p3
elif (p1 > p2 and p3 > p2 and p1 > p3):
  b = p2
elif (p2 > p1 and p3 > p1 and p3 > p2):
  b = p1
print( 'você deve comprar o produto que custa:', b)
