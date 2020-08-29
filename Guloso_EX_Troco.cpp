#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> moedas{100,50,25,10,5,1};//VETOR COM AS MOEDAS EXISTENTES
    int total = 0; // 
    int tam_vetor = sizeof(moedas)/sizeof(int);// QTD DE MOEDAS DISPONIVEIS
    int troco;
    cout<<"Qual o valor do seu troco?: ";
    cin >> troco; // RECEBE O NOVO VALOR DE TROCO
    
    for(int i=0; i<tam_vetor; i++){// LACO QUE VAI DE 0 ATE 
        int num_moedas = troco / moedas[i];// num_moedas = 33/10 = 3.3
        troco -= num_moedas * moedas[i]; // 3.3*10=33 33-30=3
        total += num_moedas;//

        if(num_moedas > 0){ // IMPRIME APENAS AS MOEDAS QUE PRECISA
            cout<< num_moedas
            <<" moeda(s) de "
            << moedas[i] << endl;
        }// FIM DO IF
    }// FIM DO FOR
    cout << endl <<"Sendo um Total de "
    << total
    << " moeda(s)" <<endl;
}// FIM DO PROGRAMA