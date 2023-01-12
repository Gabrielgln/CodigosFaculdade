def rotate_word(palavra, valor):
  word_rot = ''#palavra vazia
  for letra in palavra: #para cada letra na palavra
    letra_tmp = ord(letra) + valor # transforma a letra em numero que soma + valor
    if letra_tmp > ord('z'):#se letra + valor for maior que Z
      letra_tmp = letra_tmp - 26 #letra vai voltar para A
    elif letra_tmp < ord('a'):#menor que A (CASO O USUARIO DIGITE NUMERO NEGATIVO)
      letra_tmp = letra_tmp + 26
    word_rot = word_rot + chr(letra_tmp)#palavra vazia = palavra vazia + letra 
  return word_rot

print(rotate_word('gabriel',1))

#criptografia rapida
tam = int(input("Digite o tamanho: "))
crip = ''
palavra = "gabriel"
for letra in palavra:
  crip_tmp = ord(letra) + tam
  crip = crip + chr(crip_tmp)
print(crip)