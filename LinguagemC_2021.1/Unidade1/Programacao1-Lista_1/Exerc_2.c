/*
2. Considere uma disciplina que adota o seguinte critério de aprovação: os alunos fazem duas provas (P1 e P2) iniciais; se a média nessas duas provas for maior ou igual a 5.0, e se nenhuma das duas notas for inferior a 3.0, o aluno passa direto. Caso contrário, o aluno faz uma terceira prova (P3) e a média é calculada considerando-se essa terceira nota e a maior das notas entre P1 e P2. Neste caso, o aluno é aprovado se a média final for maior ou igual a 5.0. Escreva um programa que leia inicialmente as duas notas de um aluno, fornecidas pelo usuário via teclado. Se as notas não forem suficientes para o aluno passar direto, o programa deve capturar a nota da terceira prova, também fornecida via o teclado. Como saída, o programa deve imprimir a média final do aluno, seguida da mensagem "Aprovado" ou "Reprovado", conforme o critério descrito acima. 
*/

#include <stdio.h>

int main(void) {
  int nota1, nota2, media, nota3;
  printf("\nDigite a sua primeira nota e segunda nota: ");
  scanf("%d %d", &nota1, &nota2);
  media = (nota1 + nota2) / 2;
  if (media >= 5 && nota1 >= 3 && nota2 >= 3) {
    printf("Aprovado!");
  } 
  else {
    printf("\nDigite a terceira nota: ");
    scanf("%d", &nota3);
    if (nota1 > nota2) {
      media = (nota1 + nota3) / 2;
    }
    else {
      media = (nota2 + nota3) / 2;
    }
      if (media >= 5) {
        printf("Sua média é %d e você foi Aprovado!", media);
    } else {
        printf("Sua média é %d e você foi Reprovado!", media);
    }
  }
   
  return 0;
}