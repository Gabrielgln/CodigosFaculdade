#Avaliação - Foi realizada uma pesquisa de algumas características físicas da população de uma certa região,
#a qual coletou os seguintes dados referentes a cada habitante para serem analisados:

# * idade
# * sexo (masculino e feminino)- cor dos olhos (azuis, verdes ou castanhos)- cor dos cabelos
#( louros, castanhos, pretos) Faça um programa que determine e escreva:
# * a maior idade dos habitantes- a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos
#(inclusive) e que tenham olhos verdes e cabelos louros.
#O programa deve encerrar a solicitação de dados dos habitantes quando o valor -1 for fornecido como idade.

q = 0
i = 0
maior = 0
while i != -1:
  i = int(input('informe a idade: '))
  if i == -1:
    print('programa de dados encerrado!')
    break
  cor = int(input('cor do cabelo: digite (1) para (cabelos louros), (2) para (cabelos castanhos) ou (3) para (cabelos pretos): '))
  olhos = int(input('cor dos olhos : digite (1) para (olhos azuis), (2) para (olhos verdes) ou (3) para (olhos castanhos): '))
  s = int(input('qual o sexo? digite (1) para (masculino) ou digite (2) para (feminino): '))
  if s == 2 and i >= 18 and i <= 35 and olhos == 2 and cor == 1:
    q = q + 1
  if i == 0:
    maior = i
  elif i > maior:
    maior = i 
print('a maior idade é',maior)
print('a quantidade de individuos do sexo feminino entre 18-35 com olhos verdes e cabelos louros é: ',q)