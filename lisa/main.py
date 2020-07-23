# patricia.lisa.main.py
__author__ = "Victória Regina Caruzo"
__version__ = "09.07.20"

from _spy.vitollino.main import Cena, Elemento, STYLE
from random import shuffle 
""" from grace.main import Praia """

__version__ = "1.0"
__author__ = "ECHO"
STYLE["width"] = 1150
STYLE["height"] = "620px"
TABULEIRO = "http://www.infcross.com.br/mestrado/tabuleiro.jpg"
BOTAO = "http://www.infcross.com.br/mestrado/botao3.jpg"
DADO1 = "http://www.infcross.com.br/mestrado/dado1.png"
DADO2 = "http://www.infcross.com.br/mestrado/dado2.png" 
DADO3 = "http://www.infcross.com.br/mestrado/dado3.png"
DADO4 = "http://www.infcross.com.br/mestrado/dado4.png"
DADO5 = "http://www.infcross.com.br/mestrado/dado5.png"
DADO6 = "http://www.infcross.com.br/mestrado/dado6.png"



class Tabuleiro:
    def vai(self):
        """ Mostra a cena do tabuleiro """
        Cena(TABULEIRO).vai()

class Jogo:
    """ Representa uma cena de tabuleiro com o botão """
    def __init__(self):
        """ Mostra o tabuleiro com o botão start"""
        self.cena = Cena(TABULEIRO, direita=Tabuleiro())
        self.start = Elemento(BOTAO, x=5, y=15, cena=self.cena)
        #Cena(CENA_JOGO).vai()
    def vai(self):
        """ Mostra o tabuleiro """
        self.cena.vai()
        #Cena(CENA_JOGO).vai()

class Dado:
    dados = [DADO1, DADO2, DADO3, DADO4, DADO5, DADO6]*5
    shuffle(dados)
    print ("Reshuffled list : ",  list)
    
    #def __init__(self, outra):
    
    
    
if __name__ == "__main__":
    Jogo().vai()