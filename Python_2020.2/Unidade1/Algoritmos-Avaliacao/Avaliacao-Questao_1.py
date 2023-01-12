#Avaliação - Faça um programa que verifica os lados digitados pelo o usuário e faça a medida desses lados com base no valor digitado
#e retorne ao usuário a medida exata e qual figura geométrica é equivalente aos lados digitados:

lados = float(input('quantos lados?'))
medida = float(input('qual a medida dos lados?'))
if lados == 3:
  area = (medida * medida) / 2
  print('triangulo',area,'cm²')

elif lados == 4:
  area = medida * medida
  print('quadrado',area,'cm²')

elif lados == 5:
  print('pentágono')

elif lados < 3:
  print('não é um polígono')

elif lados > 5:
  print('polígono não identificado')