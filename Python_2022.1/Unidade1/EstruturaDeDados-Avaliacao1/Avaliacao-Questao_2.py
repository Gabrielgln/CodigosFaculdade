#class Gincana:
#def __init__(self):
#vencedores = [5,7,2,5,9,1,7,5,3,8,0]

#Essa classe será usada para fazer um programa para controlar os vencedores das provas da gincana de um colégio. Cada vez que uma prova é realizada, a equipe vencedora da prova tem seu identificador (um número inteiro entre 0 e 9) armazenado em um vetor de vencedores. Acrescente à classe um método que retorne a quantidade de provas vencidas pela equipe vencedora (4,0 pontos).

def num_vitoria_vencedor(self):
  num_vitorias = [0] * 10
  for i in range(len(self.vencedores)): #tam da lista de vencedores
    num_vitorias[ self.vencedores[i] ] += 1 #num_vitoria recebe num_vitorias + 1
  return max(num_vitorias) #MAX pega o contador com mais num_vitorias