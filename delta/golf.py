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

IMG_CARD_FACE_DOWN = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline"
IMG_CARD_1 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline"
IMG_CARD_2 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Linux.png?disp=inline"
IMG_CARD_3 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Gitlab.png?disp=inline"
IMG_CARD_4 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_github.png?disp=inline"
IMG_CARD_5 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Activ.png?disp=inline"

IMG_WIDTH = 150
IMG_HEIGHT = 150


class Card():
    def __init__(self, image, position, cena):
    
        self.image = image
        self.faceDown = True
        self.position = position
        pos_x = 50 + self.position[0]*IMG_WIDTH
        pos_y = 50 + self.position[1]*IMG_HEIGHT
        if faceDown:
            Elemento(IMG_CARD_FACE_DOWN, x=pos_x, y=pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=cena)
        else: 
            Elemento(self.image, x=pos_x, y=pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=cena)
        self.removed = False
        
        
        
class Game:
    def create_2x5_cards(self):
    
        """ matrix 4x5
            1A 1B 2A 2B 3A
            3B 4A 4B 5A 5B
        """
        self.cena = Cena()
        self.card1a = Card(IMG_CARD_1, [0,0], self.cena)
        self.card1b = Card(IMG_CARD_1, [1,0], self.cena)
        
        self.card2a = Card(IMG_CARD_2, [2,0], self.cena, faceDown=False)
        self.card2b = Card(IMG_CARD_2, [3,0], self.cena)
        
        self.card3a = Card(IMG_CARD_3, [4,0], self.cena)
        self.card3b = Card(IMG_CARD_3, [0,1], self.cena)
        
        self.card4a = Card(IMG_CARD_4, [1,1], self.cena)
        self.card4b = Card(IMG_CARD_4, [2,1], self.cena)
        
        self.card5a = Card(IMG_CARD_5, [3,1], self.cena)
        self.card5b = Card(IMG_CARD_5, [4,1], self.cena)
        self.cena.vai()
        
    def randomize_cards(self, ):
        pass
    
    def create_grid(self, grid_size):
        for row_num in range(grid_size):
            new_row = self.create_row(row_num, grid_size)
            self.grid.append(new_row)
        
    def rederize_cards(self):
        pass


if __name__ == "__main__":
    Game().create_2x5_cards()