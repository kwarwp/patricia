# patricia.sarah.main.py
# SPDX-License-Identifier: GPL-3.0-or-later

""" Jogo do Mistério da Praia.

    Descubra o mistério desta praia.

Changelog
---------
    20.07
        * NEW: O jogo original.

"""
from _spy.vitollino.main import Cena, Elemento, STYLE
from grace.main import Praia

__version__ = "1.0"
__author__ = "ECHO"
STYLE["width"] = 500
CENA_CALCADA = "http://www.infcross.com.br/mestrado/tabuleiro.jpg"
BANHISTA = "http://www.infcross.com.br/mestrado/botao.jpg"

class Calcada:
    """ Representa uma cena da calçada da praia """
    def __init__(self):
        """ Mostra a cena da praia """
        self.cena = Cena(CENA_CALCADA, direita=Praia())
        self.banhista = Elemento(BANHISTA, x=100, y=200, cena=self.cena)
        #Cena(CENA_CALCADA).vai()
    def vai(self):
        """ Mostra a cena da praia """
        self.cena.vai()
        #Cena(CENA_CALCADA).vai()
    
if __name__ == "__main__":
    Calcada().vai()
    
    
    