#7 - Faça um programa que leia uma matriz de dimensões informadas pelo usuário. Dado um valor,
#verifique quantas vezes algum múltiplo desse valor aparece na matriz.

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

def verificar(matriz,ordem,valor):
  cont = 0
  for i in range(ordem):
    for j in range(ordem):
      if valor % matriz[i][j] == 0:
        cont = cont + 1
  return cont



m = []
n = int(input('digite a ordem da matriz: '))

criação(m,n)
leitura(m,n)
impressao(m,n)
v = int(input('digite qual valor deseja verificar: '))
verificar(m,n,v)
print('Há',verificar(m,n,v),'multiplos de',v)