#Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

n = int(input('Digite a quantidade de termos: '))

soma = 0
print('H =',end=' ')
for i in range(1,n+1,1):
  soma = soma + 1/i
  if i == 1:
    print(1,end=' ')
  else:
    print('+ 1/',i,end=' ',sep='')
print()
print(soma)
