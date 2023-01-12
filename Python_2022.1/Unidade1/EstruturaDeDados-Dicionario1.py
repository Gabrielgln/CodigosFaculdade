arquivo = open('scorpions.txt','r') #abrir o arquivo em modo 'r' = leitura
letra = arquivo.read().lower()#read = ler, lower = transformar tudo em minusculo

lista = letra.split()#separar por palavra

ocorrencias = {}#criar um dicionario

for palavra in lista:#para cada palavra na lista
  ocorrencias[palavra] = ocorrencias.get(palavra,0) + 1 #ocorrencia recebe palavra e o valor que começa com 0 e soma +1

#max_ocorrencias = None
#max_palavra = None
#for k,v in ocorrencias.items():
#  if max_ocorrencias == None or v > max_ocorrencias:
#    max_ocorrencias = v
#    max_palavra = k

#print('A palavra',max_palavra,'foi a que mais ocorreu, num total de',max_ocorrencias,'vezes.')

listatmp = [] #criando uma lista temporaria
for k,v in ocorrencias.items():#para cada valor e chave no dicionario
  listatmp.append((v,k))#lista recebe chave e valor
listatmp = sorted(listatmp,reverse=True)#sorted = ordenar a lista , reverse = reverter a lista

num_palavras = 10
for v,k in listatmp[:num_palavras]:#para cada chave e valor na lista até 10
    print(k,v)
  
#listatmp = sorted([(v,k) for k,v in ocorrencias.items()],reverse=True)


