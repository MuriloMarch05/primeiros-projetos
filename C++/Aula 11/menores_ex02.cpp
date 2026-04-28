/*2) Leia 8 idades e armazene-as em um vetor. A seguir, apresente um relat�rio que imprima
somente as idades menores de 18 anos digitadas.*/

#include <iostream>
using namespace std;

int main()
{
	setlocale(LC_ALL, "Portuguese");
	int idades[8], i;
	
	cout << "Digite oito idades: " << endl;
	
	for(i=0;i<8;i++)
	{
		cin >> idades[i];
	}
	
	cout << "\nMenores de 18 anos: ";
	
	for(i=0;i<8;i++)
	{
		if(idades[i]<18)
		{
			cout << idades[i] << " ";
		}
	}

	return 0;
} 
