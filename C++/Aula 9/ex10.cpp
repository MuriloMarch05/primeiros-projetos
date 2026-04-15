/* 10) Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a
turma é jovem, adulta ou idosa, conforme a média calculada.
*/

#include <iostream>
#include <string>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int pessoas=0, idades=0, soma=0, cont;
    string faixa;
    double media=0;

    cout << "Quantas pessoas você quer cadastrar? ";
    cin >> pessoas;

    for (cont=1; cont <= pessoas; cont++)
        {
            cout << "Digite a idade: ";
            cin >> idades;
            soma += idades;

        }

    media = (double)soma / pessoas;

    if (media>=0 && media<=25)
        {
            faixa = "Jovem";
        }

    else if (media > 25 && media <= 60)
        {
            faixa = "Adulta";
        }
    else if (media > 60)
        {
            faixa = "Idosa";
        }

    cout << "A faixa etária da turma é: " << faixa << endl;
    cout << "A média é: " << media << endl;

}
