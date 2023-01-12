/*
3. Escreva um programa que leia três valores e apresente-os na tela em ordem crescente.
*/
#include <stdio.h>

int main(void) {
  int valor1, valor2, valor3;
  
  printf("Digite o primeiro valor: \n");
  scanf("%d", &valor1);

  printf("Digite o segundo valor: \n");
  scanf("%d", &valor2);

  printf("Digite o terceiro valor: \n");
  scanf("%d", &valor3);
  
  if (valor1 <= valor2 && valor2 <= valor3) {
    printf("%d %d %d", valor1, valor2, valor3);
  }
  else if (valor3 <= valor2 && valor2 <= valor1) {
    printf("%d %d %d", valor3, valor2, valor1);
  }
  else if (valor1 <= valor3 && valor3 <= valor2) {
    printf("%d %d %d", valor1, valor3, valor2);
  }
  else if (valor2 <= valor1 && valor1 <= valor3) {
    printf("%d %d %d", valor2, valor1, valor3);
  }
  else if (valor3 <= valor1 && valor1 <= valor2) {
    printf("%d %d %d", valor3, valor1, valor2);
  } else {
    printf("%d %d %d", valor2, valor3, valor1);
  }
  return 0;
}