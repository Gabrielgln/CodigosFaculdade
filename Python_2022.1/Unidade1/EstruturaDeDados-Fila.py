#Apresente uma codificação em Python que simule a fila de um atendimento de um banco. A codificação deve realizar a disponibilização de ficha de atendimento, e realizar o atendimento das pessoas presentes na fila. Utilize o conceito Fila para representar a fila bancária. Os dados das pessoas da fila devem possuir nome, CPF e número da conta bancária.


class fila_banco:
  def __init__(self): #criando a fila
    self.head = []

  def add_cliente(self,valor): #para adicionar na fila
    self.head.append(valor)

  def remove_cliente(self):
    self.head.pop(0) # 0 - para remover da primeira posição

  def verificar_lista(self):#verificar fila
    if (len(self.head) == 0):
      print("Lista vazia!")

  def imprimir(self): #para imprimir fila
    for i in range(len(self.head)):
      print(self.head[i])
  

class Cliente:
  def __init__(self):#construtor vazio
    self.nome = ''
    self.conta = ''
    self.cpf = ''

  def append(self,nome,conta,cpf):#incluir clienta na fila
    self.nome = nome
    self.conta = conta
    self.cpf = cpf

  def __str__(self):
    return ('{' + self.nome + "," + self.conta + ',' + self.cpf+'}') #obrigatorio para imprimir

f = fila_banco()
p1 = Cliente() #primeiro cliente
nome1 = input("Digite o nome da pessoa: ")
conta1 = input("digite o numero da conta: ")
cpf1 = input("digite o cpf da pessoa: ")
p1.append(nome1,conta1,cpf1)
p2 = Cliente() #segundo cliente
nome2 = input("Digite o nome da pessoa: ")
conta2 = input("digite o numero da conta: ")
cpf2 = input("digite o cpf da pessoa: ")
p2.append(nome2,conta2,cpf2)
f.add_cliente(p1)
f.add_cliente(p2)
f.imprimir()
f.remove_cliente()
f.imprimir()


#Apresente uma codificação em Python que realize a inversão dos caracteres de uma palavra informada pelo usuário. Utilize o conceito Pilha

class Pilha:
  def __init__(self):
    self.head = []

  def append(self,valor):
    self.head.append(valor)

  def remove(self):
    return self.head.pop()

pilha = Pilha()
p_invertido = ''
palavra = input("Digite a palavra que deseja inverter: ") #uepb
for i in range(len(palavra)): #lendo a palavra
  pilha.append(palavra[i]) #pilha vai receber cada palavra

for i in range(len(palavra)):
  p_invertido = p_invertido + (pilha.remove())

print(p_invertido)

  


    

  
  