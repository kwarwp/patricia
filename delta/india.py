# patricia.delta.india.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo da Memória, 3x4.
..codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    20.07.01
        - 

"""
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
#from delta.hotel import Game  
import random
import time

CARD_BAIXO = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline"
IMG_CARD_1 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline"
IMG_CARD_2 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Linux.png?disp=inline"
IMG_CARD_3 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Gitlab.png?disp=inline"
IMG_CARD_4 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Activ.png?disp=inline"
IMG_CARD_5 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_github.png?disp=inline"

IMG_WIDTH = 150
IMG_HEIGHT = 150

class Card:
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
        
        
class Tabuleiro():
    """ Jogo da Memória para entendimento da POO
       
        :param dimensao: Resgata o número de linhas e colunas para gerar o tamanho da matriz do game
    """
    n_linhas = None
    n_colunas = None
    
    def __init__(self, dimensao=(l,c):
        self.lado, self.linha, self.coluna
        self.c = n_colunas <= 5
        self.dimensao = dim
        
    def gera_tabu():
        pass
        
    def regra():
       pass

if __name__ == "__main__":
    Tabuleiro().vai()