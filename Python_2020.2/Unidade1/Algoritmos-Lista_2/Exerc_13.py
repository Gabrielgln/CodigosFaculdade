#Um posto está vendendo combustíveis com a seguinte tabela de descontos: Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R4,50opreçodolitrodoálcooléR 3,40.

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
