/*
4) Fa�a um algoritmo que leia a nota de 10 alunos, calcule a m�dia da classe e depois imprima as
notas e a m�dia da seguinte forma:
1 - 10.0
2 - 3.3
3 - 8.9
:
10 - 7.2
A media da classe = 7.3
*/

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	cout << fixed << setprecision(1);
	int i, cont;
	double media, soma=0, notas[10];
	
	cout << "Digite as notas dos 10 alunos: " << endl;
	
	for(i=1;i<11;i++)
	{
		cin >> notas[i];
		soma += notas[i];
	}
	
	cout << "Notas dos alunos: " << endl;
	for(i=1;i<11;i++)
	{
		cout << i << " - " << notas[i] << endl;
	}
	
	media = soma/10;
	
	cout << "Media da classe = "<< media << endl;

	return 0;
}
