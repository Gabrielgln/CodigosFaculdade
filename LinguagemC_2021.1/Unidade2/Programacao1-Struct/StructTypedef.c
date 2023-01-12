#include <stdio.h>
#include <string.h>

typedef struct{
  int m;
  char n[10];
  int tel;
  char dic[20];
}dados;

int main(void){
  dados alunos[2];
  int i;
  for(i=0;i<2;i++){
    printf("Dados do Aluno %d°\n",i+1);
    printf("Nome:\n");
    setbuf(stdin,NULL); //comando para poder da "enter"
    fgets(alunos[i].n,sizeof(alunos[i].n),stdin); //comando para ler uma string
    printf("Matricula:\n");
    scanf("%d",&alunos[i].m);
    printf("Telefone:\n");
    scanf("%d",&alunos[i].tel);
    setbuf(stdin,NULL); //comando para poder da "enter"
    printf("Disciplina:\n");
    fgets(alunos[i].dic,sizeof(alunos[i].dic),stdin); //comando para ler uma string

  }
  for (i=0;i<2;i++){
    printf("Nome: %s, Matricula: %d, Disciplina: %s e Telefone: %d do aluno %d°\n",alunos[i].n, alunos[i].m, alunos[i].dic, alunos[i].tel,i+1);
  

  }
}