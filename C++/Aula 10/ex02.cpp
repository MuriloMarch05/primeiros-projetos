/*2) Calcule e mostre a soma dos números impares entre 30 e 100.*/

#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");

    int cont=30, soma=0;

    while (cont <= 100)
    {
       if (cont % 2 != 0)
         {
              soma += cont;
         }
        cont++;
    }
    cout << "A soma dos números ímpares entre 30 e 100 é: " << soma << endl;

    return 0;
}

