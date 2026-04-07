#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int cod, qtd; // Código do produto e quantidade comprada
    double valor; // Valor total a ser pago

    cin >> cod >> qtd;
    
    switch(cod)
    {
        case 1:
            valor = qtd * 4.00;
            break;
        case 2:
            valor = qtd * 4.50;
            break;
        case 3:
            valor = qtd * 5.00;
            break;
        case 4:
            valor = qtd * 2.00;
            break;
        case 5:
            valor = qtd * 1.50;
            break;
        default:
            valor = 0.00; // Código inválido

    }
    cout << fixed << setprecision(2);
    cout << "Total: R$ "<< valor << endl;
}



