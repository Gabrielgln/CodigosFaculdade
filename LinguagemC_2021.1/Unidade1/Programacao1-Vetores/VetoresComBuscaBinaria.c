#include <stdio.h>

int PesquisaBinaria (int vet[], int chave, int tam)
{
     int inf = 0;     // limite inferior (o primeiro índice de vetor em C é zero          )
     int sup = tam-1; // limite superior (termina em um número a menos. 0 a 9 são 10 números)
     int meio;
     
     while (inf <= sup)
     {
          meio = (inf + sup)/2;
          if (chave == vet[meio]){
            return meio;     
			   }
          else if (chave < vet[meio]){
            sup = meio-1;
          }
          else{
            inf = meio+1;
          }
     }
     return -1;   // não encontrado
}
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
int main(void)
{
printf("Busca Linear\n");

int numeros[10]={1,5,3,4,6,2,7,10,9,8};
ordenar_vetor(numeros,10);
int i, valor;

printf("Qual é o valor que deseja procurar?\n");
scanf("%d", &valor);

int n;
n = PesquisaBinaria (numeros, valor, 10);

if (n != -1){
	printf("Achou na posicao %d!", n);
}

return(0);
}