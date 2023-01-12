#include <stdio.h>
#include <string.h>

typedef struct{
  int celular;
  int telfixo;
}Contatos;

typedef struct{
  int matricula;
  char nome[10];
  Contatos contato;
}Aluno;

int main(void) {
  
  Aluno alunos[2];
  int i;

  for (i=0;i<2;i++){
    printf("Insira a matrícula\n");
    scanf("%d",&alunos[i].matricula);
    printf("Contato Celular: \n");
    scanf("%d",&alunos[i].contato.celular);
    printf("Contato Telefone Fixo: \n");
    scanf("%d",&alunos[i].contato.telfixo);
    printf("Insira o nome: \n");
    scanf("%s",alunos[i].nome);
  }

  for (i=0;i<2;i++){
    printf("Aluno %s Matrícula %d Telefone: %d \n",alunos[i].nome,alunos[i].matricula,alunos[i].contato.celular);
  }  


  

  return 0;
}