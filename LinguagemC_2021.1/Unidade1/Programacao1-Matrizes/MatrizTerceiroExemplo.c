#include <stdio.h>
int main(void) {

  int notas [2][5][2];
  int i,j,k;

  char nomes[2][10][10] = {{"igor", "manel", "veronica","gabriel","fred","ruan","davi","bia","hugo","laura"},{"raul", "rebeca", "weleton","JJ","escamoso","ana","froid","eminem","paula","joao"}}; // 2x3

  for (i=0;i<2;i++){
    printf("turma %d°:\n",i+1);
    for (j=0;j<10;j++){
      printf("%s:\n",nomes[i][j]);
      for (k=0;k<2;k++){
        printf("nota %d: ",k+1);
        scanf("%d",&notas[i][j][k]);
        
         
      }
      printf("\n");
    }
    printf("\n");
  }
  
  for (i=0;i<2;i++){
    printf("turma %d°:\n",i+1);
    for (j=0;j<10;j++){
      printf("%s:\n",nomes[i][j]);
      for (k=0;k<2;k++){
        printf("%d pontos\n",notas[i][j][k]);
      }
      printf("\n");

    }
    printf("\n");
  }


return 0;
}
