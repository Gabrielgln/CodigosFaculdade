#1 - Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor.
#Os dados deverão ser armazenados no vetor na ordem que forem sendo lidos,
#sendo que caso o usuário digite um número que já foi digitado anteriormente,
#o programa deverá pedir para ele digitar outro número.
#Note que cada valor digitado pelo usuário deve ser pesquisado no vetor,
#verificando se ele existe entre os números que já foram fornecidos.
#Exibir na tela o vetor final que foi digitado.

def lVetor(vetor):
  cont = 0
  while cont < 10: 
    valor = int(input("Digite um valor: "))
    if valor not in vetor: 
      vetor.append(valor) 
      cont = cont + 1 
    else:
      valor = int(input('o valor está repetindo, digite outro valor: '))
      vetor.append(valor)
  return vetor 
       
vetor = [] 
lVetor(vetor)
print(vetor)