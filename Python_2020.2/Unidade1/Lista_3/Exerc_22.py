#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#1 - 0
#3 - 10
#6 - 15
#9 - 20
#12 - 25
#Exemplo de saída do programa:
#Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
#RS 1.000,00 0 1PARC. RS 1.000,00
#RS 1.100,00 100 3PARC. RS 366,00
#RS 1.150,00 150 6PARC. RS 191,67

for i in range(3,12+1,3):
  divida = float(input('informe o valor da divida: '))
  parcelas = i
  juros = divida % 1000
  d = divida / parcelas
  print('parcelas:',parcelas,', juros:',juros,', valor da parcela:',d) 
