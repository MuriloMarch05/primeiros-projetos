/*Faça um programa para ler 5 números inteiros quaisquer e armazená-los em
um vetor A. Em seguida, criar um novo vetor B cujos elementos são os
elementos do vetor A com sinal trocado. Imprima os 2 vetores.*/

#include <iostream>
using namespace std;

int main()
{   
    setlocale(LC_ALL, "Portuguese");
    int A[5], B[5];
    int i;
    cout << "Digite 5 números inteiros: " << endl;
    
    for (i = 0; i < 5; i++)
    {
        cin >> A[i];
        B[i] = -A[i];
    }

    cout << "Vetor A: ";

    for (i = 0; i < 5; i++)
    {
        cout << A[i] << " ";
    }

    cout << "\nVetor B: ";

    for (i = 0; i < 5; i++)
    {
        cout << B[i] << " ";
    }

    return 0;
}