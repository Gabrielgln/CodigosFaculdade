class Node:
  def __init__(self,chave = None):
    self.chave = chave
    self.left = None
    self.right = None

  def insert(self,value):
    if not self.chave:
      self.chave = value
      #print("dale")
    if value < self.chave:
      if self.left:
        self.left.insert(value)
      else:
        self.left = Node(value)
        #print("valor adicionado com sucesso 1 !")
    elif value > self.chave:
      if self.right:
        self.right.insert(value)
      else:
        self.right = Node(value)
        #print("valor adicionado com sucesso 2 !")

  def imprimir_pre(self):
      if self.chave:
        print(self.chave,end='-') #imprimi no começo!
      if self.left:
        self.left.imprimir_pre()
      if self.right:
        self.right.imprimir_pre()


  #inverter os dados da lista
  def inverter_arvore(self):
    if self.chave:
      if self.left and self.right:
        aux = self.left
        self.left = self.right
        self.right = aux


tree = Node()
tree.insert(5)
tree.insert(2)
tree.insert(3)
tree.insert(8)
tree.insert(7)
tree.insert(9)
tree.imprimir_pre()
tree.inverter_arvore()
print()
tree.imprimir_pre()