# 1 - apresente uma codificação em python que apresente todos os graus dos nos de uma arvore

# 2 - apresente uma codificação em python que apresente e contabilize todos os nos folhas de uma arvore

class Tree:
  def __init__(self, chave=None):
    self.chave = chave
    self.left = None
    self.right = None
    

  def insert(self, value):
    if not self.chave:
      self.chave = value
    elif value < self.chave:
      # ir para esquerda
      if self.left:
        self.left.insert(value)
      else:
        self.left = Tree(value)
    elif value > self.chave:
      # ir para direita
      if self.right:
        self.right.insert(value)
      else:
        self.right = Tree(value)
#1 
  def verificar_grau(self):
    if self.chave:
      grau = 0
      if self.left:
        grau = grau + 1
        self.left.verificar_grau()
      if self.right:
        grau = grau + 1
        self.right.verificar_grau()
      print("Nó -",self.chave,end='')
      print(" Grau:",grau)
    return "Grau geral da arvore:",grau

  def imprimir_folha(self):
    if not self.chave:
      return 0 
    if self.right == None and self.left == None:
      print("Nós Folha:", self.chave)
    else:
      if self.right:
        self.right.imprimir_folha()
        if self.right == None and self.left == None:
          print(self.data)
      if self.left:
        self.left.imprimir_folha()
    
#2
def verificar_folha(tree):
  if not tree:
    return 0
  elif not tree.left and not tree.right:
    return 1
  else:
    esq = verificar_folha(tree.left)
    dir = verificar_folha(tree.right)
  return esq + dir
 
tree = Tree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(10)
tree.insert(2)
tree.insert(3)
tree.insert(40)
tree.insert(30)

tree.verificar_grau()
print()
print("Quantidade de Nós folha:",verificar_folha(tree))
print()
tree.imprimir_folha()

