#include <stdio.h>

int main(void){
  int mat[10][10];
  int ordem;

  //Escolha da ordem da matriz
  printf("Qual a ordem da matriz: ");
  scanf("%d", &ordem);

  //Leitura da matriz
  for(int i = 0; i<ordem; i++){
    for(int j = 0; j<ordem; j++){
      printf("Elemento[%d],[%d]: ",i+1,j+1);
      scanf("%d", &mat[i][j]);
    }
  }

  //impressão da matriz
  for(int i = 0; i<ordem; i++){
    for(int j = 0; j<ordem; j++){
      printf("%d ", mat[i][j]);
    }
  printf("\n");  // pular linha
  }

  //Soma da diagonal secundária
  int soma = 0;
  for(int i = 0; i<ordem; i++){
    soma = soma + mat[i][ordem-i-1];
  }
  //Impressão da soma da diagonal secundária
  printf("A soma da diagonal secundária é %d.",soma);
  return 0;
}