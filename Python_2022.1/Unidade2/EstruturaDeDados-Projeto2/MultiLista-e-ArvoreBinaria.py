class Node:
  def __init__(self,chave = None):
    self.chave = chave
    self.left = None
    self.right = None

  def gerar_arvore(self,lista,ini,fim):
    meio = (ini+fim) // 2
    self.chave = lista[meio]
    if ini <= meio-1:
      self.left = Node()
      self.left.gerar_arvore(lista,ini,meio-1)
    else:
      self.left = None
    if meio+1 <= fim:
      self.right = Node()
      self.right.gerar_arvore(lista,meio+1,fim)
    else:
      self.right = None

  def imprimir_pos(self):
    if self.left:
      self.left.imprimir_pos()
    if self.right:
      self.right.imprimir_pos()
    if self.chave:
      print(self.chave,end=' ')

  def imprimir_central(self):
    if self.left:
      self.left.imprimir_central()
    if self.chave:
      print(self.chave,end=' ')
    if self.right:
      self.right.imprimir_central()


class Disciplina:
  def __init__(self,nome,nota1,nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2
    
class Aluno:
  def __init__(self,aluno):
    self.aluno = aluno
    self.disciplinas = []
    self.next = None
    
class MultiLista:
  def __init__(self):
    self.head = None

  def append_aluno(self,n_aluno):
    if self.head:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = Aluno(n_aluno)
      print("Aluno cadastrado com sucesso!")
    else:
      self.head = Aluno(n_aluno)
      print("Aluno cadastrado com sucesso!")

  def buscar_aluno(self,n_aluno):
    if self.head:
      aux = self.head
      while aux and not (aux.aluno == n_aluno):
        aux = aux.next
      if aux:
        return aux
      else:
        print("Aluno não existente!")

  def append_disciplina(self,n_aluno,n_disciplina,nota1,nota2):
      aux = self.buscar_aluno(n_aluno)
      if aux:
        aux.disciplinas.append(Disciplina(n_disciplina,nota1,nota2))
        print("Disciplina cadastrada com sucesso!")
      else:
        print("Aluno não registrado. Retorne ao menu e faço o cadastro do aluno.")

  def remove_aluno(self,n_aluno):
      if self.head:
        aux1 = self.head
        aux2 = None
        if aux1.aluno == n_aluno:
          self.head = aux1.next
          del aux1
          print("Aluno removido com sucesso!")
        else:
          while aux1 and not (aux1.aluno == n_aluno):
            aux2 = aux1
            aux1 = aux1.next
          aux2.next = aux1.next
          del aux1
          print("Aluno removido com sucesso!")
      
  def remove_disciplina(self,n_aluno,n_disciplina):
    aux = self.buscar_aluno(n_aluno)
    for i in range(len(aux.disciplinas)):
      if aux.disciplinas[i].nome == n_disciplina:
        aux.disciplinas.pop(i)
        print("Disciplina removida com sucesso!")

  def remover_nota(self,n_aluno,n_disciplina):
    aux = self.buscar_aluno(n_aluno)
    for i in range(len(aux.disciplinas)):
      if aux.disciplinas[i].nome == n_disciplina:
        op = int(input("Qual nota que deseja excluir?\n1 - Nota1\n2 - Nota2\n"))
        if op == 1:
          aux1 = aux.disciplinas[i].nota1
          aux.disciplinas[i].nota1 = None
          del aux1
          print("Primeira nota removida com sucesso!")
        else:
          aux2 = aux.disciplinas[i].nota2
          aux.disciplinas[i].nota2 = None
          del aux2
          print("Segunda nota removida com sucesso!")

  def atualizar_aluno(self,n_aluno,n_aluno_atualizado):
      if self.head:
        aux = self.head
        while aux and not(aux.aluno == n_aluno):
          aux = aux.next
        aux.aluno = n_aluno_atualizado

  def atualizar_disciplina(self,n_aluno,n_disciplina,n_disciplina_atualizado):
    if self.head:
      aux = self.buscar_aluno(n_aluno)
      for i in range(len(aux.disciplinas)):
        if aux.disciplinas[i].nome == n_disciplina:
          aux.disciplinas[i].nome = n_disciplina_atualizado
        else:
          print("Disciplina não encontrada.")

  def atualizar_nota(self,n_aluno,n_disciplina):
    if self.head:
      aux = self.buscar_aluno(n_aluno)
      for i in range(len(aux.disciplinas)):
        if aux.disciplinas[i].nome == n_disciplina:
          op = int(input("Qual nota que deseja atualizar?\n1 - Nota1\n2 - Nota2:\n"))
          if op == 1:
            nota1 = int(input("Digite a nota atualizada: "))
            aux.disciplinas[i].nota1 = nota1
          else:
            nota2 = int(input("Digite a nota atualizada: "))
            aux.disciplinas[i].nota2 = nota2
          print("Notas atualizadas com sucesso!")

  def visualizar_alunos_aprovados(self,n_aluno):
    if self.head:
      aux = self.buscar_aluno(n_aluno)
      print("--------------------")
      print('{',aux.aluno,'}',"- Disciplinas com média maior que 7:")
      for i in range(len(aux.disciplinas)):
        if aux.disciplinas[i].nota1 and aux.disciplinas[i].nota2:
          if (aux.disciplinas[i].nota1 + aux.disciplinas[i].nota2) / 2 >= 7:
            print(aux.disciplinas[i].nome)
        else:
          print("Aluno não possui disciplinas com media de aprovação")

  def visualizar_alunos_reprovados(self,n_aluno):
    if self.head:
      aux = self.buscar_aluno(n_aluno)
      print("--------------------")
      print('{',aux.aluno,'}',"- Disciplinas com média menor que 7:")
      for i in range(len(aux.disciplinas)):
        if aux.disciplinas[i].nota1 and aux.disciplinas[i].nota2:
          if (aux.disciplinas[i].nota1 + aux.disciplinas[i].nota2) / 2 < 7:
            print(aux.disciplinas[i].nome)
        else:
          print("Aluno não possui disciplinas com media de reprovação")

  def visualizar_media(self,n_aluno,n_disciplina):
    if self.head:
      aux = self.buscar_aluno(n_aluno)
      for i in range(len(aux.disciplinas)):
        if aux.disciplinas[i].nome == n_disciplina:
          if aux.disciplinas[i].nota1 and aux.disciplinas[i].nota2:
            print("--------------------")
            print('{',aux.aluno,'}')
            print(aux.disciplinas[i].nome,"-",(aux.disciplinas[i].nota1 + aux.disciplinas[i].nota2) / 2)
          else:
            print("Aluno informado possui apenas 1 ou nenhuma nota na disciplina!")

  def gerar_lista(self):
    l = []
    if self.head:
      aux = self.head
      while aux:
        l.append(aux.aluno)
        aux = aux.next
    return l

  def imprimir_crescente(self):
    vetor = self.gerar_lista()
    if vetor:
      vetor.sort()
      return vetor
    else:
      return 0

  def relatorio_notas(self,n_aluno):
    if self.head:
      aux = self.head
      while aux and not aux.aluno == n_aluno:
        aux = aux.next
      print("--------------------")
      print('{',aux.aluno,'}')
      for i in aux.disciplinas:
        print(i.nome,'-',i.nota1,'-',i.nota2)
    else:
      print("Não existem alunos cadastrados!")

uni = MultiLista()
tree = Node()

user = -1
while user != 0:
  print("\n----------MENU----------")
  print("1 - Cadastrar aluno\n2 - Cadastrar disciplina em aluno\n3 - Remover aluno\n4 - Remover disciplina de aluno\n5 - Remover nota de disciplina de aluno\n6 - Atualizar aluno\n7 - Atualizar disciplina de aluno\n8 - Atualizar nota de disciplina de aluno\n9 - Visualizar a média do aluno em uma disciplina\n10 - Visualizar os nomes dos alunos em ordem alfabética\n11 - Visualizar os nomes dos alunos que estão com média menor que 7\n12 - Visualizar os nomes dos alunos que estão com média maior ou igual a 7\n13 - Visualizar as notas das disciplinas cadastradas em um aluno\n0 -  Sair.\n")
  user = int(input("Digite a sua opção: \n"))
  if user == 1:
    print("------Cadastrar Aluno------\n")
    n_aluno = input("Digite o nome do aluno: ")
    uni.append_aluno(n_aluno)

  elif user == 2:
    print("---Cadastrar disciplina e notas da disciplina---\n")
    n_aluno = input("Digite o nome do aluno: ")
    n_disciplina = input("Informe a disciplina que deseja cadastrar: \n")
    nota1 = float(input("Informe a primeira nota do aluno: "))
    nota2 = float(input("Informe a segunda nota do aluno: \n"))
    uni.append_disciplina(n_aluno,n_disciplina,nota1,nota2)

  elif user == 3:
    print("------Remover Aluno------\n")
    n_aluno = input("Informe o aluno que deseja remover: \n")
    uni.remove_aluno(n_aluno)

  elif user == 4:
    print("------Remover Disciplina-------\n")
    n_aluno = input("Digite o nome do aluno que deseja remover a disciplina: ")
    n_disciplina = input("Digite a disciplina do aluno que irá ser removido: ")
    uni.remove_disciplina(n_aluno,n_disciplina)

  elif user == 5:
    print("----Remover nota de disciplina de aluno----\n")
    n_aluno = input("Digite o nome do aluno que deseja remover a nota: ") 
    n_disciplina = input("Informe a disciplina que deseja remover a nota: \n")
    uni.remover_nota(n_aluno,n_disciplina)

  elif user == 6:
    print("------Atualizar Aluno-------\n")
    n_aluno = input("Informe o aluno que deseja atulizar: ")
    n_aluno_atualizado = input("Informe o nome do aluno atualizado: \n")
    uni.atualizar_aluno(n_aluno,n_aluno_atualizado)

  elif user == 7:
    print("-------Atualizar Disciplina---------\n")
    n_aluno = input("Informe o nome do aluno que deseja atualizar: ")
    n_disciplina = input("Informe a disciplina do que o aluno está matriculado: ")
    n_disciplina_atualizado = input("Digite o nome atualizado da disciplina: ")
    uni.atualizar_disciplina(n_aluno, n_disciplina,n_disciplina_atualizado)

  elif user == 8:
    print("-------Atualizar nota do Aluno-------\n")
    n_aluno = input("Informe o aluno que deseja  atualizar as notas: ")
    n_disciplina = input("Informe a disciplina do aluno: ")
    uni.atualizar_nota(n_aluno,n_disciplina)

  elif user == 9:
    print("-----Visualizar média do aluno em uma disciplina------\n")
    n_aluno = input("Informe o nome do aluno: ")
    n_disciplina = input("Informe a disciplina do aluno: ")
    uni.visualizar_media(n_aluno,n_disciplina)

  elif user == 10:
    print("-----Visualizar os nomes dos alunos em ordem alfabética na arvore-----\n")
    lista_alunos = uni.imprimir_crescente()
    if lista_alunos == 0:
      print("Não existem alunos cadastrados na arvore!")
    else:
      tree.gerar_arvore(lista_alunos,0,len(lista_alunos)-1)
      tree.imprimir_central()
      print()

  elif user == 11:
    print("---Visualizar os nomes dos alunos que estão com média menor que 7---\n")
    n_aluno = input("Informe o aluno para verificar as médias das disciplinas: ")
    uni.visualizar_alunos_reprovados(n_aluno)

  elif user == 12:
    print("---Visualizar os nomes dos alunos que estão com média maior que 7---\n")
    n_aluno = input("Informe o aluno para verificar as médias das disciplinas: ")
    uni.visualizar_alunos_aprovados(n_aluno)

  elif user == 13:
    print("------Visualizar as notas das disciplinas do aluno-------\n")
    n_aluno = input("Informe o aluno para verificar as notas das disciplinas: ")
    uni.relatorio_notas(n_aluno)

  elif user > 13:
    print("Essa opção não está disponível. Retorne ao MENU.\n")