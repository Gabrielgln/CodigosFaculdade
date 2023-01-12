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
#Q6 - 
  def ordenar(self):
    aux = 0
    tam = self.__len__()
    for i in range(tam):
      for j in range(tam):
        if self[i] < self[j]:
          aux = self[i]
          self[i] = self[j]
          self[j] = aux

  def verificar_igual(self,index):
    tam = self.__len__()
    for i in range(tam):
      if index == self[i]:
        return True
    return False    

  def juntar_listas(self,lista2):
    lista3 = Computador()
    tam_lista1 = self.__len__()
    tam_lista2 = lista2.__len__()

    for i in range(tam_lista1):
      lista3.append(self[i])

    for i in range(tam_lista2):
      if not self.verificar_igual(lista2[i]):
        lista3.append(lista2[i])

    lista3.ordenar()
    return lista3
   
computador1 = Computador()
computador1.append(1)
computador1.append(10)
computador1.append(55)
computador1.append(5)
print(computador1)
computador2 = Computador()
computador2.append(1)
computador2.append(4)
computador2.append(2)
print(computador2)
print(computador1.juntar_listas(computador2))

  #def append(self,value):
   # if self.head:
    #  aux = self.head
        #while aux.next:
          #aux = aux.next
        #self.head = Node(value)
      #aux = Node(value)
    #self.__size += 1

