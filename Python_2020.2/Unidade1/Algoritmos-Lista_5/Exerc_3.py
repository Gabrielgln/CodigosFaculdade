#3 - Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das ´ componentes deste vetor,
#armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.

vetor = []
vetor2 = []
for i in range(10):
  num = float(input('digite um valor: '))
  vetor.append(num)
  vetor2.append(num ** 2)
print(vetor)
print(vetor2)  