#Fa�a um programa que pe�a dois n�meros, base e expoente, calcule e mostre o primeiro n�mero elevado ao segundo n�mero. N�o utilize a fun��o de pot�ncia da linguagem.

#resultado = base ** expoente
base = int(input('Base: '))
expoente = int(input('Expoente: '))
resultado = 1
for i in range(expoente):
  resultado = resultado * base
print(base,'elevado a',expoente,'� igual a',resultado)
