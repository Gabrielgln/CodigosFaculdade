#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
#O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%
#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
    #Salário Bruto: (5 * 220)        #: R$ 1100,00

    #(-) IR (5%)                     #: R$   55,00 

    #(-) Sindicato ( 3%)             #: R$   33,00

    #FGTS (11%)                      #: R$  121,00

    #Total de descontos              #: R$   88,00

    #Salário Líquido                #: R$ 1012,00
hora = float(input('qual o valor da sua hora:'))
horas = float(input('qual o total de horas por mês:'))

salario_bruto = hora * horas
print('salario bruto:',salario_bruto)

if salario_bruto <= 900:
  ir = 0
  percentual = 0

elif salario_bruto <= 1500:
  ir = salario_bruto * 0.05
  percentual = 5

elif salario_bruto <= 2500:
  ir = salario_bruto * 0.10
  percentual = 10

else:
  ir = salario_bruto * 0.20
  percentual = 20
print('(-) IR (',percentual,'%): R$',ir)

sindicato = salario_bruto * 0.03
print('(-) sindicato (3%): R$',sindicato)

fgts = salario_bruto * 0.11
print('FGTS (11%): R$',fgts)

descontos = ir + sindicato
print('total de descontos: R$',descontos)

print ('salario liquido: R$', salario_bruto - descontos)
