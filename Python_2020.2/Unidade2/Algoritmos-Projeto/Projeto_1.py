#Projeto 1 - Vamos construir um sistema de recomendações rudimentar. Um sistema de recomendações é a aplicação que fornece
#indicações de conteúdo para ser consumido em um serviço online, como por exemplo,streaming de filmes, músicas,
#vídeos em geral.

#Para nosso sistema de recomendações, vamos considerar justamente um serviço de streaming de filmes temos
#a seguinte sequência de passos:

#1- Solicitar a inclusão de um total de 10 filmes (no papel de operador do serviço);

#2- Exibir os filmes ao usuário 1 e perguntar se ele assistiu cada um (no papel de usuário 1);

#3- Exibir os filmes ao usuário 2 e perguntar se ele assistiu cada um (no papel de usuário 2);

#4- Mostrar recomendações para o usuário 1: aqueles filmes que ele não assistiu, mas foram assistidos pelo usuário 2.

#5- Mostrar recomendações para o usuário 2: aqueles filmes que ele não assistiu, mas foram assistidos pelo usuário 1.

#Para estruturar as informações, usaremos:

#Lista de strings contendo os nomes dos filmes;

#Lista de booleanos contendo os filmes assistidos pelo usuário 1;

#Lista de booleanos contendo os filmes assistidos pelo usuário 2;

filmes = ['Homen Aranha','Flash','Homen de Ferro','Thor','Hulk','Mulher Maravilha','Barraca do beijo','João e o pé de feijão','Shrek','Projeto X']
usuario1 = []
usuario2 = []
r1 = []
r2 = []
print("User1 já assistiu esses filmes?: ")
for i in range(10):
  print(filmes[i],"\ndigite 1 para (sim) ou digite 2 para (não): ")
  filme1 = int(input())
  if filme1 == 1:
    usuario1.append(filmes[i])
#troca de usuario 1 para usuario2
print()
print("User2 já assistiu esses filmes?: ")
for i in range(10):
  print(filmes[i],"\ndigite 1 para (sim) ou digite 2 para (não): ")
  f1 = int(input())
  if f1 == 1:
    usuario2.append(filmes[i])

r1 = [x for x in usuario2 if x not in usuario1]
print("Os filmes que o User-2 recomendou para o User-1 foram: \n",r1)
r2 = [x for x in usuario1 if x not in usuario2]
print("Os filmes que o User-1 recomendou para o User-2 foram: \n",r2)

