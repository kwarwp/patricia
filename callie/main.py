# patricia.callie.main.py
# Rio de Janeiro, 9 de junho de 2020
from _spy_vittollino.main import Cena, STYLE
__version__ = "20.07"
__author__= 'Emanuelle Simas'

STYLE["Width"] = 500

TABULEIRO = "https://activufrj.nce.ufrj.br/file/ProgOO/TAB_COMPL_5x5.png"

class Jogo:
    """ Representa apenas o tabuleiro do jogo """
    def __init__(self):
        """ Mostra o tabuleiro """
        self.tab = Cena(TABULEIRO)

    def vai(self):
        """ Mostra a cena do tabuleiro """
        self.tab.vai()
        #Cena(CENA_CALCADA).vai()
    
if __name__ == "__main__":
    Jogo().vai()

    