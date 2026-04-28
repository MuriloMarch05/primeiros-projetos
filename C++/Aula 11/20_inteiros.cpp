/*3) Escreva um programa que leia at� 20 n�meros inteiros para um vetor e calcule a m�dia dos
valores que est�o no intervalo de 10 a 25.
*/
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	setlocale(LC_ALL, "Portuguese");
	int vet[20], i;
	double soma=0, media;
	
	cout << "Digite 20 n�meros inteiros: " << endl;
	
	for(i=0;i<=19;i++)
	{
		cin >> vet[i];
		
		if (vet[i]>=10 && vet[i] <=25)
		{
			soma += vet[i];
		}
	}
	
	media = soma/20;
	
	cout << "A m�dia dos valores entre 10 e 25 �: " << media << endl;

	return 0;
}
