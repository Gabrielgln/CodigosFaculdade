#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

quantidade = int(input('quantos valores?' ))
penultimo = 1
ultimo = 1
print(penultimo,ultimo,end=' ')
for i in range(quantidade-2):
  proximo = ultimo + penultimo
  print(proximo,end=' ')
  penultimo = ultimo
  ultimo = proximo
