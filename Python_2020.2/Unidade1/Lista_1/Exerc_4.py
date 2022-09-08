#Faça um programa que calcule a área total (m2) de uma casa com 4 cômodos. O usuário deve inserir a largura e comprimento de cada um dos cômodos, calcular a área individual de cada um e por fim exibir a área total da casa.

comp1 = float(input('qual o comprimento:'))
larg1 = float(input('qual a largura:'))
comp2 = float(input('qual o comprimento:'))
larg2 = float(input('qual a largura:'))
comp3 = float(input('qual o comprimento:'))
larg3 = float(input('qual a largura:'))
comp4 = float(input('qual o comprimento:'))
larg4 = float(input('qual a largura:'))
m2 = (comp1*larg1)+(comp2*larg2)+(comp3*larg3)+(comp4*larg4)
print('a area total da casa é:', m2)
