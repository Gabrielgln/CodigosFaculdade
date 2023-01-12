#include <stdio.h>

void leituraMatriz(int t, int mat[][t]){
  int i,j;
  for (i=0;i<t;i++){
    for (j=0;j<t;j++){
      scanf("%d",&mat[i][j]);
    }
  }
}
int main(void) {
  
  int t;
  printf("Digite o tamanho: ");
  scanf("%d",&t);
  int a[t][t];
  int i,j;
  leituraMatriz(t,a);
  for (i=0;i<2;i++){
    for (j=0;j<2;j++){
      printf("%d ",a[i][j]);
    }
    printf("\n");
  }

  return 0;
}