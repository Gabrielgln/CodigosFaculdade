#4 - Dado um vetor, de tamanho N, de valores inteiros, verifique se os elementos nele contidos
#encontram-se em ordem crescente.

def crescente(lista,tamanho):
  for i in range(tamanho-1):
    if lista[i] > lista[i+1]:
      return False
  return True


def lista(lista,tamanho):
  for i in range(tamanho):
    print('valor',i+1,':')
    vetor[i] = int(input())

n = int(input('digite a quantidade de itens do vetor: '))
vetor = [0] * n
lista(vetor,n)
print(vetor)
if crescente(vetor,n):
  print('os números estão em ordem crescente!')
else:
  print('os números NÃO estão em ordem crescente!')
