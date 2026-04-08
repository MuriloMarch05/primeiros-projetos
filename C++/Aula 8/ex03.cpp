#include <iostream>
using namespace std;

int main() 
{
    setlocale(LC_ALL, "Portuguese");
    int opcaoPr, opcaoSob, opcaoBeb;
    int tot_cal;
    
    tot_cal = 0;
    
    cout <<"1-Vegetariano\n2-Peixe\n3-Frango\n4-Carne\nQual prato? ";
    cin >> opcaoPr;
    
    switch(opcaoPr)
      {
        case 1: tot_cal += 180; break;
        case 2: tot_cal += 230; break;
        case 3: tot_cal += 250; break;
        case 4: tot_cal += 350; break;
        
        default: cout << "Opção de prato inválida." << endl;
      }
    cout << "------------------------------\n";
    cout << "1-Abacaxi\n2-Sorv Diet\n3-Mousse Diet\n4-Mousse Chocolate\nQual sobremesa? ";
    cin >> opcaoSob;
    
    switch(opcaoSob)
      {
        case 1: tot_cal += 75; break;
        case 2: tot_cal += 110; break;
        case 3: tot_cal += 170; break;
        case 4: tot_cal += 200; break;
        
        default: cout << "Opção de sobremesa inválida." << endl;
      }
      
      cout << "------------------------------\n";
      cout << "1-Chá\n2-Suco de laranja\n3-Suco de Melão\n4- Refri diet\nQual bebida? ";
      cin >> opcaoBeb;
      
    switch(opcaoBeb)
      {
        case 1: tot_cal += 20; break;
        case 2: tot_cal += 70; break;
        case 3: tot_cal += 100; break;
        case 4: tot_cal += 65; break;
          
        default: cout << "Opção de bebida inválida." << endl;
      }
    cout << "------------------------------\n";
    cout << "Sua refeição conterá " << tot_cal << "kcal." << endl;
    cout << "Obrigado por escolher nosso restaurante!" << endl;
      
    return 0;
}