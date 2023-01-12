class Node:
  def __init__(self, value):
    self.data = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.__size = 0

  def append(self, value):
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

  def __crescente(self):
    for i in range(self.__size-1):
      if self[i] > self[i+1]:
        return False
    return True

  def __buscaBinariaTemp(self,ini,fim,valor):
    if ini > fim:
      return None
    else:
      meio = (ini + fim) // 2
      if self[meio] == valor:
        return meio
      elif valor < self[meio]:
        return self.__buscaBinariaTemp(ini,meio-1,valor)
      else:
        return self.__buscaBinariaTemp(ini+1,fim,valor)

  def buscaBinaria(self,valor):
    if self.__crescente():
      return self.__buscaBinariaTemp(0,len(self)-1,valor)
    else:
      return None

  def merge(self,lista):
    i = 0
    j = 0
    lm = LinkedList()
    while i < len(self) and j < len(lista):
      if self[i] < lista[j]:
        lm.append(self[i])
        i += 1
      elif self[i] > lista[j]:
        lm.append(lista[j])
        j += 1
      else:
        lm.append(self[i])
        i += 1
        j += 1
    while i < len(self):
      lm.append(self[i])
      i += 1
    while j < len(lista):
      lm.append(lista[j])
      j += 1
    return lm  
      
l = LinkedList()
l.append(100)
l.append(200)
l.append(300)
l.append(400)
l.append(500)
m = LinkedList()
m.append(150)
m.append(180)
m.append(200)
m.append(350)
m.append(400)
m.append(450)
print(l)
print(m)
n = l.merge(m)
#print(len(l))
# print(l[0])
#l[0] = 170
#print(l[0])
print(n)
#pos = l.buscaBinaria(400)
#print(pos)



#lista = []
#lista.append(10)
#print(lista[0])

        