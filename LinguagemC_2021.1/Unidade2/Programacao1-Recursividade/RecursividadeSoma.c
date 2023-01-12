#include <stdio.h>
int soma(int v[], int tam){
    if(tam == 0) 
        return 0;
    else
        return v[tam - 1] + soma(v, tam - 1); 
}

int main () {

    int vet[] = {1,3,5,2,6,7,4,9,8};

    printf("Soma: %d\n", soma(vet, 9));

    return 0;
}

