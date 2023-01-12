#include <stdio.h>
#include <string.h>

int main(void) {
  
  char linha[2];
  int coluna[10];
  int i,j;



  for (i = 0; i < 2; i++){
    for ( j = 0; j < 10; j++){
      printf("Turma [%d], Aluno [%d]: ", i+1 ,j+1);
      scanf("%d %c", &linha[i], &coluna[i]);
    }
    printf("\n");
  }


  return 0;
}