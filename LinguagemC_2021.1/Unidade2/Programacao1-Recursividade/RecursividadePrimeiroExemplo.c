#include <stdio.h>

int valor;
int fatorial(int valor){
  if(valor == 0)
    return 1;
  else
    return valor * fatorial(valor - 1);
}
int main(void) {
  printf("Digite o valor para achar seu fatorial\n");
  scanf("%d",&valor);
  printf("O fatorial de %d é %d",valor,fatorial(valor));
  return 0;
}