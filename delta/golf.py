# patricia.delta.golf.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo da Memória.

.. codeauthor:: Paulo Assumpção <paulo.assump@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""

from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
import random

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
    
        self.cena = cena
        self.image = image
        self.faceDown = True
        self.position = position
        self.pos_x = 50 + self.position[0]*IMG_WIDTH
        self.pos_y = 50 + self.position[1]*IMG_HEIGHT
        self.card = Elemento(IMG_CARD_FACE_DOWN, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.card.elt.bind("click", self.turn)
        self.removed = False
        
    def turn(self, ev=None):
        self.card =Elemento(self.image, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.cena.vai()
        
        # para teste
        self.nomeTexto = Texto(self.card, self.image)
        self.nomeTexto.vai()
        
        
class Game:

    def vai(self): 
        self.create_2x5_cards()
    
    def create_2x5_cards(self):
    
        """ 
            matrix 2x5:
            1A 1B 2A 2B 3A
            3B 4A 4B 5A 5B
        """
        self.cena = Cena()
        list_cards=self.shuffle_cards()
        
        self.card1a = Card(IMG_CARD_1, list_cards[0], self.cena)
        self.card1b = Card(IMG_CARD_1, list_cards[1], self.cena)
        
        self.card2a = Card(IMG_CARD_2, list_cards[2], self.cena)
        self.card2b = Card(IMG_CARD_2, list_cards[3], self.cena)
        
        self.card3a = Card(IMG_CARD_3, list_cards[4], self.cena)
        self.card3b = Card(IMG_CARD_3, list_cards[5], self.cena)
        
        self.card4a = Card(IMG_CARD_4, list_cards[6], self.cena)
        self.card4b = Card(IMG_CARD_4, list_cards[7], self.cena)
        
        self.card5a = Card(IMG_CARD_5, list_cards[8], self.cena)
        self.card5b = Card(IMG_CARD_5, list_cards[9], self.cena)
        self.cena.vai()
        
    def shuffle_cards(self):
        
        list_cards =  [(0,0), (1,0), (2,0), (3,0), (4,0), (0,1), (1,1), (2,1), (3,1), (4,1)]
        random.shuffle(list_cards)
        return list_cards
        
    
    def create_grid(self, grid_size):
        for row_num in range(grid_size):
            new_row = self.create_row(row_num, grid_size)
            self.grid.append(new_row)
        
    def rederize_cards(self):
        pass


if __name__ == "__main__":
    Game().vai()