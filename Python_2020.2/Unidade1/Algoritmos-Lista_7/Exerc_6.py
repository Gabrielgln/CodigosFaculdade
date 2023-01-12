#6 - Faça um programa que leia dois vetores e gere um terceiro vetor sendo a concatenação dos dois primeiros.
#Não use a concatenação de listas do Python.

def ler_vetor(vetor,tamanho):
  for i in range(tamanho):
    print('Elemento',i+1,':')
    vetor[i] = int(input())

#vetor1 = [4,6,8,2]
#vetor2 = [5,3,9,7,8]
#vetor3 = [4,6,8,2,5,3,9,7,8]
def concatenar_vetores(vetor3,vetor1,vetor2,tam1,tam2):
  for i in range(tam1):
    vetor3[i] = vetor1[i]
  for i in range(tam2):
    vetor3[tam1+i] = vetor2[i]

tam1 = int(input('Tamanho do primeiro vetor: '))
vet1 = [0] * tam1
print('Vetor 1:')
ler_vetor(vet1,tam1)

tam2 = int(input('Tamanho do segundo vetor: '))
vet2 = [0] * tam2
print('Vetor 2:')
ler_vetor(vet2,tam2)

vet3 = [0] * (tam1 + tam2)
concatenar_vetores(vet3,vet1,vet2,tam1,tam2)
print('Vetor 1:',vet1)
print('Vetor 2:',vet2)
print('Vetor concatenado:',vet3)