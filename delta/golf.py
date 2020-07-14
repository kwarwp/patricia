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

class Card():
    def __init__(self, image,cena):
        self.image = image
        self.faceDown = True
        self.imageFaceDown = Elemento("http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline", cena=cena)
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

class Calcada:

    def __init__(self):
        """ Mostra a cena da praia """
        self.cena = Cena(CENA_CALCADA)
        self.banhista = Elemento(BANHISTA, x=100, y=100, cena=self.cena)
        
    """ representa uma cena na calçada da praia """
    def vai(self):
        self.cena.vai()
        
class Game:
    def crate_cards(self):
        self.cena = Cena()
        card1 = Card("http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline", cena)
        card2 = Card("http://activufrj.nce.ufrj.br/file/ProgOO/Card_Linux.png?disp=inline", cena)
        card3 = Card("http://activufrj.nce.ufrj.br/file/ProgOO/Card_Gitlab.png?disp=inline", cena)
        card4 = Card("http://activufrj.nce.ufrj.br/file/ProgOO/Card_github.png?disp=inline", cena)
        card5 = Card("http://activufrj.nce.ufrj.br/file/ProgOO/Card_Activ.png?disp=inline", cena)
    


if __name__ == "__main__":
    Game().crate_cards()