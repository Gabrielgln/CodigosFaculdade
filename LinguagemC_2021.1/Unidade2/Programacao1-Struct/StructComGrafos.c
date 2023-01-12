#include <stdio.h>
#include <string.h>

typedef struct{
  int v1, v2, v3;
}valores;

int main(void) {
  valores valor[1];
  int i;
  for(i=0;i<1;i++){
    printf("digite os valores para serem aprensentados na lista!\n");
    setbuf(stdin,NULL);
    printf("Primeiro valor:\n");
    scanf("%d",&valor[i].v1);
    printf("Segundo valor:\n");
    scanf("%d",&valor[i].v2);
    printf("Terceiro valor:\n");
    scanf("%d",&valor[i].v3);
    printf("Resultado: [%d] -> %d -> %d\n", valor[i].v1, valor[i].v2, valor[i].v3);
    printf("Resultado: [%d] -> %d -> %d\n", valor[i].v2, valor[i].v3, valor[i].v1);
    printf("Resultado: [%d] -> %d -> %d\n", valor[i].v3, valor[i].v2, valor[i].v1);
    printf("\n");
  }
  return 0;
}