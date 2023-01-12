class Funcionario:
  def __init__(self,nome,salario):
    self.nome = nome
    self.salario = salario
  
class Hash:
  def __init__(self,tam):
    self.tam = tam
    self.lista = [0] * self.tam
    for i in range(self.tam):
      self.lista[i] = [] #em cada posição da lista cria outra lista
      
 
  def insert(self,funcionario):
    #saber a posição pela primeira letra do nome do funcionario pelo resto da divisão do tamanho da lista
    pos = ord(funcionario.nome[0]) % self.tam
    #adicionando na posição que foi o resultado da ord
    self.lista[pos].append(funcionario)

  def buscar_salario(self,nome):
    pos = ord(nome[0]) % self.tam
    for i in self.lista[pos]:
      if i.nome == nome:
        return i.salario

user = -1
M = 10
hash = Hash(M)
contem = False
while user !=0:
  print("\n--------------------MENU--------------------\n1 - para inserir um funcionário\n2 - para buscar o salario de um funcionário\n0 - para sair")
  user = int(input("Digite: "))
  if user == 1:
    nome = input("Digite o nome do funcionário: ")
    salario = int(input("Digite o salario do funcionário: "))
    f = Funcionario(nome,salario)
    hash.insert(f)
    contem = True
  elif user == 2:
    if contem:
      nome = input("Digite o nome do funcionário: ")
      buscador = hash.buscar_salario(nome)
      if buscador:
        print("O salario de",nome,"é R$: ",buscador)
      else:
        print("Funcionário inexistente!")
    else:
      print("Não tem nenhum funcionário inserido")
  elif user == 0:
    print("Programa encerrado!")
  else:
    print("Digite novamente!")
        

  
#f = Funcionario("gabriel",1000)
#h = Hash(10)
#h.insert(f)
#print(h.buscar_salario("gabriel"))








