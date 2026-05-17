/*Classificação Etária: Receba a idade de uma pessoa e classifique-a: 5-10 (Infantil), 11-17 (Juvenil), 18-60 (Adulto) e >60 (Sênior).*/

#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");

    int idade;

    cout << "Digite sua idade: " << endl;
    cin >> idade;

    if (idade >= 5 && idade <= 10)
    {
        cout << "Infantil." << endl;
    }

    else if (idade >= 11 && idade <= 17)
    {
        cout << "Juvenil." << endl;
    }

    else if (idade >= 18 && idade <= 60)
    {
        cout << "Adulto." << endl;
    }

    else if (idade > 60)
    {
        cout << "Sênior." << endl;
    }
    
    return 0;
}







