#9 - Imprimir as n primeiras linhas do triângulo de Pascal:

#1

#1 1

#1 2 1

#1 3 3 1

#1 4 6 4 1

#1 5 10 10 5 1 …

n = int(input('Quantas linhas do triângulo de Pascal deseja imprimir? '))

mat = []
for i in range(n):
  mat.append([0] * n)

for i in range(n):
  for j in range(i+1):
    if j == 0 or j == i:
      mat[i][j] = 1
    else:
      mat[i][j] = mat[i-1][j-1] + mat[i-1][j]

for i in range(n):
  for j in range(i+1):
    print(mat[i][j],end=' ')
  print()