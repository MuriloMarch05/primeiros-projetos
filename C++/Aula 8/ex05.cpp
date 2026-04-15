#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int tipoViagem, qtdPessoas, precoBase = 0;
    int valTot, cidBR, cidEX;
    
    cout << "Para onde irá viajar? (1-Brasil, 2-Exterior) ";
    cin >> tipoViagem;
    
    switch(tipoViagem) // Tipo de viagem, switch-case raiz
      {
        case 1: // Brasil
          cout << "----------------------------------\n";  
          cout << "Para qual cidade do Brasil?\n1-RJ\n2-Salvador\n3-Porto Alegre\nOpção: ";
          cin >> cidBR;
          
            switch(cidBR) // Switch-case para cidades do Brasil
            {
              case 1: precoBase = 700; break;
              case 2: precoBase = 900; break;
              case 3: precoBase = 880; break;
              
              default: cout << "Opção inválida.\n"; break;
            }
        break; // Fim do case 1
        
        case 2: // Exterior
        cout << "----------------------------------\n";
        cout << "Para qual cidade do exterior?\n1-NY\n2-Paris\n3-Cancún\n4-Madri\nOpção:";
        cin >> cidEX;
        
            switch(cidEX) // Switch-case para cidades do exterior
            {
              case 1: precoBase = 2200; break;
              case 2: precoBase = 3550; break;
              case 3: precoBase = 3900; break;
              case 4: precoBase = 4000; break;
              
              default: cout << "Opção inválida.\n"; break;
            }
            
        break; // Fim do case 2
        
      }

    if (precoBase > 0) // Verificação se o preço base foi definido, ou seja, se a opção de viagem e cidade foram válidas
    {
        cout << "Quantas pessoas? ";
        cin >> qtdPessoas;
    }
    valTot = precoBase * qtdPessoas; // Cálculo do valor total da viagem

    cout << "----------------------------------\n";
    cout << "Você pagará R$ " << valTot << " para viajar." << endl;
    
    return 0;


    // Para fazer os exercícios, usei o Gemini para me auxiliar na lógica em si e na correção, mas o código foi feito por mim. Não solicitei nenhum código pronto, apenas dicas e correções.
}
