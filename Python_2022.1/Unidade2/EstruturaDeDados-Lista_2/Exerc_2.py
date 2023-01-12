class Venda:
  def __init__(self,nome,valor):
    self.nome = nome
    self.valor = valor

class Supermercado:
  def __init__(self,nome_super):
    self.nome_super = nome_super
    self.vendas = []
    self.next = None
    self.valor_geral = 0
    
class MultiLista:
  def __init__(self):
    self.head = None

  def append_supermercado(self,nome_sup):
    if self.head:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = Supermercado(nome_sup)
    else:
      self.head = Supermercado(nome_sup)

  def buscar_supermercado(self,nome_sup):
    aux = self.head
    while aux and not(aux.nome_super == nome_sup):
      aux = aux.next
    return aux

  def append_venda(self,nome_sup,nome_venda,valor_venda):
    aux = self.buscar_supermercado(nome_sup)
    if aux:
      aux.vendas.append(Venda(nome_venda,valor_venda))
      aux.valor_geral = aux.valor_geral + valor_venda
    else:
      print("Supermercado inexistente!")

  def remove_supermercado(self,nome_super):
    if self.head:
      aux1 = self.head
      aux2 = aux1
      while aux1.next and not(aux1.nome_super == nome_super):
        aux2 = aux1
        aux1 = aux1.next
      aux2.next = aux1.next
      del aux1

  def remove_venda(self,nome_sup,nome_venda,valor_venda):
    aux = self.buscar_supermercado(nome_sup)
    for i in range(len(aux.vendas)):
      if aux.vendas[i].nome == nome_venda:
        aux.valor_geral = aux.valor_geral - valor_venda
        aux.vendas.pop(i)

  def relatorio_vendas(self):
    aux = self.head
    while aux:
      print("------------------------------")
      print('{',aux.nome_super,'-','Valor Total =',aux.valor_geral,'}')
      for i in aux.vendas:
        print(i.nome,'-',i.valor)
      aux = aux.next

sup = MultiLista()
sup.append_supermercado("Guedes")
sup.append_venda("Guedes","Gabriel",10)
sup.append_supermercado("Hiper")
sup.append_venda("Hiper","Veronica",10)
sup.relatorio_vendas()
sup.remove_venda("Hiper","Veronica",10)
sup.remove_supermercado("Hiper")
sup.relatorio_vendas()
        
    
  