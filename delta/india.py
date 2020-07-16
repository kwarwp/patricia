# patricia.delta.india.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo da Memória, 3x4.
..codeauthor:: Paulo Assumpção <>
.. sub-codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    20.07.01
        Transforma o tabuleiro 2x5 em 2x4

"""
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
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
        
        
class Game:
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
        
        self.card1a = Card("PyCharm", IMG_CARD_1, list_cards[0], Game.cena, Game.rule)
        self.card1b = Card("PyCharm", IMG_CARD_1, list_cards[1], Game.cena, Game.rule)
        
        self.card2a = Card("Linux", IMG_CARD_2, list_cards[2], Game.cena, Game.rule)
        self.card2b = Card("Linux", IMG_CARD_2, list_cards[3], Game.cena, Game.rule)
        
        self.card3a = Card("GitLab", IMG_CARD_3, list_cards[4], Game.cena, Game.rule)
        self.card3b = Card("GitLab", IMG_CARD_3, list_cards[5], Game.cena, Game.rule)
        
        #self.card4a = Card("Activ", IMG_CARD_4, list_cards[6], Game.cena, Game.rule)
        #self.card4b = Card("Activ", IMG_CARD_4, list_cards[7], Game.cena, Game.rule)
        
        #self.card5a = Card("Activ", IMG_CARD_5, list_cards[8], Game.cena, Game.rule)
        #self.card5b = Card("Activ", IMG_CARD_5, list_cards[9], Game.cena, Game.rule)
        
        Game.cena.vai()

    @staticmethod
    def rule(selected_card):
    
        # abortar se o clique ocorrer sobre a mesma carta
        if Game.previous_selected_card == selected_card:
            return
        
        # tem um par selecionado?
        if Game.previous_selected_card is None:
            # primeira carta selecionada
            Game.previous_selected_card = selected_card
            # desabilita o clique sobre carta virada
            Game.previous_selected_card.card.elt.unbind("click")
            return
        
        # Não acertou
        if Game.previous_selected_card.name != selected_card.name:            
            # reabilita a ação o clique e vira a carta 1 para baixo
            Game.previous_selected_card.card.elt.bind("click", Game.previous_selected_card.turnUp)
            #Game.previous_selected_card.turnDown()
            
            # reabilita a ação do clique e vira a carta 2 para baixo
            selected_card.card.elt.bind("click", selected_card.turnUp)
            selected_card.turndown()
            #Texto(Game.cena, "Opa!", "Errou!!!").vai()
            
            # Aqui tem q esperar pelo menos 3 segundos, como fazer? (sleep, não funciona)
            
            Game.previous_selected_card.turnDown()
            Game.previous_selected_card = None
            
        # acertou 
        else:
            # desabilita o clique sobre as cartas acertadas
            Game.previous_selected_card = None
            selected_card.card.elt.unbind("click")
            #Texto(Game.cena, "Acertou!!!").vai()
        

    def shuffle_cards(self):   
        list_cards =  [(0,0), (1,0), (2,0),(0,1), (1,1), (2,1)] #organiza as cartas em [coluna][linha]
                                                 
        random.shuffle(list_cards)
        return list_cards
        

if __name__ == "__main__":
    Game().vai()