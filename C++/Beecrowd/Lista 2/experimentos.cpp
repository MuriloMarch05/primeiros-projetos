#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    cout << fixed << setprecision(2);
    int cont=0,qtd_exp=0, quantia=0, total=0, ratos=0, sapos=0, coelhos=0;
    char tipo;
    
    cin >> qtd_exp;
    
    for (cont=1;cont<=qtd_exp;cont++)
    {
        cin >> quantia;
        cin >> tipo;
        
        if (tipo == 'C')
        {
            coelhos += quantia;
        }
        
        else if (tipo == 'R')
        {
            ratos += quantia;
        }
        
        else if (tipo == 'S')
        {
            sapos += quantia;
        }
        
    }
    
    total = coelhos + ratos + sapos;
    cout << "Total: " << total <<" cobaias" << endl;
    cout << "Total de coelhos: " << coelhos << endl;
    cout << "Total de ratos: " << ratos << endl;
    cout << "Total de sapos: " << sapos << endl;
    cout << "Percentual de coelhos: " << ((double)coelhos/total) * 100 << " %" << endl;
    cout << "Percentual de ratos: " << ((double)ratos/total) * 100 << " %" << endl;
    cout << "Percentual de sapos: " << ((double)sapos/total) * 100 << " %" << endl;
    
    return 0;
}