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
        self.cena = self.cria(cenario=cenario) if vitollino else None
        
    def cria_pecas(self,x,y):
        ''' Gera 
        '''
          
    def cria(self, mapa=" "):
        """ Cria o ambiente de programação Kwarwp."""
        cena = self.v.c(self.TABULEIRO["_"])
        ceu = self.v.a(self.TABULEIRO["~"], w =, h =, x=, y=, cena=cena)
        sol = self.v.a(self.TABULEIRO["*"], w =60, h =60, x=0, y=40, cena=cena)
        indio = 
        tabuleiro = 
        cena.vai()
        #return cena
    
if __name__ == "__main__":
    Kwarwp(Jogo) 