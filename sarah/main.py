# patricia.sarah.main.py

""" Jogo Olimpíadas de Matemática20.07
        * NEW: O jogo original
"""

from _spy.vitollino.main import Cena, Elemento, STYLE
from grace.main import Praia
__version__ = "20.07"
__author__ = "Renato"
STYLE["width"] = 500
TABULEIRO = "http://www.infcross.com.br/mestrado/tabuleiro.jpg"
BOTAO = "http://www.infcross.com.br/mestrado/botao.jpg"


class Jogo:
    """ Representa uma cena da calçada da praia """
    def __init__(self):
        """ Mostra o tabuleiro """
        self.cena = Cena(TABULEIRO, direita=Praia())
        self.banhista = Elemento(BANHISTA, x=100, y=200, cena=self.cena)
        #Cena(CENA_CALCADA).vai()
    def vai(self):
        """ Mostra o tabuleiro """
        self.cena.vai()
        #Cena(CENA_CALCADA).vai()
    
if __name__ == "__main__":
    Jogo().vai()
    
    
    