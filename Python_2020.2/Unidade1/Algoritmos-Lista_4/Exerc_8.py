#questão 8

#Um programa que desenhe um triângulo retângulo com a base voltada para cima, como a seguir:

t = 8
ch = input("Caractere: ")
for linha in range(t):
    for coluna in range(t):
        if (linha + coluna) <= t-1:
            print(ch, sep = '', end = '')
        else:
            print('  ', sep = '', end = '')
    print()