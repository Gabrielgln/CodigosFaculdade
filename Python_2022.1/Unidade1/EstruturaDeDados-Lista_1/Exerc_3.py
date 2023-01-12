class Node:
  def __init__(self, value):
    self.data = value
    self.next = None

class Computador:
  def __init__(self):
    self.head = None
    self.__size = 0

  def append(self,value):
    if self.head:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = Node(value)
    else:
      self.head = Node(value)
    self.__size += 1

  def __len__(self):
    return self.__size

  def __getitem__(self, index):
    if self.head:
      aux = self.head
      for i in range(index):
        if aux.next:
          aux = aux.next
        else:
          raise IndexError('Índice fora da lista.')
      return aux.data
    else:
      raise IndexError('Lista vazia.')

  def __setitem__(self, index, value):
    if self.head:
      aux = self.head
      for i in range(index):
        if aux.next:
          aux = aux.next
        else:
          raise IndexError('Índice fora da lista.')
      aux.data = value
    else:
      raise IndexError('Lista vazia.') 

  def __str__(self):
    output = '['
    aux = self.head
    while aux:
      output += str(aux.data)
      if aux.next:
        output += ', '
      aux = aux.next
    output += ']'
    return output
    
#Q3 - Dadas duas listas, verifique se ambas possuem o mesmo tamanho. Em caso positivo, gere uma terceira lista contendo os elementos das duas listas recebidas intercalados.
    
  def verificar_lista(self,lista2):
    tam1 = self.__len__()#self sempre é a primeira lista
    tam2 = lista2.__len__()#pegando o tamanho da lista 2
    if tam1 == tam2:
      lista3 = []
      for i in range(tam1):
        lista3.append(self[i])#1 - adicionar na lista 3
        lista3.append(lista2[i])#2 - adicionar na lista 3
      print(lista3)
    else:
      print("Listas com tamanhos diferentes!")

computador1 = Computador()
computador1.append(100)
computador1.append(10)
computador1.append(5)
print(computador1)
computador2 = Computador()
computador2.append(5000)
computador2.append(1000)
computador2.append(999)
print(computador2)
computador1.verificar_lista(computador2)