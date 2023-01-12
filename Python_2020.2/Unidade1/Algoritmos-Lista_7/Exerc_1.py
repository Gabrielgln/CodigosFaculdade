#1 - Faça um programa que leia um vetor de inteiros. Imprima separadamente os valores pares
#e os valores ímpares do vetor.

def par_impar(numero):
  for i in range(numero):
    if numero % 2 == 0:
      return True
    else:
      return False

def ler_vetor(lista,tamanho):
  for i in range(tamanho):
    print('teste',i+1,':')
    lista[i] = int(input())


n = int(input('digite o total de valores para teste: '))
vetor = [0] * n
ler_vetor(vetor,n)
print(vetor)
for i in range(n):
  if not par_impar(vetor[i]):
    print(vetor[i],'o valor é impar!')
  else:
    print(vetor[i],'o valor é par!')