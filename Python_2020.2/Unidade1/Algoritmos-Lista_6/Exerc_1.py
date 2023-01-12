#1 - Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.

ordem = 4
matriz = []
for i in range(ordem):
  matriz.append([0] * ordem)

for i in range(ordem):
  for j in range(ordem):
    print('M[',i+1,',',j+1,'] = ',sep='',end='') # M[1,1] = 
    matriz[i][j] = int(input())

print('Matriz informada:')
for i in range(ordem):
  for j in range(ordem):
    print(matriz[i][j],end=' ')
  print()

cont = 0
for i in range(ordem):
  for j in range(ordem):
    if matriz[i][j] > 10:
      cont = cont + 1

print('Há',cont,'elementos maiores que 10 na matriz.')