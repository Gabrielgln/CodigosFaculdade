#questão 6

#Um programa que desenhe a diagonal principal e a diagonal secundária do quadrado, como a seguir:

tam = 8
ch = input("Caractere: ")
for linha in range(tam):
    for coluna in range(tam):
        if linha == coluna or (linha + coluna == tam-1):
            print(ch, ch, sep = '', end = '')
        else:
            print('  ', sep = '', end = '')
    print()