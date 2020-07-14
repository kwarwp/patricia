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

IMG_CARD_1 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline"
IMG_CARD_2 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Linux.png?disp=inline"
IMG_CARD_3 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Gitlab.png?disp=inline"
IMG_CARD_4 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_github.png?disp=inline"
IMG_CARD_5 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Activ.png?disp=inline"

class Card():
    def __init__(self, image,cena):
        self.image = image
        self.faceDown = True
        self.imageFaceDown = Elemento("http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline", cena=cena)
        self.removed = False
        self.position = [0,0]
        
        
class Game:
    def crate_4x5_cards(self):
        self.cena = Cena()
        self.card1 = Card(IMG_CARD_1, self.cena)
        self.card2 = Card(IMG_CARD_2, self.cena)
        self.card3 = Card(IMG_CARD_3, self.cena)
        self.card4 = Card(IMG_CARD_4, self.cena)
        self.card5 = Card(IMG_CARD_5, self.cena)
        self.cena.vai()
        
    def randomize_cards(self):
        pass
    
    def create_grid(self, grid_size):
        for row_num in range(grid_size):
            new_row = self.create_row(row_num, grid_size)
            self.grid.append(new_row)
        
    def rederize_cards(self):
        pass


if __name__ == "__main__":
    Game().crate_4x5_cards()
    print(teste)