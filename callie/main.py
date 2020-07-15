# patricia.callie.main.py
# Rio de Janeiro, 9 de junho de 2020
    
     ''' Tentativa de implementação do vira e desvira carta
            para o aplicativo proposto no curso ProgOO.
            
                     Grupo Delta
      '''
from _spy.vitollino.main import Cena, Elemento, STYLE, ESTYLE
__version__ = "20.07"
__author__= 'Emanuelle Simas'

STYLE["width"] = 600

TABULEIRO = "https://activufrj.nce.ufrj.br/file/ProgOO/TAB_VAZIO.png"
CARTA = "https://activufrj.nce.ufrj.br/file/ProgOO/Card_Activ.png"
CARTA2 = "https://activufrj.nce.ufrj.br/file/ProgOO/Card_github.png"
CARTA3 = "https://activufrj.nce.ufrj.br/file/ProgOO/Card_Gitlab.png"
#PosicaoX= (width_inicial+8)*coluna  (8+145)*1=153/ (145+8)*2=306
#Posicaoy=(heigth_inicial+8)*linha
class Jogo:
    """ Representa apenas o tabuleiro do jogo """
    def __init__(self):
        """ Mostra o tabuleiro """
        self.tab = Cena(TABULEIRO)
        self.carta = Elemento(CARTA, x=2, y=5,w=145,h=190, cena=self.tab)
        self.carta2 = Elemento(CARTA2, x=153, y=5, w=145,h=190,cena=self.tab)
        self.carta3 = Elemento(CARTA3, x=2, y=203,w=145,h=190, cena=self.tab)
        ''' Sendo o Width da cena 600, o melhor tamanho 
                            para a carta é w=145 e h-190'''

    def vai(self):
        """ Mostra a cena do tabuleiro """
        self.tab.vai()
        self.carta.vai()
        self.carta2.vai
        #Cena(CENA_CALCADA).vai()
    
if __name__ == "__main__":
    Jogo().vai()

    