#Um posto est� vendendo combust�veis com a seguinte tabela de descontos: �lcool:
#at� 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#at� 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro
#Escreva um algoritmo que leia o n�mero de litros vendidos, o tipo de combust�vel (codificado da seguinte forma: A-�lcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o pre�o do litro da gasolina � R4,50opre�odolitrodo�lcool�R 3,40.

lv = float(input('quantos litros?'))
a = lv
A = lv * 3.40
if lv <= 20:
  a = A * 0.03
elif lv > 20:
  a = A * 0.05
print('desconto de', a)

g = lv
G = lv * 4.50
