#Supondo que a popula��o de um pa�s A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a popula��o de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Fa�a um programa que calcule e escreva o n�mero de anos necess�rios para que a popula��o do pa�s A ultrapasse ou iguale a popula��o do pa�s B, mantidas as taxas de crescimento.

A = 80000
taxaA = 0.03
B = 200000
taxaB = 0.015
anos = 0

while A < B:
  A = A + A * taxaA
  B = B + B * taxaB
  anos = anos + 1
print('S�o necess�rios',anos,'anos para que o pa�s A ultrapasse o pa�s B.')
