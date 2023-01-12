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

  def insert(self,num,index):
    tam = self.__len__()
    if self.head:
      if index < tam:
        for i in range(index,tam):
          self[i] = num
          break
      else: 
        raise IndexError("Burro!")
    else:
      print('Lista vazia!')
  

computador1 = Computador()
computador1.append(98)
computador1.append(9)
computador1.append(100)
computador1.append(100)
computador1.append(100)
print(computador1)
computador1.insert(4,2)
print(computador1)



          
          
      
      
    