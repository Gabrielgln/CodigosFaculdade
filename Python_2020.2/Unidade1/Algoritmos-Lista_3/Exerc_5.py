#Fa�a um programa que leia 10 n�meros e informe o maior n�mero.

for i in range(10):
  valor = int(input('digite um numero: '))
  if i == 0:
    maior = valor
  elif valor > maior:
    maior = valor  
print('numero maior �:',maior)   
