# patricia.naomi.main.py
from _spy.vitollino.main import Cena, Elemento
from browser import document # importa o DOM para atribuir o evento de teclado

class Eventos:
    """ Associa um evento a uma imagem e captura eventos de teclado. """
    CENA_TABULEIRO = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline"
    CENA_CARTA1= "http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline"
    CARTA_PYCHARM = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline"
    
    
    def __init__(self):
        self.tabuleiro = Cena(self.CENA_TABULEIRO)
        self.pycharm = Elemento(self.CARTA_PYCHARM, , x=100, y=200, cena=self.tabuleiro)
        self.pycharm=Elemento(self.CARTA_PYCHARM,,X=200,y=300,cena=self.tabuleiro)
        self.pycharm=Elemento(self.CARTA_PYCHARM,,X=300,y=400,cena=self.tabuleiro)
        self.pycharm=Elemento(self.CARTA_PYCHARM,,X=200,y=300,cena=self.tabuleiro)
        self.pycharm=Elemento(self.CARTA_PYCHARM,,X=200,y=300,cena=self.tabuleiro)
        
        
        
        
    def vai(self):
        """ mostra a cena da calçada. """
        self.tabuleiro.vai()
        
    
        
if __name__ == "__main__":
    Eventos().vai()