#4 - Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da forma:

#A[i][j] = 2i + 7j − 2 se i < j;

#A[i][j] = 3i2 − 1 se i = j;

#A[i][j] = 4i3 − 5j2 + 1 se i > j.

nlinhas = 3
ncolunas = 5

matriz = []
for i in range(nlinhas):
  matriz.append([0] * ncolunas)

for i in range(nlinhas):
  for j in range(ncolunas):
    if i < j:
      matriz[i][j] = 2 * i + 7 * j - 2
    elif i == j:
      matriz[i][j] = 3*i**2 - 1
    else:
      matriz[i][j] = 4*i**3 - 5*j*j + 1

for i in range(nlinhas):
  for j in range(ncolunas):
    print(matriz[i][j],end=' ')
  print()