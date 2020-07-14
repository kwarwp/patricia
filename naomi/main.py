# patricia.naomi.main.py
from _spy.vitollino.main import Cena, Elemento
from browser import document # importa o DOM para atribuir o evento de teclado

class Eventos:
    """ Associa um evento a uma imagem e captura eventos de teclado. """
    CENA_TABULEIRO = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline"
    CARTA_PYCHARM = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline"
    
    
    def __init__(self):
        self.calcada = Cena(self.CENA_TABULEIRO)
        self.banhista = Elemento(self.CARTA_PYCHARM, , x=100, y=200, cena=self.calcada)
        self.dark_side = Elemento(self.DARK_SIDE, , x=100, y=100, cena=self.calcada)
        self.dark_side.o = 0  # faz a opacidade virar zero, não mostra o letreiro
        document.bind("keydown", self.anda_banhista)  # captura o evento de teclado
        
        self.banhista.elt.bind("mouseover", self.ve_dark)  # usa o evento para mostrar "dark side"
        self.banhista.elt.bind("mouseout", self.ve_dark)  # usa o mesmo evento para ocultar "dark side"
        self.muda = 1
        
    def vai(self):
        """ mostra a cena da calçada. """
        self.calcada.vai()
        
    def anda_banhista(self, ev=None):
        """" Faz o banhista caminhar com a cptura das setas. 
        
            :param ev: estrutura enviad pelo evento onde se recupera informações.
        """
        key = ev.keyCode # recupera o código da tecla enviada no evento
        # os códigos 37 e 38 são a seta para esquerda e para direita
        # se não for nenhum deles, anda zero
        key = key - 38 if key in [37, 39] else 0
        self.banhista.x += key # muda a posição de mais um ou menos um
        
    def ve_dark(self, ev=None):
        """" Faz o letreiro mostrar ou ocultar quando se passa o mouse no banhista. 
        
            :param ev: estrutura enviad pelo evento onde se recupera informações.
        """
        self.dark_side.o = self.muda  # muda a opacidade do letreiro
        self.muda = abs(self.muda - 1)  # chaveia para na próxima chamada inverter
        
        
        
if __name__ == "__main__":
    Eventos().vai()