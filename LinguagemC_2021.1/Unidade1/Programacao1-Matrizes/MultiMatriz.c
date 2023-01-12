#include <stdio.h>

void ler_matriz(int mat[10][10], int lin, int col){
  for(int i = 0; i < lin; i++)
    for(int j = 0; j < col; j++){
      printf("Mat[%d,%d]: ",i+1,j+1);
      scanf("%d",&mat[i][j]);
    }
}

void imprimir_matriz(int mat[10][10], int lin, int col){
  for(int i = 0; i < lin; i++){
    for(int j = 0; j < col; j++){
      printf("%d ",mat[i][j]);
    }
    printf("\n");
  }
}

void multiplicar_matrizes(int matr[10][10],int mat1[10][10], int l1, int c1, int mat2[10][10], int l2, int c2){
  for(int i = 0; i < l1; i++){
    for(int j = 0; j < c2; j++){
      matr[i][j] = 0;
      for(int k = 0; k < l2; k++)
        matr[i][j] = matr[i][j] + mat1[i][k] * mat2[k][j];
    }
  }
}

int main(void) {
  int m1[10][10], m2[10][10], mr[10][10];
  int l1, c1, l2, c2;
  printf("Matriz 1:\nQuantas linhas? ");
  scanf("%d",&l1);
  printf("Quantas colunas? ");
  scanf("%d",&c1);
  ler_matriz(m1, l1, c1);
  printf("Matriz 2:\nQuantas linhas? ");
  scanf("%d",&l2);
  printf("Quantas colunas? ");
  scanf("%d",&c2);
  ler_matriz(m2, l2, c2);
  printf("Matriz 1\n");
  imprimir_matriz(m1, l1, c1);
  printf("Matriz 2\n");
  imprimir_matriz(m2, l2, c2);
  if(c1 == l2){
    printf("Matriz 1 x matriz 2\n");
    multiplicar_matrizes(mr, m1, l1, c1, m2, l2, c2);
    imprimir_matriz(mr,l1,c2);
  } else {
    printf("Não é possível multiplicar as matrizes.\n");
  }
  return 0;
}