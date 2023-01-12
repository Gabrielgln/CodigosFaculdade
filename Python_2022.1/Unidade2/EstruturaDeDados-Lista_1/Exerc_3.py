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

  def pop_indicador(self,index):
    if index >= self.__len__():
      raise IndexError("Deu pau")
    elif index == 0:
      aux1 = self.head
      self.head = self.head.next
      del aux1
    else:
      aux1 = self.head
      for i in range(index):
        aux2 = aux1
        aux1 = aux1.next
      aux2.next = aux1.next #aux2.next.next
      del aux1
      
  def pop(self):
    if self.head == None:
      raise IndexError("Deu pau")
    elif self.head.next == None:
      del self.head
      self.head = None
    else:
      aux1 = self.head
      while aux1.next:
        aux2 = aux1
        aux1 = aux1.next
      del aux1
      aux2.next = None

computador1 = Computador()
computador1.append(98)
computador1.append(9)
computador1.append(100)
computador1.append(100)
computador1.append(100)
print(computador1)
computador1.pop_indicador(1)
computador1.pop()
print(computador1)