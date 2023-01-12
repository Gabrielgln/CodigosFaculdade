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

#Q2 - Faça uma função que receba uma lista encadeada e a divida em duas listas, cada uma com metade dos elementos. Caso haja uma quantidade ímpar de elementos, a primeira lista retornada deve conter um elemento a mais.  

  def dividir_lista(lista):
    tam_lista = lista.__len__()#função para ler lista
    tam = (tam_lista/2)
    nova_lista1 = []
    nova_lista2 = []
    if tam_lista % 2 == 0:#se a lista for par
      for i in range(0,int(tam)):#começa de 0 ate metade da lista
        nova_lista1.append(lista.__getitem__(i))#get pega o indice da lista
      for i in range(int(tam),tam_lista): #da metade da lista até o tamanho final da lista
        nova_lista2.append(lista.__getitem__(i))
    else: # se não for par
      for i in range(0,int(tam+1)):#começa de 0 até a metade da lista + 1
        nova_lista1.append(lista.__getitem__(i))
      for i in range(int(tam+1),tam_lista):#começa da metade da lista+1 até o tamanho final da lista
        nova_lista2.append(lista.__getitem__(i))
    print(nova_lista1)
    print(nova_lista2)
        
computador1 = Computador()
computador1.append(100)
computador1.append(10)
computador1.append(10)
computador1.append(5)
computador1.append(50)
computador1.append(55)
print(computador1)
computador1.dividir_lista()
