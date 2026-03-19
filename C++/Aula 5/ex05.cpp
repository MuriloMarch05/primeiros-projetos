/*5) Escreva um programa que declare 3 variáveis inteiras e atribua
os valores 1, 2 e 3 a elas; 3 variáveis caracteres e atribua a elas as
letras a, b e c ; 1 variável real com o valor 5.68.*/

#include <iostream>
using namespace std;
int main()
{
    int num1, num2, num3;
    char letra1, letra2, letra3;
    float numReal;
    num1 = 1;
    num2 = 2;
    num3 = 3;
    letra1 = 'a';
    letra2 = 'b';
    letra3 = 'c';
    numReal = 5.68;
    cout << "Numeros inteiros: " << num1 << ", " << num2 << ", " << num3 << endl;
    cout << "Letras: " << letra1 << ", " << letra2 << ", " << letra3 << endl;
    cout << "Numero real: " << numReal << endl;
    return 0;
    
}

