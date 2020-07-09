# patricia.sara.main.py

from _spy.vitollino.main import Cena

__version__ = "20.07"
__author__ = "Paulo Assumpção"

CENA_CALCADA = "https://i.imgur.com/zOxshRh.jpg"
CENA_DIREITA = ""

class Calcada:
    """ representa uma cena na calçada da praia """
    def vai(self):
        """ Mostra a cena da praia """
        Cena(CENA_CALCADA).vai()

if __name__ == "__main__":
    Calcada().vai()