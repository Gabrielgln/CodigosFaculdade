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

#remover o primeiro elemento da lista
  
  def remove(self):
    if (self.head):
      aux = self.head 
      if (aux.next):
        self.head = aux.next 
        aux.next = None 
        del(aux) 
      else: 
        del(self.head)
        self.head = None 

#remover o ultimo elemento da lista
  
  def remove_ultima(self):
    if(self.head):
      aux1 = self.head
      aux2 = None
      while(aux1.next):
        aux2 = aux1
        aux1 = aux1.next
      if(aux2 == None):
        del(self.head)
        self.head = None
      else:
        aux2.next = None
        del(aux1)

#imprimi so os numeros pares da lista
  def imprimir_par(self):
    if self.head:
      aux = self.head
      while aux:
        if aux.data % 2 == 0 :
          print(aux.data)
        aux = aux.next
    else:
      raise IndexError('Lista Vazia')
        
computador1 = Computador()
computador1.append(100)
computador1.append(10)
computador1.append(7)
computador1.append(23)
#print(computador1[0])
print(computador1)
computador1.remove()
print(computador1)
computador1.remove_ultima()
print(computador1)
computador1.imprimir_par()




