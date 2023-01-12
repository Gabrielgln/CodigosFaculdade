class BSTnode:
    def __init__(self, value = None):
        self.data = value
        self.left = None  
        self.right = None

    def insert(self, value):
        if not self.data:
            self.data = value
        elif value < self.data:
            # ir para esquerda
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTnode(value)
        elif value > self.data:
            # ir para direita
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTnode(value)

    def imprimir_pre(self):
        if self.data:
            print(self.data,end=' ')
        if self.left:
            self.left.imprimir_pre() 
        if self.right:
            self.right.imprimir_pre()

    def imprimir_central(self):
        if self.left:
            self.left.imprimir_central()
        if self.data:
            print(self.data,end=' ')
        if self.right:
            self.right.imprimir_central()

    def imprimir_pos(self):
        if self.left:
            self.left.imprimir_pos()
        if self.right:
            self.right.imprimir_pos()
        if self.data:
            print(self.data,end=' ')

    # def tamanho(self):
    #     if not self.data:
    #         return 0
    #     else:
    #         if self.left:
    #             esq = self.left.tamanho() 
    #         else:
    #             esq = 0
    #         if self.right:
    #             dir = self.right.tamanho() 
    #         else:
    #             dir = 0
    #         return esq + dir + 1

    def tamanho(self):
        if not self.data:
            return 0
        else:
            return (self.left.tamanho() if self.left else 0) + (self.right.tamanho() if self.right else 0) + 1

    def altura(self):
        if not self.data:
            return -1
        else:
            alt_e = self.left.altura() if self.left else -1
            alt_d = self.right.altura() if self.right else -1
            # if alt_e > alt_d:
            #     return alt_e + 1
            # else:
            #     return alt_d + 1
            return alt_e + 1 if alt_e > alt_d else alt_d + 1

    def balanceada(self):
        if not self.data:
            return True
        else:
            x = self.left.balanceada() if self.left else True
            y = self.right.balanceada() if self.right else True
            alt_e = self.left.altura() if self.left else -1
            alt_d = self.right.altura() if self.right else -1
            z = abs(alt_d - alt_e) <= 1
            return x and y and z

    def gerar_lista(self,lista):
        if self.data:
            if self.left:
              self.left.gerar_lista(lista)
            lista.append(self.data)
            if self.right:
              self.right.gerar_lista(lista)
        
root = BSTnode()
root.insert(10)
root.insert(7)
root.insert(20)
root.insert(3)
root.insert(5)
root.insert(13)
root.insert(22)
root.insert(8)
root.imprimir_pre()
print()
root.imprimir_central()
print()
root.imprimir_pos()
print('\nTamanho:', root.tamanho())
print('Altura: ', root.altura())
print('Balanceada: ', root.balanceada())
vet = []
root.gerar_lista(vet)
print('Lista:',vet )