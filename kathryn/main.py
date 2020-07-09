# patricia.kathryn.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
__author__ = 'Rodrigo'
__version__ = '20.07'

http://1.bp.blogspot.com/_j2E5RPBo45s/S1Hi7RGkIMI/AAAAAAAAADI/Xn66c31EJNw/s1600-h/cartoes_memoria.JPG

''' Mágica da idade:

    Poderá esconder tudo, menos a sua idade!

Changelog
---------
    20.07
        * NEW: O jogo original.

'''
from _spy.vitollino.main import Cena, Elemento, STYLE
from grace.main import Praia


STYLE["width"] = 500
CENA_CALCADA = 'http://1.bp.blogspot.com/_j2E5RPBo45s/S1Hi7RGkIMI/AAAAAAAAADI/Xn66c31EJNw/s1600-h/cartoes_memoria.JPG'
BANHISTA = "https://i.imgur.com/CWQ00XG.png"


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