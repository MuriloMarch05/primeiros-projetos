/*6) Faça um programa que leia informações de alunos (Matricula, Nota1, Nota2 , Nota3) com o fim das
informações indicado por Matricula = 9999. Para cada aluno deve ser calculada a média aritmética. Se a média
final for igual ou superior a 5, o programa deve mostrar Matrícula, Média Final e a mensagem "APROVADO" ; se a
média final for inferior a 5, o programa deve mostrar Matricula, Média Final e a mensagem "REPROVADO". Ao
final devem ser mostrados o total de aprovados, o total de alunos da turma e o total de reprovados.*/

#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");

    int matricula=0, tot_apr=0, tot_rep=0, cont=0;
    double nota1, nota2, nota3, media;
    string situacao;
    cout << fixed << setprecision(2);

    while (matricula != 9999)
    {
        cout << "Matrícula (9999 para parar): ";
        cin >> matricula;

        if (matricula == 9999) // Para o loop quando a matrícula for 9999 antes de perguntar as notas.
        {
            break;
        }

        cout << "Nota 1: ";
        cin >> nota1;
        cout << "Nota 2: ";
        cin >> nota2;
        cout << "Nota 3: ";
        cin >> nota3;

        media = (nota1 + nota2 + nota3) / 3;

        if (media >= 5)
        {
            situacao = "APROVADO";
            tot_apr += 1;
        }
        else
        {
            situacao = "REPROVADO";
            tot_rep += 1;
        }

        cout << "Matrícula: " << matricula << "\nMédia final: " << media << "\nSituação: " << situacao << endl;
        cout << "-----------------------------" << endl;

    }

    cout << "-----------------------------\nTotal de aprovados: " << tot_apr << endl;
    cout << "Total de reprovados: " << tot_rep << endl;
    cout << "Total de alunos da turma: " << (tot_apr + tot_rep) << endl;

}
