class Gincana:
  def __init__(self):
    self.vencedores = [5,7,2,5,9,1,7,5,3,8,0]

  def qte_vitorias(self):
    dicionario = {}

    for campeao in self.vencedores: #campeao == i --> chave
      dicionario[campeao] = dicionario.get(campeao,0)+1 #contator do dicionario

    num_vitorias = 0
    vetor1 = []
    vetor2 = []
    for chave,valor in dicionario.items(): #items = chave e valor
      if num_vitorias < valor:
        num_vitorias = valor
      vetor1.append(chave)
      vetor2.append(valor)
    for i in range(len(vetor1)):
      print(vetor1[i],":",vetor2[i])
    return num_vitorias
   


gincana = Gincana()
gincana.qte_vitorias()
print("O vencedor teve um total de:",gincana.qte_vitorias(),"vitorias!")
      

  
    