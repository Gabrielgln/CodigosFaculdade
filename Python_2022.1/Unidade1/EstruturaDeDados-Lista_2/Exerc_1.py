#Apresente uma codificação em Python que possui uma função que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule e apresente o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

def alugar_carro(dias,km):
  dias = dias*60
  km = km * 0.15
  print("O valor a ser pago pelo aluguél do carro é: ",dias +km) 
  return dias + km

dias_aluguel = int(input("Digite a quantidade de dias que você alugou o carro: "))
km_rodados = int(input("Digite a quantidade de km rodados durante esses dias: "))
alugar_carro(dias_aluguel,km_rodados)



#Apresente uma codificação em Python que possui uma função recursiva que insere 4 dados em uma lista.


def inserir_dados(dados,lista,cont):
  if cont<4:
    lista.append(dados[cont])
    inserir_dados(dados,lista,cont+1)  
  return lista
    
idade = int(input("Digite a idade: "))
nome = (input("Digite a nome: "))
numero = int(input("Digite o numero: "))
end = int(input("Digite o endereço: "))
dados_usuario = idade,nome,numero,end
l = []
inserir_dados(dados_usuario,l,0)
print(l)