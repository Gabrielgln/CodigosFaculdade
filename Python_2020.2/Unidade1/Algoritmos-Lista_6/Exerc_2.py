#2 - Leia uma matriz 3 x 4. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e,
#ao final, escrever a localização (linha e coluna) ou uma mensagem de “não encontrado”.

nlinhas = 3
ncolunas = 4

m = []
for i in range(nlinhas):
  m.append([0] * ncolunas)

for i in range(nlinhas):
  for j in range(ncolunas):
    print('m[',i+1,',',j+1,']: ',sep='',end='')
    m[i][j] = int(input())

for i in range(nlinhas):
  for j in range(ncolunas):
    print(m[i][j],end=' ')
  print()

x = int(input('Que valor deseja encontrar? '))

encontrou = False
for i in range(nlinhas):
  for j in range(ncolunas):
    if m[i][j] == x:
      print('Aparece na linha',i+1,'e na coluna',j+1)
      encontrou = True
if not encontrou:
  print('Não encontrado.')