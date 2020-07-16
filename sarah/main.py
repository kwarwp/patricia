# patricia.sarah.main.py
# patricia.echo.main.py
""" Jogo Olimpíadas de Matemática20.07
        * NEW: O jogo original
        Autor: Grupo Echo (Aline, Lorena, Renato e Victoria)
"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv

""" tabuleiro = Cena (img ="https://www.ibilce.unesp.br/Home/Departamentos/Matematica/2cejta/avancando-com-o-resto.png") """

STYLE["width"] = 1345
STYLE["height"] = "620px"

tabuleiro ="http://www.infcross.com.br/mestrado/tabuleiro.jpg"
botao = "http://www.infcross.com.br/mestrado/botao.jpg"
#tabuleiro = Cena (img)
#tabuleiro.vai()


def cena_principal():
    inicio = Cena(img=tabuleiro)
    inicio_e = Elemento(img=botao)
    inicio.vai()
    inicio_e.vai()
cena_principal() 






# patricia.adda.main.py
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
    
    
    