#include <iostream>
using namespace std;

int main()
{
    int id_anos, id_meses, id_dias; // Idade em anos, meses e dias
    int total_dias; // Idade total em dias

    cin >> total_dias;

    id_anos = total_dias / 365; // Calcula a idade em anos
    id_meses = (total_dias % 365) / 30; // Calcula a idade em meses
    id_dias = (total_dias % 365) % 30; // Calcula a idade em dias

    cout << id_anos << " anos, " << id_meses << " meses e " << id_dias << " dias" << endl;
}



