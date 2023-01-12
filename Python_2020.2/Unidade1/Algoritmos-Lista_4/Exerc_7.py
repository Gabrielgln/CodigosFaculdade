#questão 7

#Um programa que desenhe um triângulo retângulo com a base voltada para baixo, como a seguir: 

ch = input("Caractere: ")
for linha in range(8):
    for coluna in range(8):
        if linha >= coluna:
            print(ch, sep = '', end = '')
        else:
            print(' ', sep = '', end = '')
    print()