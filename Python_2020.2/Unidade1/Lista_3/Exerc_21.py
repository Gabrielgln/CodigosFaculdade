#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 2019);
#Número de acidentes de trânsito com vítimas (em 2019).
#Deseja-se saber:
#Qual o maior e menor índice de acidentes de trânsito e a que cidade pertence; #Qual a média de veículos nas cinco cidades juntas;

veiculos = 0
acidentes = 0
for i in range(5):
  veiculo = int(input('informe o numero de veículos de passeio (em 2019): '))
  acidente = int(input('informe Número de acidentes de trânsito com vítimas (em 2019): '))
  veiculos = veiculos + veiculo
  if acidente < 2000:
    acidentes = acidentes + acidente
m_a = acidentes / i
m = veiculos / i
