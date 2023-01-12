#2 - Faça uma função que receba uma matriz e suas dimensões.
#A função deve substituir por zero todos os elementos negativos da matriz

def criação_matriz(matrix,linhas,colunas):
  for i in range(linhas):
    matrix.append([0] * colunas)

def leitura_matriz(matrix,linhas, colunas):
  for i in range(linhas):
    for j in range(colunas):
      matrix[i][j] = int(input())
  return matriz

def parazero(matriz,linhas,colunas):
  for i in range(linhas):
    for j in range(colunas):
      if (matriz[i][j] < 0):
        matriz[i][j] = 0
  return matriz

def print(matriz,linhas,colunas):
  for i in range(linhas):
    print("/", end = " ")
    for j in range(colunas):
      print(f'{matriz[i][j]:^5}', end = " ")
    print("/")

matriz = []
l = int(input("Número de linhas: "))
c = int(input("Número de colunas: "))
criação_matriz(matriz,l,c)
leitura_matriz(matriz,l,c)
parazero(matriz,l,c)
print(matriz,l,c)

