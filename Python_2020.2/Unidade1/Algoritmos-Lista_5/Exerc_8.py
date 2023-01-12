#8 - Faça um programa que leia e monte dois vetores de números inteiros com 20 números cada.
#Depois de montados gere um terceiro vetor formado pela diferença dos dois vetores lidos,
#um quarto vetor formado pela soma dos dois vetores lidos e por último um quinto vetor
#formado pela multiplicação dos dois vetores lidos.

vetor = []
vetor2 = []
vetor3 = []
vetor4 = []
vetor5 = []
for i in range(10):
  num = int(input('digite um valor entre 20 e 40 : '))
  num2 = int(input('digite um segundo valor entre 0 e 20 : '))
  vetor.append(num)
  vetor2.append(num2)
  vetor3.append(num - num2)
  vetor4.append(num + num2)
  vetor5.append(num * num2)
print('os números do primeiro vetor: ',vetor)
print('os números do segundo vetor: ',vetor2)
print('a diferença entre os vetores são: ',vetor3)
print('a soma dos vetores são: ',vetor4)
print('a multiplicação dos vetores são: ',vetor5)  