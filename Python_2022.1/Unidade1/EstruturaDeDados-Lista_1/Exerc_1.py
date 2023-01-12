class Node:
  def __init__(self, valor):
    self.valor = valor
    self.next = None

class Computador:
  def __init__(self):
    self.head = None
    self.__size = 0

  def append(self,valor):
    if self.head:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = Node(valor)
    else:
      self.head = Node(valor)
    #aumenta +1 no tamanho da lista
    self.__size += 1

  def len(self):
    return self.__size

  def __str__(self):
    output = '['
    aux = self.head
    while aux:
      output += str(aux.valor)
      if aux.next:
        output += ', '
      aux = aux.next
    output += ']'
    return output
#Q1 - Faça uma função para concatenar duas listas encadeadas.
  def concatenar(self,lista2):
    self.append(lista2)
         
computador1 = Computador()
computador1.append(100)
computador1.append(10)
computador1.append(10)
computador1.append(10)
computador1.append(10)
computador1.append(10)
print(computador1)
computador2 = Computador()
computador2.append(5555)
computador2.append(900)
computador1.concatenar(computador2)
print(computador1)


  
  

