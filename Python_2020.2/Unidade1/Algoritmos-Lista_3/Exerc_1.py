#Fa�a um programa que pe�a uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inv�lido e continue pedindo at� que o usu�rio informe um valor v�lido.

nota = float(input('Digite uma nota entre 0 e 10: '))
while nota > 10 or nota < 0:
  nota = float(input('Nota inv�lida, digite outra vez: '))
print('A nota digitada foi',nota)
