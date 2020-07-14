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
        
        
class Game:
    def crate_5x5_cards(self):
        self.cena = Cena()
        self.card1 = Card("http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline", self.cena)
        self.card2 = Card("http://activufrj.nce.ufrj.br/file/ProgOO/Card_Linux.png?disp=inline", self.cena)
        self.card3 = Card("http://activufrj.nce.ufrj.br/file/ProgOO/Card_Gitlab.png?disp=inline", self.cena)
        self.card4 = Card("http://activufrj.nce.ufrj.br/file/ProgOO/Card_github.png?disp=inline", self.cena)
        self.card5 = Card("http://activufrj.nce.ufrj.br/file/ProgOO/Card_Activ.png?disp=inline", self.cena)
        self.cena.vai()
        
    def randomize_cards(self):
        pass
    
        


if __name__ == "__main__":
    Game().crate_5x5_cards()