#Crie um programa que pergunta o nome do usuário e o ano de nascimento do usuário e calcula qual idade ele tem (ou terá, se ainda não fez aniversário neste ano). Ex.: Nome = Carlos, Ano = 1999. O programa mostra a mensagem: “Carlos tem 20 anos”.

nome = str(input('qual seu nome:'))
nasceu = float(input('qual ano você nasceu:'))
idade = 2021 - nasceu
print('sua idade é:', idade)
