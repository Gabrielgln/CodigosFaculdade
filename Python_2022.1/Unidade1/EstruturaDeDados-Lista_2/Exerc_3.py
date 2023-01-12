#apresente uma codificação em python que simule o cadastro, pesquisa e remoção de produtos em um sistema de armazenamento de produtos de um supermercado. utilize o conceito de dicionario para representar os produtos. os produtos devem ter: nome e valor

dicionario = {}
produto = input('Adicionar produto: ')
dicionario[produto] = int(input('digite o valor do produto: '))
produto = input('Adicionar produto: ')
dicionario[produto] = int(input('digite o valor do produto: '))
produto = input('Adicionar produto: ')
dicionario[produto] = int(input('digite o valor do produto: '))
print(dicionario)
pesquisa_produto = input('digite o produto que está pesquisando: ')
print(dicionario[pesquisa_produto])
remove_produto = input('digite o produto que deseja remover: ')
dicionario.pop(remove_produto)
print(dicionario)