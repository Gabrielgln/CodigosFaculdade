  /*
1. Escreva um programa para ler 2 valores e uma das seguintes operações a serem executadas: 
1. Adição 
2. Subtração 
3. Divisão 
4. Multiplicação 
*/

#include <stdio.h>

int main(void) {
  int valor1, valor2;
  char operacao;
  
  printf("digite o valor 1, um operador e o valor 2: ( (+), (-) (*), (/) ) \n");
  scanf("%d %c %d", &valor1, &operacao, &valor2);

  switch (operacao) {
    case '+':
      printf("%d", valor1 + valor2);
      break;
    case '-':
      printf("%d", valor1 - valor2);
      break;
    case '/':
      printf("%d", valor1 / valor2);
      break;
    case '*':
      printf("%d", valor1 * valor2);
      break;
    default:
      printf("Operador inválido!");
  }
  
  return 0;
}