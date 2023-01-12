def rotate_word(palavra,valor):
  word_rot = '' #string vazia
  for letra in palavra:
    letra_tmp = ord(letra) + valor
    if letra_tmp > ord('z'): #transforma o valor do 'z' em num
      letra_tmp -= 26 #letra_tmp = letra_tmp - 26
    elif letra_tmp < ord('a'):#transforma o valor do 'a' em num
      letra_tmp += 26 #letra_tmp = letra_tmp + 26
    word_rot += chr(letra_tmp) #transforma o valor em string
  return word_rot

def gerar_dicionario(endereco):
  arquivo = open(endereco,'r')#para abrir um arquivo importado
  l = arquivo.read().lower()#read = lear , lower = transforma em minusculo
  lista = l.split() #separa por palavras
  dicionario = {}#criar um dicionario
  #print(lista)
  for palavra in lista:#para cada palavra na lista = 
    dicionario[palavra] = None#cada chave de palavra recebe valor None
  #print(dicionario)
  return dicionario

def verificar_palavra(palavra,dicionario):
  for i in range(1,14): # metade do alfabeto
    palavra_rot = rotate_word(palavra,i)#verificar a palavra
    if palavra_rot in dicionario:#se tiver a palavra_rot no dicionario
      print(palavra,i,palavra_rot)
  
dicionario = gerar_dicionario('words.txt')
for palavra in dicionario.keys():
  verificar_palavra(palavra,dicionario)