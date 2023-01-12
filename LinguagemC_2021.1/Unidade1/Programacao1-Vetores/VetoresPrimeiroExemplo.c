#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
  
  int tentativa, aleatoria;

  srand(time(NULL));
  aleatoria = rand()%100;
  //printf("%d\n",aleatoria);

  printf("digite um numero para tentativa: ");
  scanf("%d",&tentativa);
  
  //exemplo do DO WHILE:
  //do{
  //scanf("%d",&tentativa);
  //}while ((tentativa != aleatoria) && (tentativa != 0));
  //&& = and
  //|| = or
  while ((tentativa != aleatoria) && (tentativa != 0)){
    printf("digite um numero para tentativa: ");
    scanf("%d",&tentativa);
  }  

  if (tentativa == aleatoria){
  printf("Acertou\n");
  }else{
  printf("Desistiu de tentar!");
  printf("\nesse era o numero aleatorio: %d",aleatoria);
  }


  return 0;
}
