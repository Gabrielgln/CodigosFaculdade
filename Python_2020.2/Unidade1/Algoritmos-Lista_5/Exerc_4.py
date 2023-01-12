#4 - Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.

vetor = []
q = 0
for i in range(10):
  num = int(input('digite um numero infeliz: '))
  if num % 2 == 0:
    vetor.append(num)
    q = q + 1
print('o valores pares são: ',vetor,'no total de:',q,'numeros pares') 