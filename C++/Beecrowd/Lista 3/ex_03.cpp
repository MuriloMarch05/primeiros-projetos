/*Faça um programa que leia um vetor A[100]. 
No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições. */

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    cout << fixed << setprecision(1);
    double A[100];
    int i;
    
    for(i=0;i<100;i++)
    {
        cin >> A[i];
        
        if(A[i] <= 10)
        {
            cout << "A["<<i<<"]"<< " = "<< A[i] << endl;    
        }
        
    }

    return 0;
}