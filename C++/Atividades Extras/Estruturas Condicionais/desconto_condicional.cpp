/*Desconto Condicional:** Dado o preço de uma mercadoria e a sua categoria (A ou B) dê um desconto em seu preço de acordo com a seguinte regra:

- 5% se for da categoria A e o preço for superior ou igual a $100,00
  
- 8% se for da categoria A e o preço for inferior a $100,00
  
- 10% se for da categoria B e o preço for superior ou igual a $50,00
  
- 12% se for da categoria B e o preço for inferior a $50,00*/

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");
    cout << fixed << setprecision(2);
    
    double preco, desconto;
    char categoria;

    cout << "Digite o preço do produto: R$ ";
    cin >> preco;

    cout << "Qual a categoria? (A/B) ";
    cin >> categoria;

    categoria = toupper(categoria);

    if (categoria == 'A')
    {

        if (preco >= 100)
        {
            desconto = preco*0.95;
            cout << "Preço final com desconto de 5%: R$ " << desconto << endl;
        }
    
        else if (preco < 100)
        {
            desconto = preco*0.92;
            cout << "Preço final com desconto de 8%: R$ " << desconto << endl;
        }
    }

    else if (categoria == 'B')
    {
        if(preco >= 50)
        {
            desconto = preco*0.90;
            cout << "Preço final com desconto de 10%: R$ " << endl;
        }

        else if (preco < 50)
        {
            desconto = preco*0.88;
            cout << "Preço final com desconto de 12%: R$ " << endl;
        }
    }

    else
    {
        cout << "Categoria inválida."<< endl;   
    }

    return 0;
}
