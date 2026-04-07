#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int tempo, velmedia; // Tempo em horas e velocidade média em km/h
    double distancia, litros; // Distância percorrida e litros de combustível consumidos

    cin >> tempo >> velmedia;

    distancia = tempo * velmedia;

    litros = distancia / 12.0; // Consumo de combustível é de 12 km/l

    cout << fixed << setprecision(3);
    cout << litros << endl;
    
}



