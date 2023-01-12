#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct agenda {
  char nome[40];
  char tel[15];
  char cel[15];
  char email[40];
  int cod;
  struct agenda *prox;
} Agenda;

Agenda *inicializar(){
  return NULL;
}

void inserir_contato(Agenda **lista,char nome[40],char tel[15],char cel[15],char email[40],int cod){
  Agenda *novo = malloc(sizeof(Agenda));
  novo->cod = cod;
  strcpy(novo->nome,nome);
  strcpy(novo->tel,tel);
  strcpy(novo->cel,cel);
  strcpy(novo->email,email);
  if (lista == NULL){
    *lista = novo;
    (*lista)->prox = NULL;
  }else{
    novo->prox = *lista;
    *lista = novo;
  }
}

void listar_contatos(Agenda *lista){
  while(lista != NULL) {
    printf("Nome: %s\n", lista->nome);
    printf("Telefone: %s\n", lista->tel);
    printf("Celular: %s\n", lista->cel);
    printf("E-mail: %s\n", lista->email);
    printf("Codigo: %d\n",lista->cod);
    lista = lista->prox;
  }
}

void buscar_contato(Agenda *lista,int cod) {
  Agenda *pont = lista;
  while (pont != NULL){
    if (pont->cod == cod) {
      printf("\nContato encontrado!");  
    }
    pont = pont->prox; 
  }
}

Agenda *excluir_contato(Agenda **lista,int cod) {
  Agenda *inicio = *lista;
  Agenda *anterior = NULL;
  while (inicio!=NULL && inicio->cod != cod){
    anterior = inicio;
    inicio = (Agenda *)inicio->prox;
  }
  if (inicio==NULL){
    return *lista;
  }
  if (anterior == NULL){
    *lista = inicio->prox;
  }
  else{
    anterior->prox = (Agenda *) inicio->prox;
  }
  free(inicio);
  return *lista;
}

void liberar_agenda (Agenda **lista){
  Agenda *p = *lista;
  Agenda *aux;
  while (p!=NULL){
    aux = (Agenda *) p->prox;
    free(p);
    p=aux;
  }
}

int gerarMenu(int operacao) {
  printf("-------------------\n");
  printf("1 – Inserir Contato\n");
  printf("2 – Listar Contatos\n");
  printf("3 – Buscar Contato\n");
  printf("4 - Exclui um Contato\n");
  printf("5 - Exclui Agenda\n");
  printf("6 – Sair\n");
  printf("-------------------\n");
  printf("Digite a operação que você deseja realizar: ");
  scanf("%d", &operacao);
  return operacao;
}
int main() {
  Agenda *lista = inicializar();
  int operacao;
  char nome[45], telefone[15], celular[15], email[40];
  int codigo;
  operacao = 0;
  while (operacao != 6) {
    operacao = gerarMenu(operacao);
    switch(operacao) {
      case 1:
        printf("Nome: ");
        scanf("%s", nome);
        
        printf("\nTelefone: ");
        scanf("%s", telefone);
        
        printf("\nCelular: ");
        scanf("%s",celular);
        
        printf("\nE-mail: ");
        scanf("%s", email);

        printf("\nCodigo: ");
        scanf("%d",&codigo);
        
        inserir_contato(&lista, nome, telefone, celular, email,codigo);
        setbuf(stdin,NULL);
        break;
      case 2:
        listar_contatos(lista);
        break;
      case 3:
        printf("Digite o codigo do contato:\n ");
        scanf("%s", nome);
        buscar_contato(lista,codigo);
        break;
      case 4:
        printf("Digite o codigo do contato para excluir:\n ");
        scanf("%d",&codigo);
        excluir_contato(&lista,codigo);
        printf("Contato excluído com sucesso!\n");
        break;
      case 5:
        liberar_agenda(&lista);
        printf("Agenda limpada com sucesso!\n");
        break;
      case 6:
        printf("Obrigado e volte sempre!\n");
        break;
    }
  }
  return 0;
}
