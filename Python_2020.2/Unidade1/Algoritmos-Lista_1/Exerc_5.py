#Fa�a um programa que calcule a convers�o monet�ria de Real para D�lar. O usu�rio informa o valor da cota��o do d�lar (ex.: 3,78) e quanto em real deseja converter (ex. 150,00). O programa exibe quantos d�lares valem os reais informados.

dolar = float(input('qual o valor da cota��o do dolar:'))
real = float(input('valor que vai ser convertido:'))
valor = dolar*real
print('o valor convertido para dolar sera de:', valor)
