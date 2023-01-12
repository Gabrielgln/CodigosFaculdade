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

  def verificar_repeticao(self):
    if self.head:
      dicionario = {}
      vetor1 = []
      vetor2 = []
      tam = self.__len__()
      for i in range(tam):
        dicionario[self[i]] = dicionario.get(self[i],0)+1
      
      for chave,valor in dicionario.items():
        if valor > 1: #se valor repitiu mais de uma vez
          vetor1.append(chave)
          vetor2.append(valor)
          
      print("Valor:",vetor1,":",vetor2)  
        
            
          
    else:
      raise IndexError("Lista vazia!!!")

computador1 = Computador()
computador1.append(6)    
computador1.append(5)
computador1.append(1)
computador1.append(50)
computador1.append(1)
computador1.append(1)
computador1.verificar_repeticao()