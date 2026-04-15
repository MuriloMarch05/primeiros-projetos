/* 12) Uma loja utiliza o código V para transação a vista e P para transação a prazo. Faça um
programa que receba o código e o valor de 15 transações, calcule e mostre:
- valor total das compras à vista;
- valor total das compras a prazo;
- valor total das compras efetuadas;
*/

#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int cont;
    double valor_V, valor_P, total_V=0, total_P=0, tot_geral=0;
    char cod;

    for (cont=1; cont<=15; cont++)
        {
            cout << "Digite o código (V/P): ";
            cin >> cod;

            if (cod == 'V')
            {
                cout << "Valor da transação: ";
                cin >> valor_V;
                total_V += valor_V;
            }
            else if (cod == 'P')
            {
                cout << "Valor da transação: ";
                cin >> valor_P;
                total_P += valor_P;
            }
            else
            {
                cout << "Código inválido!" << endl;
                break;
            }
        }

    tot_geral = total_V + total_P;

    cout << "Valor total das compras à vista: R$ " << total_V << endl;
    cout << "Valor total das compras a prazo: R$ " << total_P << endl;
    cout << "Valor total das compras efetuadas: R$ " << tot_geral << endl;

}
