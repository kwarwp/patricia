# patricia.delta.juliete.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""Jogo da memória, 
        projeto Delta


Changelog
---------
.. versionadded::    20.07
       Grid 2x4.

"""
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
from delta.golf import Game2x5
import random
import time

__version__ = "20.07"
__author__ = "Paulo Assumpção"

__version__ = "20.07.01"
__author__ = "Emanuelle Simas"

IMG_CARD_FACE_DOWN = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline"
IMG_CARD_1 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline"
IMG_CARD_2 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Linux.png?disp=inline"
IMG_CARD_3 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Gitlab.png?disp=inline"
IMG_CARD_4 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Activ.png?disp=inline"
#IMG_CARD_5 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_github.png?disp=inline"

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
        self.pos_x = 50 + self.position[0] * IMG_WIDTH
        self.pos_y = 50 + self.position[1] * IMG_HEIGHT
        self.card = Elemento(IMG_CARD_FACE_DOWN, tit=self.name, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.card.elt.bind("click", self.turnUp)
        self.removed = False
        
    def turnUp(self, env=None):
        self.card = Elemento(self.image, tit=self.name, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.faceDown = False 
        self.card.elt.bind("click", self.turnDown)
        self.rule(self)
        
    def turnDown(self, env=None):
        self.card = Elemento(IMG_CARD_FACE_DOWN, tit=self.name, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.faceDown = True
        self.card.elt.bind("click", self.turnUp)
        
        
class Game2x4:
    # referência para o Elemento
    previous_selected_card = None
    
    cena = Cena()
    
    def vai(self): 
        self.create_2x4_cards()
        
    
    def create_2x4_cards(self):
        """ 
            matrix 2x4:
            1A 1B 2A 2B | [0][0] [0][1] [0][2] [0][3] [0][4]|
            3A 3B 4A 4B | [1][0] [1][1] [1][2] [1][3] [1][4]|
            list_cards =  [(0,0), (1,0), (2,0), (3,0), (4,0), (0,1), (1,1), (2,1),(3,1),(4,1)]
        """
        list_cards = self.shuffle_cards()
        
        list_objects = [ Card("PyCharm", IMG_CARD_1, list_cards[0], Game2x4.cena, Game2x4.rule), 
            Card("PyCharm", IMG_CARD_1, list_cards[1], Game2x4.cena, Game2x4.rule),
            Card("Linux", IMG_CARD_2, list_cards[2], Game2x4.cena, Game2x4.rule),
            Card("Linux", IMG_CARD_2, list_cards[3], Game2x4.cena, Game2x4.rule),
            Card("GitLab", IMG_CARD_3, list_cards[4], Game2x4.cena, Game2x4.rule),
            Card("GitLab", IMG_CARD_3, list_cards[5], Game2x4.cena, Game2x4.rule),
            Card("GitHub", IMG_CARD_4, list_cards[6], Game2x4.cena, Game2x4.rule),
            Card("GitHub", IMG_CARD_4, list_cards[7], Game2x4.cena, Game2x4.rule),
            ]
        
        Game2x4.cena.vai()

    @staticmethod
    def rule(selected_card):
    
        # abortar se o clique ocorrer sobre a mesma carta
        if Game2x4.previous_selected_card == selected_card:
            return
        
        # tem um par selecionado?
        if Game2x4.previous_selected_card is None:
            # primeira carta selecionada
            Game2x4.previous_selected_card = selected_card
            # desabilita o clique sobre carta virada
            Game2x4.previous_selected_card.card.elt.unbind("click")
            return
        
        # Não acertou
        if Game2x4.previous_selected_card.name != selected_card.name:            
            # reabilita a ação o clique e vira a carta 1 para baixo
            Game2x4.previous_selected_card.card.elt.bind("click", Game2x4.previous_selected_card.turnUp)
            Game2x4.previous_selected_card.turnDown()
            
            # reabilita a ação do clique e vira a carta 2 para baixo
            selected_card.card.elt.bind("click", selected_card.turnUp)
            
            Texto(Game2x4.cena, "Opa!", "Errou!!!").vai()
            
            # Aqui tem q esperar pelo menos 3 segundos, como fazer? (sleep, não funciona)
            
            selected_card.turnDown()
            Game2x4.previous_selected_card = None
            
        # acertou 
        else:
            # desabilita o clique sobre as cartas acertadas
            Game2x4.previous_selected_card = None
            Game2x4.verifyingGameOver()
            selected_card.card.elt.unbind("click")
            Texto(Game2x4.cena, "Acertou!!!").vai()
        

    @staticmethod  
    def verifyingGameOver():
        for object in list_objects:
            if object.faceDown == True:
                return     
        Game2x5.vai()
        
    def shuffle_cards(self):   
        list_cards =  [(0,0), (1,0), (2,0),(3,0),(0,1), (1,1), (2,1),(3,1)] #organiza as cartas em [coluna][linha]
                                                 
        random.shuffle(list_cards)
        return list_cards
        

if __name__ == "__main__":
    Game2x4().vai()