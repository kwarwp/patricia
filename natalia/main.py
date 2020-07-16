# patricia.natalia.main.py

""" Jogo do Mistério da Praia.

    Agora você desceu para a praia.

Changelog
---------
    20.07
        * NEW: O jogo original.

"""
from _spy.vitollino.main import Cena
__version__ = "15.07"
__author__ = "Rosilane"
CENA_PRAIA = "https://i.imgur.com/wz5XKcr.jpg"


class Mar:
    """ Representa uma cena da calçada da praia """
    def vai(self):
        """ Mostra a cena da praia """
        #Cena(CENA_PRAIA).vai()
    

if __name__ == "__main__":
    Mar().vai()
"""
# patricia.echo.main.py
""" Jogo Olimpíadas de Matemática20.07
        * NEW: O jogo original
"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
""" tabuleiro = Cena (img ="https://www.ibilce.unesp.br/Home/Departamentos/Matematica/2cejta/avancando-com-o-resto.png") """
STYLE["width"] = 1150
STYLE["height"] = "550px"
img ="http://www.infcross.com.br/mestrado/tabuleiro.jpg"
tabuleiro = Cena (img)
tabuleiro.vai()
"""