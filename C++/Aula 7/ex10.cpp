#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");
    string nome, fx_eta;
    int idade;
    
    cout << "Qual é o seu nome? ";
    getline(cin, nome);
    
    cout << "Qual é a sua idade? ";
    cin >> idade;
    
    if (idade < 12){
        fx_eta = "Criança";
    }

    else if (idade < 20){
        fx_eta = "Adolescente";
    }

    else{
        fx_eta = "Adulto";
    }

    cout << "Nome: "<< nome << endl;
    cout << "Faixa etaria: " << fx_eta << endl;
}