# patricia.callie.main.py
# Rio de Janeiro, 9 de junho de 2020
    

from _spy.vitollino.main import Cena, Elemento, STYLE, ESTYLE

__version__ = "20.07"
__author__= 'Emanuelle Simas'

''' Tentativa de implementação do vira e desvira carta
            para o aplicativo proposto no curso ProgOO.
            
                     Grupo Delta
'''
STYLE["width"] = 600

TABULEIRO = "https://activufrj.nce.ufrj.br/file/ProgOO/TAB_VAZIO.png"
CARTA = "https://activufrj.nce.ufrj.br/file/ProgOO/Card_Activ.png"
CARTA2 = "https://activufrj.nce.ufrj.br/file/ProgOO/Card_github.png"
VERSO = "https://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png"
#PosicaoX= (width_inicial+8)*coluna  (8+145)*1=153/ (145+8)*2=306
#Posicaoy=(heigth_inicial+8)*linha

class Jogo:
    """ Representa apenas o tabuleiro do jogo """
    def __init__(self):
        """ Mostra o tabuleiro
        Tentativa construção de tabuleiro com 2 pares
        """
        self.tab = Cena(TABULEIRO)
        
        self.verso = Elemento(VERSO, x=2, y=5,w=145,h=190, cena=self.tab)
        self.verso2 = Elemento(VERSO, x=153, y=5, w=145,h=190,cena=self.tab)
        self.verso3 = Elemento(VERSO, x=2, y=203,w=145,h=190, cena=self.tab)
        self.verso4 = Elemento(VERSO, x=153, y=203, w=145, h=190, cena=self.tab)
        
        ''' Sendo o Width da cena 600px, o melhor tamanho 
                            para a carta é w=145 e h-190'''
        
        def vira_carta(self,_=0):
            '''Troca a carta quando eu clico no verso
         '''
            vira = Elemento(CARTA,x=2, y=5,w=145,h=190, cena=self.tab)
            vira2 = Elemento(CARTA, x=153, y=5, w=145,h=190,cena=self.tab)
            vira3 = Elemento(CARTA3, x=2, y=203,w=145,h=190, cena=self.tab)
            vira4 = Elemento(CARTA3, x=153, y=203, w=145, h=190, cena=self.tab)
            lista_verso = (self.verso, self.verso2, self.verso3, self.verso4)
            possib = (vira, vira2, vira3,vira4)
            
            for i in lista_verso:
                
            
                
            
            #lista_carta=(self.carta, self.carta2,self.carta3, self.carta4)
            
        self.verso.vai= vira_carta
        self.verso2.vai=vira_carta
        self.verso3.vai=vira_carta
        self.verso.vai=vira_carta
            
    def vai(self):
        """ Mostra a cena do tabuleiro e versos"""
        self.tab.vai()
        self.verso.verso1.verso2.verso3.verso4.vai()
        self.vira_carta.vai()
        #self.carta.carta2.carta3.carta4.vai()
        
        #Cena(CENA_CALCADA).vai()
    
if __name__ == "__main__":
    Jogo().vai()

    