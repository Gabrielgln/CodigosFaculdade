#include <stdio.h>

int main(void) {
  int i;
  int tam;
  printf("digite a quantidade de valores: \n");
  scanf("%d", &tam);
  int vet[tam];

  for (i=0;i<tam;i++){
    printf("digite o %d° valor: \n",i+1);
    scanf("%d", &vet[i]);
  }
  printf("valores: \n");
  for (i=0;i<tam;i++){
    printf("%d, ",vet[i]);
  }

  return 0;
}