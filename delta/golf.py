# patricia.delta.golf.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo da Memória.

.. codeauthor:: Paulo Assumpção <paulo.assump@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""

from _spy.vitollino.main import Cena, Elemento, STYLE
__version__ = "20.07"
__author__ = "Paulo Assumpção"

class Card(object):
    width = 70
    height = 95

    def __init__(self, name):
        self.name = name
        #extracts only the type information from the card name parameter
        self.type = self.name[1:]
        self.faceDown = True
        self.removed = False
        self.position = [0,0]
    
    #returns if a click was withing the bounds of the card
    def checkBounds(self, x, y):
        if (x > self.position[0] and x < self.position[0] + Card.width
            and y > self.position[1] and y < self.position[1] + Card.height):
            self.faceDown = not self.faceDown
            return True
        return False
        


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