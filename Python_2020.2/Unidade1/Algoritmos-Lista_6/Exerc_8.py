#8 - Faça programa que leia uma matriz 3 x 6 com valores reais.

#Imprima a soma de todos os elementos das colunas ímpares.

#Imprima a média aritmética dos elementos da segunda e quarta colunas.

#Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.

#Imprima a matriz modificada.

m = []
l = 3
c = 6
for i in range(l):
  m.append([0] * c)

for i in range(l):
  for j in range(c):
    print('\nM = [',i+1,',',j+1,'] : ',end='')
    m[i][j] = int(input())

for i in range(l):
  for j in range(c):
    print(m[i][j],end=' ')
  print()

for i in range(l):
  for j in range(1,c,2):
    print(m[i][j],end=' ')
  print()

soma = 0
soma1 = 0
for i in range(l):
  for j in range(c):
    if j == 1:
      soma = soma + m[i][j] / l
    elif j == 3:
      soma1 = soma1 + m[i][j] / l
print('a soma aritmética dos valores da coluna 2 é: ',soma)
print('a soma aritmética dos valores da coluna 4 é: ',soma1)

s1 = 0
s2 = 0
st = 0
for i in range(l):
  for j in range(c):
    if j == 0:
      s1 = s1 + m[i][j]
    elif j == 1:
      s2 = s2 + m[i][j]

st = s1 + s2

for i in range(l):
  for j in range(c):
    if j == 5:
      m.append([0] * m[i][j])
      m[i][j] = st

for i in range(l):
  for j in range(c):
    print(m[i][j],end=' ')
  print()