//Faça um programa para ler uma matriz digitada pelo usuário (tamanho 3x3) e exibir uma mensagem dizendo se a mesma é uma matriz identidade ou não. O seu programa deve implementar e utilizar a função matriz_identidade, que recebe como parâmetro uma matriz quadrada de inteiros de dimensão n, e retorna 1 se a matriz for uma matriz identidade, e 0 caso contrário. O protótipo da função pode ser: *//

#include <stdio.h>
int mat_identidade (int mat[][3]) {
  for (int i = 0; i < 3; i++) {
    for (int j = 0;j < 3; j++) {
      if(i == j && mat[i][j] == 1){
        printf("É Matriz Identidade");     
      }
    }
  }
 printf("Não é matriz identidade");
 return 0;
 
}

int main (void) {
  int mat[3][3];
  for (int i = 0; i < 3; i++){
    for(int j = 0; j < 3; j++){
      printf("Matriz[%d,%d]: ", i+1, j+1);
      scanf("%d", &mat[i][j]);
    }
  }
  for (int i = 0; i < 3; i++){
    for(int j = 0;j < 3; j++){
      printf("%d", mat[i][j]);    
    }
  printf("\n");

  }  
  mat_identidade(mat[3][3]);
  return 0;
}