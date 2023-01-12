class Aluno:
  def __init__(self,nome,cidade):
    self.nome = nome
    self.cidade = cidade

class Curso:
  def __init__(self,nome,turno):
    self.nome = nome
    self.turno = turno
    self.alunos = []
    self.next = None

class Multi_lista:
  def __init__(self):
    self.head = None

  def cadastrar_curso(self,nome,turno):
    if self.head:
      aux = self.head
      while aux.next:#enquanto tiver elemento no proximo
        aux = aux.next# aux vai para o proximo
      aux.next = Curso(nome,turno)
    else:
      self.head = Curso(nome,turno)

  def buscar_curso(self,nome_curso,turno_curso):
    aux = self.head
    while aux and not(aux.nome == nome_curso and aux.turno == turno_curso):
      #enquanto tiver elemento e não for igual a nome e turno
      aux = aux.next # aux vai para o proximo
    if aux == None:
      return aux
    else:
      return aux

  def cadastrar_aluno(self,nome,cidade,nome_curso,turno_curso):
    aux = self.buscar_curso(nome_curso,turno_curso)
    if aux:
      aux.alunos.append(Aluno(nome,cidade))
    else:
      print("Curso inexistente")

  def relatorio(self):
    aux = self.head
    while aux:
      print("{",aux.nome,"-",aux.turno,"}")
      for i in aux.alunos:
        print(i.nome,'-',i.cidade)
      aux = aux.next

uepb = Multi_lista()
uepb.cadastrar_curso("matematica","manhã")
uepb.cadastrar_aluno("gabriel","patos","matematica","manhã")
uepb.relatorio()