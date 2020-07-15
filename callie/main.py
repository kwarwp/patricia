# patricia.callie.main.py
# Rio de Janeiro, 9 de junho de 2020
from _spy.vitollino.main import Cena, Elemento, STYLE
__version__ = "20.07"
__author__= 'Emanuelle Simas'

STYLE["width"] = 500

TABULEIRO = "https://activufrj.nce.ufrj.br/file/ProgOO/TAB_COMPL_5x5.png"
CARTA = "https://activufrj.nce.ufrj.br/file/ProgOO/Card_Activ.png"
#PosicaoX=
#Posicaoy=
class Jogo:
    """ Representa apenas o tabuleiro do jogo """
    def __init__(self):
        """ Mostra o tabuleiro """
        self.tab = Cena(TABULEIRO)
        self.carta = Elemento(CARTA, x=10, y=10, width=300, heigth=80, cena=self.tab)

    def vai(self):
        """ Mostra a cena do tabuleiro """
        self.tab.vai()
        self.carta.vai()
        #Cena(CENA_CALCADA).vai()
    
if __name__ == "__main__":
    Jogo().vai()

    