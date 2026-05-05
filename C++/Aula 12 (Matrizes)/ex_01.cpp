/*1) Seja a matriz inteira valores (4x4). Preenchê-la por leitura, apresentar seus valores, e a
quantidade de elementos maiores que 15.
*/

#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int valores[4][4], l, c, qtde=0;

    cout << "Digite os valores da matriz 4x4: "<< endl;

    for(l=0; l<4; l++)
    {
        for(c=0; c<4; c++)
        {
            cin >> valores[l][c];

            if (valores[l][c] > 15)
            {
                qtde += 1;
            }
        }
    }
    for (l=0;l<4;l++)
    {
        for(c=0;c<4;c++)
        {
            cout << valores[l][c] << " ";
        }
        cout << endl;
    }

    cout << "Quantidade de elementos maiores que 15: " << qtde << endl;
    return 0;
}