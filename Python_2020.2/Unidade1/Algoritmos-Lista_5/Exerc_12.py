#12 - Faça um programa no qual o usuário forneça valores para um vetor. A digitação é encerrada com um valor negativo.
#Na sequência o usuário deve fornecer dois valores. Procure por ocorrências do primeiro valor no vetor,
#e substitua por ocorrências do segundo valor.

lista = []
valor = int(input('digite um valor: '))
while valor > 0:
  valor = int(input('digite um valor: '))
  lista.append(valor)
  if valor < 0:
    lista.pop()


valor1 = int(input('digite o primeiro valor a ser analisado: '))
valor2 = int(input('digite o segundo valor a ser analisado: '))
for i in range(lista.count(valor1)):
  lista.remove(valor1)
  lista.append(valor2)
print(lista)  
