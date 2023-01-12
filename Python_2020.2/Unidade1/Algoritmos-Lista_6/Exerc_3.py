#3 - Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posição das matrizes lidas.

ordem = 2
m = []
mt = []
for i in range(ordem):
  m.append([0] * ordem)

for i in range(ordem):
  for j in range(ordem):
    print('\nM = [',i+1,',',j+1,']: ',end='')
    m[i][j] = int(input())

for i in range(ordem):
  for j in range(ordem):
    print(m[i][j],end=' ')
  print()

maior = m[0][0]
for i in range(ordem):
  for j in range(ordem):
    if maior < m[i][j]:
      mt.append(m[i][j])
print(mt)