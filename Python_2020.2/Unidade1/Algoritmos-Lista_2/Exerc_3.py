#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('digite um numero:'))
n2 = int(input('digite um numero:'))
n3 = int(input('digite um numero:'))
if n1 >= n2 and n1 >= n3:
  print ('maior:', n1)
  if n2 <= n3:
    print ('menor:', n2)
  else:
    print ('menor:',n3)

elif n2 >= n1 and n2 >= n3:
  print ('maior:',n2)
  if n1 <= n3:
    print('menor:',n1)
  else:
    print('menor:',n3)

else:
  print('maior:',n3)
  if n2 <= n1:
    print('menor:',n2)
  else:
    print('menor:',n1)   

