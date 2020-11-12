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
    def __init__(self, name, image, position, cena):
        self.name = name
        self.cena = cena
        self.image = image
        self.faceDown = True
        self.position = position
        self.pos_x = 50 + self.position[0] * IMG_WIDTH
        self.pos_y = 50 + self.position[1] * IMG_HEIGHT
        self.card = Elemento(IMG_CARD_FACE_DOWN, tit=self.name, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.card.elt.bind("click", self.turnUp)
        #self.removed = False
        
    def turnUp(self, env=None):
        self.card = Elemento(self.image, tit=self.name, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.faceDown = False 
        self.card.elt.bind("click", self.turnDown) # DIZ QUE AO CLICAR NA CARTA ELA VIRA PRA BAIXO
        
    def turnDown(self, env=None):
        self.card = Elemento(IMG_CARD_FACE_DOWN, tit=self.name, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.faceDown = True
        self.card.elt.bind("click", self.turnUp) # DIZ QUE AO CLICAR ELA DEVE VIRAR PRA CIMA
        
        
class Tabuleiro:
    """ Contém uma matriz de casas.
 
    :param matriz: Uma tupla com número de colunas e linhas - default (2, 2).
    """
        
    def __init__(self, matriz = (2,2)):
        _col, _lin = matriz
        self.tabuleiro = [Casa(self, (col,lin)) for col in range(_col) for lin in range(_lin)]
        
    def monta(self,imagem,casa):
        _col, _lin = casa
        _casa = self.tabuleiro[_col][_lin]
        _casa.joga(tipo) # coloca o tipo de pino no local
        
class Casa:
    """ Local onde se pode colocar um pino.
        :param tabuleiro: a referencia do tabuleiro.
        :param posicao: Uma tupla com a ordem da coluna e da linha.
    """   
    cena = Cena() 
    
    CARD_LIST = [self.card1a = Card("PyCharm", IMG_CARD_1, list_cards[0], Tabuleiro.cena),
                 self.card1b = Card("PyCharm", IMG_CARD_1, list_cards[1], Tabuleiro.cena),
                 self.card2a = Card("Linux", IMG_CARD_2, list_cards[2], Tabuleiro.cena),
                 self.card2b = Card("Linux", IMG_CARD_2, list_cards[3], Tabuleiro.cena),
                 self.card3a = Card("GitLab", IMG_CARD_3, list_cards[4], Tabuleiro.cena),
                 self.card3b = Card("GitLab", IMG_CARD_3, list_cards[5], Tabuleiro.cena),
                 self.card4a = Card("GitHub", IMG_CARD_4, list_cards[6], Tabuleiro.cena),
                 self.card4b = Card("GitHub", IMG_CARD_4, list_cards[7], Tabuleiro.cena),
                 self.card5a = Card("Activ", IMG_CARD_5, list_cards[8], Tabuleiro.cena),
                 self.card5b = Card("Activ", IMG_CARD_5, list_cards[9], Tabuleiro.cena)]
                 
    def __init__(self, tabuleiro, posicao):
        self.tabuleiro, self.posicao = tabuleiro, posicao
        self.carta = None

    def joga(self, tipo):
        """ Coloca o pino de um tipo nesta casa.
            :param tipo: tipo do pino que será colocado.
        """         
        self.pino = Card().self.card
        
    def __repr__(self):
        return str(self.pino)
        
def Main():

    jogo = Tabuleiro()
    _col, _lin = (3, 3)
    casas = [(col, lin)  for col in range(_col) for lin in range(_lin)]
    tipo = True
    while casas:
        perg_lin = int(input("Em qual linha coloco a peça?"))
        perg_col = int(input("Em qual coluna  coloco a peça?"))
        jogo.joga(tipo,(perg_lin,perg_col))
        tipo = not tipo
        print(jogo)

        

if __name__ == "__main__":
    Main().vai()