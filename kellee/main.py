# patricia.kellee.main.py

"""
 Iniciando  jogo!

"""

#from _spy.vitollino.main import Cena, Elemento, STYLE
#_version_="14.07"
#_author_ = "Rosilane"

#FUNDO = "https://image.freepik.com/vetores-gratis/plataforma-de-tileset-e-plano-de-fundo-para-criar-jogos-para-celular_22289-375.jpg"

#def vai():
#	""" Mostrar o Fundo"""
#	Cena(FUNDO).vai()
#vai()


""" Jogo do Mistério da Praia.

    Descubra o mistério desta praia.

Changelog
---------
    20.07
        * NEW: O jogo original.

"""
from _spy.vitollino.main import Cena, Elemento, Texto,STYLE
from natalia.main import Mar
from grace.main import Praia
__version__ = "15.07"
__author__ = "Rosilane"
STYLE["width"] = 500
CENA_CALCADA = "https://i.imgur.com/zOxshRh.jpg"
BANHISTA = "https://i.imgur.com/CWQ00XG.png"


class Calcada:
    """ Representa uma cena da calçada da praia """
    def __init__(self):
        """ Mostra a cena da praia """
        self.cena = Cena(CENA_CALCADA, direita=Praia())
        self.banhista = Elemento(BANHISTA, x=100, y=200, cena=self.cena)
        
        self.cena = Cena(CENA_CALCADA, direita=Mar())
        self.banhista = Elemento(BANHISTA, x=100, y=200, cena=self.cena)
        
        #Cena(CENA_CALCADA).vai()
    def vai(self):
        """ Mostra a cena da praia """
        self.cena.vai()
        #Cena(CENA_CALCADA).vai()
    
if __name__ == "__main__":
    Calcada().vai()
