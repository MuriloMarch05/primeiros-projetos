#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
    cout << fixed << setprecision(3);
    
    double raio, pi, volume;
    
    cin >> raio;
    
    pi = 3.14159;
    
    volume = (4.0/3) * pi * pow(raio, 3);
    
    cout << "VOLUME = " << volume << endl;
}


