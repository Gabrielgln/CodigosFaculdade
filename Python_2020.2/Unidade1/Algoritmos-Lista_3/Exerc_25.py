#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n = int(input('Quantos termos possuirá a equação? '))
soma = 0
print('S =',end=' ')
for i in range(1,n+1,1):
  soma = soma + i/(i*2-1)
  if (i != 1):
    print('+ ',i,'/',i*2-1,end=' ',sep='')
  else:
    print(i,'/',i*2-1,end=' ',sep='')
print()
print(soma)
