#Crie um programa que pergunta o nome do usu�rio e o ano de nascimento do usu�rio e calcula qual idade ele tem (ou ter�, se ainda n�o fez anivers�rio neste ano). Ex.: Nome = Carlos, Ano = 1999. O programa mostra a mensagem: �Carlos tem 20 anos�.

nome = str(input('qual seu nome:'))
nasceu = float(input('qual ano voc� nasceu:'))
idade = 2021 - nasceu
print('sua idade �:', idade)
