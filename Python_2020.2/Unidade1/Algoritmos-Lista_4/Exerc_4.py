#questão 4

#Um programa que desenhe um quadrado totalmente preenchido, como a seguir:

ch = input("Caractere: ")
for linha in range(8):
    for coluna in range(8):
        print(ch, ch, sep = '', end = '')
    print()