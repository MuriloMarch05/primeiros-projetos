/*6) Declare 3 variáveis e atribua a eles o seu nome, a sua idade e o
seu sexo ( ‘M’ ou ‘F’).*/

#include <iostream>
using namespace std;
int main()
{
    string nome;
    int idade;
    char sexo;

    cout << "Digite seu nome: ";
    cin >> nome;
    cout << "Digite sua idade: ";
    cin >> idade;
    cout << "Digite o seu sexo (M ou F): ";
    cin >> sexo;
    cout << "Nome: " << nome << endl;
    cout << "Idade: " << idade << endl;
    cout << "Sexo: " << sexo << endl;
    return 0;

}

