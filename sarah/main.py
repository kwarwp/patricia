# patricia.echo.main.py
""" Jogo Olimpíadas de Matemática20.07
        * NEW: O jogo original
"""

from _spy.vitollino.main import Cena, Elemento, STYLE
""" from grace.main import Praia """

__version__ = "1.0"
__author__ = "ECHO"
STYLE["width"] = 1345
STYLE["height"] = "620px"
TABULEIRO = "http://www.infcross.com.br/mestrado/tabuleiro.jpg"
BOTAO = "http://www.infcross.com.br/mestrado/botao.jpg"

class Tabuleiro:
    """ Representa uma cena da calçada da praia """
    def vai(self):
        """ Mostra a cena do tabuleiro """
        Cena(TABULEIRO).vai()

class Jogo:
    """ Representa uma cena de tabuleiro com o botão """
    def __init__(self):
        """ Mostra o tabuleiro com o botão start"""
        self.cena = Cena(TABULEIRO, direita=Tabuleiro())
        self.banhista = Elemento(BOTAO, x=200, y=400, cena=self.cena)
        #Cena(CENA_CALCADA).vai()
    def vai(self):
        """ Mostra o tabuleiro """
        self.cena.vai()
        #Cena(CENA_CALCADA).vai()
    
if __name__ == "__main__":
    Jogo().vai()
    
    
    