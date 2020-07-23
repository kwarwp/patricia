# patricia.delta.golf.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo da Memória.

.. codeauthor:: Paulo Assumpção <paulo.assump@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Grid 2x5 de cartões do jogo da memória
        shuffle das cartas
        bind do click sobre o botão
        regra do jogo

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

"""
Classe responsável pelo desenho das cartas na cena
"""
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
        
    """
     Desenha a imagem da carta quando ela está virada para cima
    """
    def turnUp(self, env=None):
        self.card = Elemento(self.image, tit=self.name, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.faceDown = False 
        self.card.elt.bind("click", self.turnDown)
        self.rule(self)
    
    """
     Desenha a imagem da carta quando ela está virada para baixo
    """
    def turnDown(self, env=None):
        self.card = Elemento(IMG_CARD_FACE_DOWN, tit=self.name, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.faceDown = True
        self.card.elt.bind("click", self.turnUp)
        
"""
   Classe que mistura as caras, organiza na forma de matriz, e define as regras do jogo
"""       
class Game:
    # referência para o Elemento
    previous_selected_card = None
    
    cena = Cena()
    
    def vai(self): 
        self.create_2x5_cards()
    
    def create_2x5_cards(self):
         
        #    matrix 2x5:
        #    1A 1B 2A 2B 3A
        #    3B 4A 4B 5A 5B
        list_cards = self.shuffle_cards()
        
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

    """
       Estabelecendo as reggras do jogo, ou seja, verificar se as cartas são iguais, virar as cartas,...
    """
    # vou criar um método estático para a regrado do Jogo
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
        
        #Vamos gastar um tempo aqui
        while(x<10000):
            x=x+1
        
        # Não acertou
        if Game.previous_selected_card.name != selected_card.name:            
            # reabilita a ação o clique e vira a carta 1 para baixo
            Game.previous_selected_card.card.elt.bind("click", Game.previous_selected_card.turnUp)
            Game.previous_selected_card.turnDown()
            
            # reabilita a ação do clique e vira a carta 2 para baixo
            selected_card.card.elt.bind("click", selected_card.turnUp)
            selected_card.turnDown()
            Texto(Game.cena, "Errou!!!").vai()
            Game.previous_selected_card = None
            
        # acertou 
        else:
            # desabilita o clique sobre as cartas acertadas
            Game.previous_selected_card = None
            selected_card.card.elt.unbind("click")
            Texto(Game.cena, "Acertou!!!").vai()
        

    def shuffle_cards(self):   
        list_cards =  [(0,0), (1,0), (2,0), (3,0), (4,0), (0,1), (1,1), (2,1), (3,1), (4,1)]
        random.shuffle(list_cards)
        return list_cards
        

if __name__ == "__main__":
    Game().vai()