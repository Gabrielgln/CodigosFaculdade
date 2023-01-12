#5 - Considere duas matrizes quadradas de ordem N. solicite uma linha e uma coluna e troque os valores
#da posição correspondente entre as matrizes. Imprima as duas matrizes antes e depois da troca.

def criação(matriz,ordem):
  for i in range(ordem):
    matriz.append([0] * ordem)

def leitura(matriz,ordem):
  for i in range(ordem):
    for j in range(ordem):
      print('\nM[',i+1,',',j+1,'] :',end='')
      matriz[i][j] = int(input())

def impressao(matriz,ordem):
  for i in range(ordem):
    for j in range(ordem):
      print(matriz[i][j],end=' ')
    print()


def troca (matriz1,matriz2,ordem):
  linha = int(input('qual linha será trocada? '))
  coluna = int(input('qual coluna será trocada? '))
  linha = linha - 1
  coluna = coluna - 1
  t = 0
  for i in range(ordem):
    for j in range(ordem):
      if i == linha and j == coluna:
        t = matriz1[i][j]
        matriz1.append([0] * matriz1[i][j])
        matriz1[i][j] = matriz2[i][j]
        matriz2.append([0] * matriz2[i][j])
        matriz2[i][j] = t
  impressao(m1,n)
  impressao(m2,n)  

m1 = []
m2 = []
n = int(input('digite a ordem da matriz: '))

print('informções sobre a primeira matriz:')
criação(m1,n)
leitura(m1,n)
impressao(m1,n)
print('informções sobre a segunda matriz:')
criação(m2,n)
leitura(m2,n)
impressao(m2,n)
print('troca das matrizes!')
troca(m1,m2,n)
