/*5) Elabore um programa que carregue um vetor de seis elementos numéricos inteiros, calcule e
mostre:
-a quantidade de números pares;
-quais os números pares;
-a quantidade de números ímpares;
-quais os números ímpares;
*/

#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int vetor[6], pares[6], impares[6], i;
    int contPares = 0, contImpares = 0;

    cout << "Digite 6 números inteiros: " << endl;
    for (i=0;i<6;i++) // carregar o vetor e separar pares e ímpares
    {
        cin >> vetor[i];
        if (vetor[i] % 2 == 0) // verificar se o número é par ou ímpar
        {
            pares[contPares] = vetor[i]; // se for par, armazenar no vetor de pares e incrementar o contador de pares
            contPares++;
        }
        else
        {
            impares[contImpares] = vetor[i]; // se for ímpar, armazenar no vetor de ímpares e incrementar o contador de ímpares
            contImpares++;
        }

    }

    cout << "Quantidade de números pares: " << contPares << endl;
    cout << "Números pares: ";
    for (i=0;i<contPares;i++) // exibir os números pares armazenados no vetor de pares
    {
        cout << pares[i] << " ";

    }
    cout << endl; // pular linha para separar números pares e ímpares
    cout << "Quantidade de números ímpares: " << contImpares << endl;
    cout << "Números ímpares: ";
    for (i=0;i<contImpares;i++) // exibir os números ímpares armazenados no vetor de ímpares
    {
        cout << impares[i] << " ";

    }

    return 0;
}
