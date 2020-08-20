
class Noh:
    def __init__(self, dados):
        self.dados = dados
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.dados)

class Arvore_Binaria:
    def __init__(self,dados=None):
        if dados:
            noh = Noh(dados)
            self.raiz = noh
        else:
            self.raiz = None            

    def simetria_transversal(self, noh=None):
        if noh is None:
            noh = self.raiz
        if noh.esquerda:    
            print('(', end='')
            self.simetria_transversal(noh.esquerda)
        print(noh, end='')
        if noh.direita:
            self.simetria_transversal(noh.direita)    
            print(')', end='') 
      
if __name__ == "__main__":
    arvore = Arvore_Binaria()
    n1 = Noh('a')
    n2 = Noh('+')
    n3 = Noh('*')
    n4 = Noh('b')
    n5 = Noh('-')
    n6 = Noh('/')
    n7 = Noh('c')
    n8 = Noh('d')
    n9 = Noh('e')

    n6.esquerda = n7
    n6.direita = n8
    n5.esquerda = n6
    n5.direita = n9
    n3.esquerda = n4
    n3.direita = n5
    n2.esquerda = n1
    n2.direita = n3

    arvore.raiz = n2
    
    arvore.simetria_transversal()
    print('') 