#Fa�a um programa que leia 10 n�meros e informe a soma e a m�dia dos n�meros.

soma = 0
cont = 0
for i in range(1,11):
  soma = soma + valor
  cont = cont + 1
  valor = int(input('digite um numero'))
media = soma // cont
print('o valor da media dos numeros �:',media)
