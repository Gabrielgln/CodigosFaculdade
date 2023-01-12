class Cliente:
  def __init__(self,nome,idade):
    self.nome = nome
    self.idade = idade
    self.next = None

class prioritarios:
  def __init__(self):
    self.ini = None
    self.fim = None

  def append(self,nome,idade):
    cliente = Cliente(nome,idade)
    if self.ini == None and cliente.idade > 65:
      self.ini = cliente
    elif self.ini and cliente.idade > 65:
      self.ini.next = cliente
    else:
      if self.fim == None:
        self.fim = cliente
      else:
        aux = self.fim
        self.fim = cliente
        self.fim.next = aux

  def inicio(self):
    if self.ini:
      return (self.ini.nome )

  def fim(self):
    if self.fim:
      return (self.fim.nome )     

fila = prioritarios()
fila.append("gabrie",4)
fila.append("veronica",66)
fila.append("gabriel",77)
print(fila.inicio())
print(fila.fim())

#def inserir_cliente(self, nome, idade):
  #if not self.ini: # fila vazia
    #self.ini = Cliente(nome,idade)
    #self.fim = self.ini
  #elif idade < 65: # cliente jovem
    #self.fim.next = Cliente(nome,idade)
    #self.fim = self.fim.next
  #elif self.ini.idade < 65: # fila só com jovens
    #aux = Cliente(nome,idade)
    #aux.next = self.ini
    #self.ini = aux
  #elif self.fim.idade >= 65: # fila só com idosos
    #self.fim.next = Cliente(nome,idade)
    #self.fim = self.fim.next
  #else: # fila mista
    #aux = self.ini
    #while aux.idade >= 65:
      #anx2 = aux
      #aux1 = aux.next
    #novo = Cliente(nome,idade)
    #aux2.next = novo
    #novo.next = aux
        
        
    
  