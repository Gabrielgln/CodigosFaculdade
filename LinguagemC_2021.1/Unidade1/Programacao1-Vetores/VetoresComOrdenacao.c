//PESQUISE E IMPLEMENTE UMA FUNÇÃO BINARIA!

#include <stdio.h>
//função pra leitura do vetor!
void ler_vetor(int vet[], int tam){
  for (int i=0 ; i < tam ; i++){
    printf("vetor[%d]: ", i+1);
    scanf("%d",&vet[i]);
  }
}
//função pra imprimir vetor!
void imprimir_vetor(int vet[], int tam){
  for (int i = 0; i < tam; i++){
    printf("%d ",vet[i]);

  }
  printf("\n");
}
//função pra ordenar do menor para o maior (tam-j-1)!
void ordenar_vetor(int vet[], int tam){
  for (int j = 0; j < tam-1; j++){
    for (int i = 0; i < tam-j-1; i++){
      if (vet[i] > vet[i+1]){
        int aux = vet[i];
        vet[i] = vet [i+1];
        vet[i+1] = aux;
      }
    }
  }
}
//função para buscar a posição do elemento no vetor!
int buscar_elemento(int vet[], int tam, int elemento){
  for (int i = 0; i < tam; i++){
    if (vet[i] == elemento){
      return i;
    }
  }
  return -1;
}
int main(void) {
  const int maxtam = 100;
  int tamanho;
  int vetor[maxtam];

  printf("qual o tamanho do vetor: ");
  scanf("%d",&tamanho);

  ler_vetor(vetor,tamanho);
  imprimir_vetor(vetor,tamanho);
  ordenar_vetor(vetor,tamanho);
  imprimir_vetor(vetor,tamanho);

  int valor;
  printf("qual valor deseja saber a posição: ");
  scanf("%d",&valor);
  int posição = buscar_elemento(vetor,tamanho,valor);
  if (posição != -1){
    printf("o valor digitado %d esta na posição %d",valor,posição+1);
  }
  else{
    printf("não encontrado");
  }
  return 0;
}