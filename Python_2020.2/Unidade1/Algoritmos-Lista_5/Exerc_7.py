#7 - Ler um vetor de 10 elementos. Crie um segundo vetor, com todos os elementos na ordem inversa, ou seja,
#o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim por diante. Imprima os dois vetores.

vetor = [1,2,3,4,5,6,7,8,9,10]
vetor1 = []
print(vetor)
for i in range(len(vetor)):
  num = vetor.pop()
  vetor1.append(num)
print(vetor1)