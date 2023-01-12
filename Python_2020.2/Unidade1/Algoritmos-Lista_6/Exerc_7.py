#7 - Leia uma matriz de ordem n, informada pelo usuário. Calcule a soma dos elementos que estão na diagonal secundária.

ordem = int(input('digite a ordem da matriz: '))
m = []
for i in range(ordem):
  m.append([0] * ordem)

for i in range(ordem):
  for j in range(ordem):
    print('\nM = [',i+1,',',j+1,'] : ',end='')
    m[i][j] = int(input())

for i in range(ordem):
  for j in range(ordem):
    print(m[i][j],end=' ')
  print()
soma = 0
for i in range(ordem):
  for j in range(ordem):
    if i + j == ordem-1:
      soma = soma + m[i][j]
      print(m[i][j])
print('a soma dos valores da diagonal secundaria é: ',soma) 