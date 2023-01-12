#9 - Dadas duas listas de tamanho N, faça um programa que diga se as mesmas possuem conteúdo igual.

lista1 = []
lista2 = []
for i in range(5):
  n = int(input('digite um numero: '))
  n2 = int(input('digite o segundo numero: '))
  lista1.append(n)
  lista2.append(n2)
  x = n in lista1
  y = n2 in lista2
  if n == n2:
    print(x,'os numeros são iguais')
  elif n != n2:
    print('false os numeros são diferentes') 