/*Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0 até T-1 repetidas vezes, 
conforme exemplo abaixo. Imprima o vetor N. */

#include <iostream>
using namespace std;

int main()
{
    int N[1000];
    int i, T;
    
    cin>>T;
    
    for(i=0;i<1000;i++)
    {
        N[i] = i % T;
        cout << "N["<<i<<"] = "<< N[i] << endl;
    }

    return 0;
}