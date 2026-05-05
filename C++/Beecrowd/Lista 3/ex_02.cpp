/*Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. 
Em cada posição subsequente, coloque o dobro do valor da posição anterior. 
Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.*/

#include <iostream>
using namespace std;

int main()
{
    int N[10], i;
    int num;
    
    cin>>num;
    N[0] = num;
    
    for(i=0;i<10;i++)
    {
        if(i > 0)
        {
            N[i] = N[i-1] * 2;
        }
    }
    
    for(i=0;i<10;i++)
    {
        cout << "N["<<i<<"]"<< " = " << N[i] << endl;
    }

    return 0;
}