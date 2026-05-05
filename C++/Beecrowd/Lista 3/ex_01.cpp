/*Faça um programa que leia um vetor X[10]. 
Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.*/

#include <iostream>
using namespace std;

int main()
{
    int x[10];
    int i;
    
    for(i=0;i<10;i++)
    {
        cin >> x[i];
        if(x[i] <= 0)
        {
            x[i]= 1;
        }
    }
    
    for(i=0;i<10;i++)
    {
        cout << "X[" << i << "]" << " = " << x[i] << endl;
    }
    
    return 0;
}