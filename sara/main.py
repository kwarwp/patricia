# patricia.sara.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE

__version__ = "20.07"
__author__ = "Paulo Assumpção"

STYLE["width"] = 500
CENA_CALCADA = "https://i.imgur.com/zOxshRh.jpg"
BANHISTA = "https://i.imgur.com/CWQ00XG.jpg"

class Calcada:

    def __init__(self):
        """ Mostra a cena da praia """
        self.cena = Cena(CENA_CALCADA)
        self.banhista = Elemento(BANHISTA, x=100, y=100, cena=self.cena)
        
    """ representa uma cena na calçada da praia """
    def vai(self):
        self.cena.vai()


if __name__ == "__main__":
    Calcada().vai()