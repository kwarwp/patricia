# patricia.callie.main.py
# Rio de Janeiro, 5 de agosto de 2020
"""   Implementação do mapa no Kwarwp

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

.. version:: 20.01.1

"""
from _spy.vitollino.main import Jogo, STYLE

#largura e altura, respectivamente
STYLE["width"] = 700
STYLE["height"] = "600px"

MAPA_INICIAL= """
             #######
             #..#..#
             #..@..&
             #..#..#
             #######
"""


class indio():
    """Gera o índio com permissões especiais"""
    def __init__(self):
        pass
    
    
class Kwarwp():
    """ Jogo para ensino de programação.

        :param vitollino: Empacota o engenho de jogo Vitollino.
    """
    
    TABULEIRO ={"#":"https://i.imgur.com/uwYPNlz.png", # CERCA
            "^":"https://imgur.com/8jMuupz.png", # INDIO
            ".":"https://i.imgur.com/npb9Oej.png", #VAZIO
            "_":"https://i.imgur.com/sGoKfvs.jpg", #SOLO
            "&":"https://i.imgur.com/dZQ8liT.jpg", #OCA
            "@":"https://imgur.com/tLLVjfN.png", #PICHE
            "*":"https://i.imgur.com/PfodQmT.gif", #SOL
            "~":"https://i.imgur.com/UAETaiP.gif", #CEU
            "|":"https://imgur.com/ldI7IbK.png",  # TORA 
            }

    def __init__(self, vitollino=None, mapa = MAPA_INICIAL):
        self.v = vitollino()
        """Transforma a string em uma lista onde os 'enter' são considerados vírgula."""
        mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas no mapa
        
           .. note::
              Tente aplicar o seguinte script: > MAPA_INICIO = X 
              > y = x.split() > z = len(y[0])  > print(x,y,z) 
              LEN(MAPA[0]) acessa o primeiro item indexado em zero, retornando sua 'quantidade'
              
        """
        self.lado, self.coluna = 100, len(mapa[0])
        self.cena = self.cria(mapa=mapa) if vitollino else None
        
    def cria_pecas(self,x,y,cena):
        self.lado = lado #trocar posição caso dê problema
        return self.v.a(self.TABULEIRO[imagem], w=lado, h=lado, x=lado*pp ,y=lado+lado*p, cena=cena)
        
          
    def cria(self, mapa=" "):
        """ Cria o ambiente de programação Kwarwp."""
        self.lado = lado
        self.coluna = col
        self.v.c = cenario #alterar depois
        self.v.a = elemento #alterar depois
        cena = self.v.c(self.TABULEIRO["_"])
        ceu = self.v.a(self.TABULEIRO["~"], w =lado*col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(self.TABULEIRO["*"], w =60, h =60, x=0, y=40, cena=cena)
        #indio =
        """"""
        tabuleiro = [self.v.a(self.cria_pecas, x=lado*pp, y=lado+lado*p)
            for p,linha in enumerate(mapa) for pp, imagem in enumerate(linha)]
        cena.vai()
        return cena


if __name__ == "__main__":
    Kwarwp(Jogo) 