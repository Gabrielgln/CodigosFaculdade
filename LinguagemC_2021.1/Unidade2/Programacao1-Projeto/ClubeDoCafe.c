#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct comprador{
  char n[10];
  struct comprador *prox;
}comprador;

comprador *iniciar(){
  return NULL;
}
//todo lugar que tiver "lista" vai ter um "*"! 
void inserir_inicio(comprador **lista, char n[10]){
  comprador *novo = malloc(sizeof(comprador));
  strcpy(novo->n,n);
  if (*lista==NULL){
    *lista = novo;
    (*lista)->prox = NULL;
  }else{
    novo->prox = *lista;
    *lista = novo;
  }
}
//todo lugar que tiver "lista" vai ter um "*"! 
void inserir_fim(comprador **lista, char n[10]){
  comprador *novo = malloc(sizeof(comprador));
  strcpy(novo->n,n);
  if(*lista==NULL){
    *lista = novo;
    (*lista) -> prox = NULL;
  }else{
    comprador *p = *lista;
    while(p->prox!=NULL){
      p=p->prox;
    }
    p->prox = novo;
  }
}
comprador *excluir (comprador **lista){
  if(*lista!=NULL){
  comprador *aux = *lista;
  *lista = (*lista)->prox;
  free (aux);
  }
  return *lista;
}
void imprimir(comprador *lista){
  while(lista != NULL){
    printf("Sequencia de compra do café: %s\n",lista->n);
    lista=lista->prox;
  }
}
int main(void){
  comprador *lista = iniciar();
  char nome[10];
  int i;
  int rodar;
  comprador *nome_fim;
  printf("Total de funcionarios:\n ");
  scanf("%d",&rodar);
  for(i=0;i<rodar;i++){
    printf("Digite o nome do %d° funcionario:\n ",i+1);
    scanf("%s",nome);
    inserir_fim(&lista,nome);
  }
  int pausa = 0;
  while(pausa!=1){
    int r;
    printf("----------------------\n");
    printf("Menu do clube do café:\n");
    printf("\n");
    printf("1 - Para incluir um novo funcionario\n");
    printf("2 - Para excluir o 1° da fila e incluir no fim da fila\n");
    printf("0 - Encerrar o codigo\n");
    printf("----------------------\n");
    scanf("%d",&r);
    if(r==1){
      printf("Digite o nome do novo funcionario:\n ");
      scanf("%s",nome);
      inserir_fim(&lista,nome);
      imprimir(lista);
    }
    else if(r==2){
      printf("----------------------\n");
      printf("Sequencia de compra do café:\n");
      printf("\n");
      imprimir(lista);
      printf("----------------------\n");
      printf("Digite o nome do 1° funcionario da fila: \n");
      scanf("%s",nome);
      inserir_fim(&lista,nome);
      lista = excluir(&lista);
      printf("\n");
      printf("----------------------\n");
      printf("Nova sequencia de compra do café: \n");  
      imprimir(lista);
      printf("----------------------\n");
      break;
    }
    else if(r==0){
      pausa = 1;
      printf("O codigo está encerrado!");
    }
  }
  return 0;
}