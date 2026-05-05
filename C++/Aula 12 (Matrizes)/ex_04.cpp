/*4) Seja a matriz inteira números (4x3). Preenchê-la por leitura, apresentar seus valores, bem
como o menor elemento de sua última linha.*/

#include <iostream>
using namespace std;

int main()
{
    int numeros[4][3], l, c, menor;

    cout << "Digite os valores da matriz 4x3: " << endl;

    for(l=0; l<4; l++)
    {
        for(c=0;c<3;c++)
        {
            cin >> numeros[l][c];

            if (l == 3 && c == 0)
            {
                menor = numeros[l][c];
            }
            else if (l == 3 && numeros[l][c] < menor)
            {
                menor = numeros[l][c];
            }
        }
    }

    cout << "A matriz é: " << endl;
    for(l=0; l<4; l++)
    {
        for(c=0;c<3;c++)
        {
            cout << numeros[l][c] << " ";
        }
        cout << endl;
    }
    cout << "O menor elemento da última linha é: " << menor << endl;
    return 0;
}