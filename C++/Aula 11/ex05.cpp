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
    for (i=0;i<6;i++)
    {
        cin >> vetor[i];
        if (vetor[i] % 2 == 0)
        {
            pares[contPares] = vetor[i];
            contPares++;
        }
        else
        {
            impares[contImpares] = vetor[i];
            contImpares++;
        }

    }

    cout << "Quantidade de números pares: " << contPares << endl;
    cout << "Números pares: ";
    for (i=0;i<contPares;i++)
    {
        cout << pares[i] << " ";

    }
    cout << endl;
    cout << "Quantidade de números ímpares: " << contImpares << endl;
    cout << "Números ímpares: ";
    for (i=0;i<contImpares;i++)
    {
        cout << impares[i] << " ";

    }

    return 0;
}
