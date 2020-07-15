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
import random, time

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
    def __init__(self, name, image, position, cena, rule):
        self.rule = rule
        self.name = name
        self.cena = cena
        self.image = image
        self.faceDown = True
        self.position = position
        self.pos_x = 50 + self.position[0]*IMG_WIDTH
        self.pos_y = 50 + self.position[1]*IMG_HEIGHT
        self.card = Elemento(IMG_CARD_FACE_DOWN, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.card.elt.onclick = self.turnOn
        self.removed = False
        
    def turnOn(self, ev=None):
        self.card = Elemento(self.image, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.faceDown = False
        self.card.elt.bind("click", self.turnDown)
        self.rule(self)
        
    def turnDown(self, env=None):
        self.card = Elemento(IMG_CARD_FACE_DOWN, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.faceDown = True
        self.card.elt.bind("click", self.turnOn)

        
        
class Game:

    previous_selected_card = None
    cena = Cena()
    
    def vai(self): 
        self.create_2x5_cards()
    
    def create_2x5_cards(self):
    
        """ 
            matrix 2x5:
            1A 1B 2A 2B 3A
            3B 4A 4B 5A 5B
        """
        list_cards=self.shuffle_cards()
        
        self.card1a = Card("PyCharm", IMG_CARD_1, list_cards[0], Game.cena, Game.rule)
        self.card1b = Card("PyCharm", IMG_CARD_1, list_cards[1], Game.cena, Game.rule)
        
        self.card2a = Card("Linux", IMG_CARD_2, list_cards[2], Game.cena, Game.rule)
        self.card2b = Card("Linux", IMG_CARD_2, list_cards[3], Game.cena, Game.rule)
        
        self.card3a = Card("GitLab", IMG_CARD_3, list_cards[4], Game.cena, Game.rule)
        self.card3b = Card("GitLab", IMG_CARD_3, list_cards[5], Game.cena, Game.rule)
        
        self.card4a = Card("GitHub", IMG_CARD_4, list_cards[6], Game.cena, Game.rule)
        self.card4b = Card("GitHub", IMG_CARD_4, list_cards[7], Game.cena, Game.rule)
        
        self.card5a = Card("Activ", IMG_CARD_5, list_cards[8], Game.cena, Game.rule)
        self.card5b = Card("Activ", IMG_CARD_5, list_cards[9], Game.cena, Game.rule)
        
        Game.cena.vai()

    @staticmethod
    def rule(selected_card):
        # tem um par selecionado?
        if Game.previous_selected_card == None:
            Game.previous_selected_card = selected_card
            return
        
        # Não acertou
        if Game.previous_selected_card.name != selected_card.name:
            #Texto(Game.cena, "Errou!!!").vai()
            Game.previous_selected_card.turnDown()
            selected_card.turnDown()
            time.sleep(10)
        else: # acertou
            #Texto(Game.cena, "Acertou!!!").vai()
            Game.previous_selected_card.card.elt.onclick = None
            selected_card.card.elt.onclick = None
            Game.previous_selected_card = None
            
        Game.previous_selected_card = None


    def shuffle_cards(self):   
        list_cards =  [(0,0), (1,0), (2,0), (3,0), (4,0), (0,1), (1,1), (2,1), (3,1), (4,1)]
        random.shuffle(list_cards)
        return list_cards
        

if __name__ == "__main__":
    Game().vai()