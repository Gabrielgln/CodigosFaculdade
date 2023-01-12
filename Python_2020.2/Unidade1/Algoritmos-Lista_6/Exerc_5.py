#5 - Leia uma matriz de ordem n, informada pelo usuário. Calcule a soma dos elementos que estão acima da diagonal principal.

n = int(input('Informe a ordem da matriz: '))

mat = []
for i in range(n):
  mat.append([0] * n)

for i in range(n):
  for j in range(n):
    print('mat[',i+1,',',j+1,']: ',sep='',end='')
    mat[i][j] = int (input())

for i in range(n):
  for j in range(n):
    print(mat[i][j],end=' ')
  print()

soma = 0
for i in range(n):
  for j in range(n):
    if j > i:
      soma = soma + mat[i][j]
print('A soma dos elementos acima da diagonal principal é',soma)