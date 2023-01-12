#include <stdio.h>

int valores(int *a, int *b, int *temp);

int main(void){
  int n1,n2,t;
  n1 = 4;
  n2 = 5;
  t = 10;
  valores(&n1,&n2,&t);



  return(0);
}

int valores(int *a, int *b, int *temp){
  *a = *b;
  *b = *temp;
  *temp = *a;
  printf("os valores ficaram assim após a mudança: n1 = %d, n2 = %d e t = %d",*a,*b,*temp);
}

