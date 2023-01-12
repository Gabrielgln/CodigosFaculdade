#Faça um programa que leia 10 números e informe o maior número.

for i in range(10):
  valor = int(input('digite um numero: '))
  if i == 0:
    maior = valor
  elif valor > maior:
    maior = valor  
print('numero maior é:',maior)   
