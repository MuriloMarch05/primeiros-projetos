#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int num;
    cout << "Digite um número: ";
    cin >> num;
    
    if (num % 2 == 0)
        {
            cout << "O número " << num << " é par.";
        }
        
    else
        {
            cout << "O número " << num << " é ímpar.";
        }
}