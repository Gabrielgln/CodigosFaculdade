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
        
  def inverter_arvore(self):
    if self.chave:
      if self.left and self.right:
        aux = self.left
        self.left = self.right
        self.right = aux
     
  def imprimir_central(self):
    if self.left:
      self.left.imprimir_central()
    if self.chave:
      print(self.chave,end="-") #imprimi no meio!
    if self.right:
      self.right.imprimir_central()

  def imprimir_pre(self):
    if self.chave:
      print(self.chave,end='-') #imprimi no começo!
    if self.left:
      self.left.imprimir_pre()
    if self.right:
      self.right.imprimir_pre()

  def imprimir_pos(self):
    if self.left:
      self.left.imprimir_pos()
    if self.right:
      self.right.imprimir_pos()
    if self.chave:
      print(self.chave,end='-') #imprimi no fim

  def excluir(self,value):
    if self.chave:
      if self.chave == value:
        if self.left and self.right:
          del self.chave
          self.chave = self.right.excluir(value) #self.chave = self.right
        elif self.left and self.right == None:
          del self.chave
          self.chave = self.left.excluir(value) #self.chave = self.right
        elif self.left == None and self.right:
          del self.chave
          self.chave = self.right.excluir(value) #self.chave = self.right
        elif self.left == None and self.right == None:
          del self.chave
          self.chave = None  
      else:
        if value < self.chave:
          if self.left:    
            self.left.excluir(value)
        if value > self.chave:
          if self.right:
            self.right.excluir(value)
    else:
      print("Valor digitado não pertence a arvore!")

  def excluir_folha(self,value):
    if self.chave == value and self.left == None and self.right == None:
      del self.chave
      self.chave = None
    else:
      if value < self.chave:
        if self.left:
          self.left.excluir_folha(value)
      if value > self.chave:
        if self.right:
          self.right.excluir_folha(value)

  def buscar(self,index):
    if not self.chave:
      return None
    if self.chave == index:
      return index
    if index < self.chave:
      if self.left:
        esq = self.left.buscar(index)
        return esq
    if index > self.chave:
      if self.right:
        dir = self.right.buscar(index)
        return dir
        
tree = Node()
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(8)
tree.insert(7)
#tree.imprimir_pre()
#resultado = buscar(tree,1)
#resultado = tree.buscar(1)
lista = [1,6,7,5,10]
for i in lista:
  resultado = tree.buscar(i)
  if resultado:
    print("Busca pela chave",i,": Sucesso!")
  else:
    print("Busca pela chave",i,": Falha!")
print()
tree.imprimir_pre()
print('\nDepois da exclusão do 5!')
tree.excluir(5)
tree.insert(9)
tree.imprimir_pre()
print('\nDepois da exclusão do 4!')
tree.excluir(4)
tree.imprimir_pre()
print('\nDepois da exclusão do 9!')
tree.excluir(9)
tree.imprimir_pre()
#tree.excluir_folha(1)
#tree.excluir_folha(7)




