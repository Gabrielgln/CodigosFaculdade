#Uma fruteira est� vendendo frutas com a seguinte tabela de pre�os: At� 5 Kg Acima de 5 Kg
#Morango RS 2,50 por Kg RS 2,20 por Kg
#Ma�� RS 1,80 por Kg RS 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receber� ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de ma�as adquiridas e escreva o valor a ser pago pelo cliente.

morangos = float(input('Quantidade de morangos (em Kg): '))
macas = float(input('Quantidade de ma��s (em Kg): '))

if morangos <= 5:
  preco_morangos = 2.5 * morangos
else:
  preco_morangos = 2.2 * morangos
if macas <= 5:
  preco_macas = 1.8 * macas
else:
  preco_macas = 1.5 * macas

preco_total = preco_morangos + preco_macas
if morangos + macas > 8 or preco_total > 25:
  preco_total = preco_total - preco_total * 0.1
print('Valor a pagar: R$',preco_total)
