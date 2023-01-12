#6 - Leia uma matriz de ordem n, informada pelo usuário. Calcule a soma dos elementos que estão abaixo da diagonal principal.

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
    if j < i:
      soma = soma + m[i][j]
      print(m[i][j])
print('o total da soma do valores a baixo da diagonal principal é')