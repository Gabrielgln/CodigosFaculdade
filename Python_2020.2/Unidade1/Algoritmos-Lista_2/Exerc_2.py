#Fa�a um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a m�dia alcan�ada por aluno e apresentar:
#A mensagem "Aprovado", se a m�dia alcan�ada for maior ou igual a sete;
#A mensagem �Prova Final�, se a m�dia alcan�ada estiver entre quatro e sete;
#A mensagem "Reprovado", se a m�dia for menor do que quatro.

nota1 = float(input('digite sua nota1:'))
nota2 = float(input('digite sua nota2:'))
media = (nota1 + nota2) / 2

if media >= 7:
  print('aprovado')
elif media >=4: 
  print('prova final')
else:
  print('reprovado')  
