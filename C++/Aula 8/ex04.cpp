#include <iostream>
#include <cmath> // Inclui a biblioteca cmath para usar a função pow (potência)
using namespace std;

int main() // Em algumas IDE's, preciso colocar o int main(), se não ele não roda.
{
    setlocale(LC_ALL, "Portuguese"); // Permitir acentos.
    double num1, num2; // Defini como double para ficar mais preciso.
    int opcao;

    cout << "Digite o primeiro número: ";
    cin >> num1;

    cout << "Digite o segundo número: ";
    cin >> num2;

    cout << "Escolha a operação:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Potência\nOpção: ";
    cin >> opcao;

    switch(opcao)
        {
                case 1: cout << "Resultado da soma: " << num1 + num2 << endl; break;

                case 2: cout << "Resultado da subtração: " << num1 - num2 << endl; break;

                case 3: cout << "Resultado da multiplicação: " << num1 * num2 << endl; break;

                case 4: if (num2 != 0) // Condição para evitar divisão por zero.
                    {
                        cout << "Resultado da divisão: " << num1 / num2 << endl; break;
                    }
                    else
                    {
                        cout << "Erro: Divisão por zero não é permitida." << endl; break;
                    }

                case 5: cout << "Resultado da potência: " << pow(num1, num2) << endl; break; // Essa não foi pedida no enunciado, mas achei interessante incluir.
                default: cout << "Opção inválida." << endl; break;
        }

        return 0; // As IDE's deixam isso por padrão, mas não é obrigatório. O programa termina aqui.
}
