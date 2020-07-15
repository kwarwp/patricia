# patricia.natalia.main.py

""" Jogo do Mistério da Praia.

    Agora você desceu para a praia.

Changelog
---------
    20.07
        * NEW: O jogo original.

"""
from _spy.vitollino.main import Elemento
__version__ = "15.07"
__author__ = "Rosilane"
CENA_PRAIA = "https://i.imgur.com/wz5XKcr.jpg"


class Praia:
    """ Representa uma cena da calçada da praia """
    def vai(self):
        """ Mostra a cena da praia """
        Cena(CENA_PRAIA).vai()
    

if __name__ == "__main__":
    Praia().vai()