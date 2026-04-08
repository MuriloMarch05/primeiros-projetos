#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");
    string nome;
    double preco, desconto, val_pago;
    
    cout << "Qual é seu nome? ";
    getline(cin, nome);
    
    cout << "Preço bruto R$";
    cin >> preco;
    
    desconto = 0;
    
    if (preco < 50)
        {
            desconto = preco * 0.10;
        }
   else if (preco <= 100)
        {
            desconto = preco * 0.15;
        }
    else
        {
            desconto = preco * 0.20;
        }

    val_pago = preco - desconto;
    
    cout << setprecision(2) << fixed;
    cout << "\nCliente: " << nome << endl;
    cout << "Valor com desconto: R$" << val_pago << endl;
}