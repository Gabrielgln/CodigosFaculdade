class Pilha():
  def __init__(self):
    self.data = [] # para criar um pilha

  def append(self,valor):
    self.data.append(valor) #adiciona no ultimo da pilha

  def pop(self):
    return self.data.pop() #remove e retorna o ultimo da pilha

  def isEmpty(self):
    return len(self.data) == 0

def validar(expressao):
  p = Pilha()  
  for i in expressao:
    if i == '(':
      p.append(i)
    elif i == ')':
      if p.isEmpty():
        return False
      p.pop()
  return p.isEmpty

p = Pilha()
palavra = "uepb"
p_invertido = '' #variavel string nula
for i in palavra: #i=u, i=e, i=p, i=b
  p.append(i) #pilha recebe cada elemento
for i in range(len(palavra)):
  p_invertido = p_invertido + p.pop() #pilha recebe o return do ultimo elemento
print(p_invertido)
  

#exp = '()()'
#print(validar(exp))