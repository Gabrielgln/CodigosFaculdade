valor = int(input("Digite o valor para criptografar: "))
crip = '' #STRING NULA
palavra = "abc" #TEXTO USADO COMO EXEMPLO
for letra in palavra:
  crip_tmp = ord(letra) + valor #ORD - FUNÇÃO DA TABELA ASCII
  if crip_tmp > ord('z'):
    crip_tmp = crip_tmp - 26
  elif crip_tmp < ord('a'):
    crip_tmp = crip_tmp + 26
  crip = crip + chr(crip_tmp) #CONTADOR DE STRING
print(crip)