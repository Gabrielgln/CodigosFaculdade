/*
4. Faça um programa que implemente o jogo da senha (para 2 pessoas): 

a) O jogador 1 digita uma senha (valor inteiro entre 0 e 100) sem o conhecimento do jogador 2; 
b) O jogador 2 tem 5 chances para descobrir a senha; 
c) A cada tentativa do jogador 2, o programa deve avisar se o valor digitado é maior, menor ou igual a senha; 
d) Se o jogador 2 acertar a senha, o programa não deve pedir mais nenhuma tentativa. 
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
    if (valor2 > valor1){
      printf("\no valor digitado é maior que a senha!");
    }
    else if (valor2 < valor1){
      printf("\nO valor digitado é menor que a senha!");
    }
    else{
      printf("Você acertou!Parabéns hehehe:)");
      break;
    }
  }
  printf("\nVocê não conseguiu, mais sorte da proxima vez!");
  return 0;
}