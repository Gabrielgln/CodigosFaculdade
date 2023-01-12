/*
5. Faça as seguintes alterações no jogo da senha (exercício 4): 

a) se o valor digitado em uma tentativa tiver uma diferença igual a 1 para a senha, o programa deve avisar que “TÁ QUENTE!”. Neste caso, nenhuma outra mensagem deve ser emitida. Nos demais casos, continuam valendo as mensagens exibidas no exercício anterior. 

Exemplos:  
senha 43 e valor digitado 42 : TÁ QUENTE!!!  
senha 43 e valor digitado 44 : TÁ QUENTE!!!; 

b) Ao final do jogo, se for o caso, enviar a mensagem “Você perdeu. Tente novamente depois”; 
c) Ao final de uma partida, permita ao usuário jogar novamente.
*/

#include <stdio.h>

int main(void) {
  int valor1, valor2;
  int i;
  printf("\nJogador 1-digite um numero de 0-100: ");
  scanf("%d", &valor1);
  for (i = 0; i <= 5; i++) { 
    printf("\nJogador 2-digite um numero de 0-100: ");
    scanf("%d", &valor2);
    if (valor2 + 1 == valor1 || valor2 - 1 == valor1) {
      printf("TA QUENTE CARAI!");
    }
    else if (valor2 > valor1){
      printf("\no valor digitado é maior que a senha!");
    }
    else if (valor2 < valor1){
      printf("\nO valor digitado é menor que a senha!");
    }
    else {
      printf("Você acertou!Parabéns hehehe:)");
      break;
    }
  }
  printf("\nVocê não conseguiu, mais sorte da proxima vez!");
  int tentativa;
  printf("deseja jogar novamente: 1-sim ou 2-não");
  scanf("%d", &tentativa);
  if (tentativa == 1){
    for (i = 0; i <= 5; i++) { 
        printf("\nJogador 2-digite um numero de 0-100: ");
        scanf("%d", &valor2);
      if (valor2 + 1 == valor1 || valor2 - 1 == valor1) {
        printf("TA QUENTE CARAI!");
      }
      else if (valor2 > valor1){
        printf("\no valor digitado é maior que a senha!");
      }
      else if (valor2 < valor1){
        printf("\nO valor digitado é menor que a senha!");
      }
      else {
        printf("Você acertou!Parabéns hehehe:)");
      break;
    }
  }
  printf("\nVocê não conseguiu, mais sorte da proxima vez!");
  }
  return 0;
}