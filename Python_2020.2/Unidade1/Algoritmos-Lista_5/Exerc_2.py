#2 - Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa deve executar os seguintes passos:

#Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7.

#Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre na tela esta soma.

#Modifique a lista na posição 4, atribuindo a esta posição o valor 100.

#Mostre na tela cada valor da lista A, um em cada linha.

vetor = []
lista = []
for i in range(6):
  num = int(input('digite um numero: '))
  vetor.append(num)
  print(vetor)
  if i == 0 or i == 1 or i == 5:
    lista.append(num)
    soma = sum(lista)
vetor.insert(4,100)
print('A sequencia conforme a modificação da posição [4] é: ',vetor)
print('A soma das posições [0], [1], [5] é: ',soma) 