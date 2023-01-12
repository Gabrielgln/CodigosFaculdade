#include <stdio.h>


void ordenar_vetor(int v[],int t){
  int intervalo = t;
  int aux;
  while(intervalo!=1){
    intervalo = intervalo/(1.3);
    for(int i=0;i<(t-intervalo);i++){
      if(v[i]>v[i+intervalo]){
        aux=v[i+intervalo];
        v[i+intervalo]=v[i];
        v[i]=aux;
      }
    }
  }
}
int main(void) {
  int vetor[]={1,4,3,5,2};
  int tam = 5;
  int i;
  ordenar_vetor(vetor,tam);
  for(i = 0;i < tam;i++){
    printf("%d",vetor[i]);
  }
  return 0;
}