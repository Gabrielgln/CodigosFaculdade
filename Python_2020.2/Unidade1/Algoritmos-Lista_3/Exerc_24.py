#Faça um programa que mostre os n termos da Série a seguir:
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

numero = int(input('Digite o número para inverter: '))
numero_invertido = 0

while numero > 0:
  resto = numero % 10
  numero = numero // 10
  numero_invertido = numero_invertido * 10 + resto
print(numero_invertido)
