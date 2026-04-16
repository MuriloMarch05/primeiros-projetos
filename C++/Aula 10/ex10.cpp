/*10) Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo
(M/F) e salário. Faça um programa que informe:
a) a média de salário do grupo;
b) a maior e a menor idade do grupo;
c) a quantidade de mulheres com salário até R$1100,00. Encerre a entrada de dados quando for digitada
uma idade negativa que não fará parte dos cálculos.*/

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int idade, cont=0, tot_mulheres=0, maior_idade=0, menor_idade=999;
    double salario, media_salarios, soma_salarios=0;
    char sexo;

    do
    {
        cout << "Idade: ";
        cin >> idade;

        if (idade < 0)
        {
            break;
        }

        else if (idade > maior_idade)
        {
            maior_idade = idade;
        }
        else if (idade < menor_idade)
        {
            menor_idade = idade;
        }

        cout << "Sexo (M/F): ";
        cin >> sexo;
        sexo = toupper(sexo);

        cout << "Salário: R$ ";
        cin >> salario;
        soma_salarios += salario;


        if (sexo == 'F' && salario <= 1100)
        {
            tot_mulheres += 1;
        }

        cont++;

    }while(idade > 0);

    media_salarios = soma_salarios / double(cont);

    cout << "a) Média de salário do grupo: R$ "<< media_salarios << endl;
    cout << "b) Maior idade: " << maior_idade << "Menor idade: " << menor_idade << endl;
    cout << "c) Mulheres com salario até R$1100: " << tot_mulheres << endl;

}
