#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int num[10], i, pos=0, neg=0, nulo=0;

    for(i=0; i<10; i++)
    {
        cout << "Digite um número: ";
        cin >> num[i];

        if (num[i] > 0)
        {
            pos += 1;
        }
        else if (num[i] < 0)
        {
            neg += 1;
        }
        else
        {
            nulo += 1;
        }
    }

    cout << "Números digitados: " << endl;
    for(i=0; i<10; i++)
    {
        cout << num[i] << " ";
    }

    cout << "\nQuantidade de números positivos: " << pos;
    cout << "\nQuantidade de números negativos: " << neg;
    cout << "\nQuantidade de números nulos: " << nulo;

    return 0;
}
