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

  def extend(self,lista2):
    if self.head and lista2.head:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = lista2.head #self se junta com lista2
      lista2 = None #lista2 deixa de existir
    else:
      self.head = lista2.head #self se junta com lista2
      lista2 = None #lista2 deixa de existir

  def concatenar(self,lista2):
    self.extend(lista2)
    print(self)

computador1 = Computador()
computador2 = Computador()
computador1.append(7)
computador2.append(8)
computador1.concatenar(computador2)

      