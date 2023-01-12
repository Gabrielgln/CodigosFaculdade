#include <stdio.h>
#include <stdlib.h>

typedef struct aluno{
  char nome[50];
  int matricula;
  struct aluno *prox;
} Aluno;

int main(void){
  Aluno *lista;
  //primeiro aluno
  lista = malloc(sizeof(Aluno));
  printf("Nome do aluno: ");
  scanf("%s",lista -> nome);
  printf("Matricula: ");
  scanf("%d",&lista -> matricula);
  lista -> prox = NULL;

  //segundo aluno
  Aluno *novo;
  novo = malloc(sizeof(Aluno));
  printf("Nome do Aluno: ");
  scanf("%s",novo -> nome);
  printf("Matricula: ");
  scanf("%d",&novo -> matricula);
  novo -> prox = lista;
  lista = novo;

  //terceiro aluno
  novo = malloc(sizeof(Aluno));
  printf("Nome do Aluno: ");
  scanf("%s",novo -> nome);
  printf("Matricula: ");
  scanf("%d",&novo -> matricula);
  novo -> prox = lista;
  lista = novo;
}