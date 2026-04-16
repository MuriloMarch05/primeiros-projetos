/*9) Uma eleição possui 2 candidatos a prefeito: o candidato José, do Partido da Felicidade e o candidato
João, do Partido da Esperança. Os eleitores votam nos candidatos pelo número do partido. Para votar no
candidato José do Partido da Felicidade, precisam digitar o número 1. Para votar no candidato João, do
Partido da Esperança, precisam digitar o número 2. Faça um programa que simule uma urna eletrônica.
Para cada eleitor, deve ser lido o número do seu título e em seguida o eleitor poderá digitar o seu voto. A
eleição é encerrada quando um valor negativo (menor do que 0) para o título do eleitor é digitado. Informe
quantos votos cada candidato teve e qual deles ganhou a eleição.
*/

#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int titulo=0, escolha=0, votos1=0, votos2=0;

    do
    {
        cout << "Título (número negativo para parar): ";
        cin >> titulo;

        if (titulo < 0)
            {
                break;
            }

        cout << "Vote\n1-José\n2-João" << endl;
        cin >> escolha;

        if(escolha == 1)
            {
                cout << "Você votou em José do partido Felicidade.\n";
                votos1 += 1;
            }
        else if (escolha == 2)
            {
                cout << "Você votou em João do partido Esperança.\n";
                votos2 += 1;
            }
        else
            {
                cout << "Opção inválida.";
            }


    }while(titulo > 0);

    cout << "O candidato José teve " << votos1 << " voto(s)" << endl;
    cout << "O candidato João teve " << votos2 << " voto(s)" << endl;

        if (votos1 > votos2)
            {
            cout << "O vencedor foi José!";
            }

        else if (votos1 < votos2)
            {
                cout << "O vencedor foi João!";
            }
        else
            {
                cout << "Empate técnico! Necessário segundo turno.";
            }
    return 0;
}
