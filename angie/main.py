# patricia.angie.main.py
_author_ = "Monica"

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document # importa o DOM para atribuir o evento de teclado
#from grace.main import Praia

class Eventos:
    """ Associa um evento a uma imagem e captura eventos de teclado. """
    CENA_COZINHA = "https://www.decorfacil.com/wp-content/uploads/2018/03/20180311tons-de-rosa-03.jpg"
    CENA_ESCRITORIO = "https://www.decorfacil.com/wp-content/uploads/2018/03/20180311tons-de-rosa-05.jpg"
    CENA_PLANTA = "https://w7.pngwing.com/pngs/38/713/png-transparent-floor-plan-design-plan-media-schematic.png"
    
    BONECO = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Prick%C3%A4tarpucken.svg/200px-Prick%C3%A4tarpucken.svg.png"
    DARK_SIDE = "https://i.imgur.com/BKitDgi.png"
    
    #tamanho da cena
    STYLE["width"] = 1000
    STYLE["height"] = 500

    def __init__(self):
        self.ambiente = Cena(self.CENA_PLANTA)
        self.boneco = Elemento(self.BONECO, , x=100, y=200, cena=self.ambiente)
        #self.dark_side = Elemento(self.DARK_SIDE, , x=100, y=100, cena=self.ambiente)
        #self.dark_side.o = 0  # faz a opacidade virar zero, não mostra o letreiro
        document.bind("keydown", self.anda_boneco)  # captura o evento de teclado
        
        #self.boneco.elt.bind("mouseover", self.ve_dark)  # usa o evento para mostrar "dark side"
        #self.boneco.elt.bind("mouseout", self.ve_dark)  # usa o mesmo evento para ocultar "dark side"
        #self.muda = 1
        
    def vai(self):
        """ mostra a cena da planta da casa. """
        self.ambiente.vai()
        
    def anda_boneco(self, ev=None):
        """" Faz o boneco caminhar com a cptura das setas. 
            :param ev: estrutura enviad pelo evento onde se recupera informações.
        """
        key = ev.keyCode # recupera o código da tecla enviada no evento
        
        # os códigos 37 e 38 são a seta para esquerda e para direita
        # se não for nenhum deles, anda zero
        if key in [37, 39]:
            key = key - 38 
            self.boneco.x += key # muda a posição de mais um ou menos um
        elif key in [38, 40]:
            key = key - 39  
            self.boneco.y += key # muda a posição de mais um ou menos um
        else: 
            0
        #se o elemento atingiu uma porta, muda para a próxima cena
        if self.boneco.x = 500 and self.boneco.y = 500:
            self.boneco.x = 100
        #    self.boneco.y = 100
        
        #se atingiu o bau, ganhou o jogo.
        
    def ve_dark(self, ev=None):
        """" Faz o letreiro mostrar ou ocultar quando se passa o mouse no banhista. 
        
            :param ev: estrutura enviad pelo evento onde se recupera informações.
        """
        self.dark_side.o = self.muda  # muda a opacidade do letreiro
        self.muda = abs(self.muda - 1)  # chaveia para na próxima chamada inverter
        
        
        
if __name__ == "__main__":
    Eventos().vai()
    
    
#

#from _spy.vitollino.main import Cena, Elemento, STYLE

#from grace.main import Praia
#
#cena_praia = "https://lirp-cdn.multiscreensite.com/79bbfd96/dms3rep/multi/opt/Sem-t%C3%ADtulo-1-373ce17d-1920w.jpg"
#BANHISTA = "data:image/jpeg;base64,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"
#STYLE["width"] = 500

#class Calcada:

#	""" Representa a cena da calcada """
#	def __init__(self):
#		"""" Mostra a cena da praia """
#		self.cena = Cena(cena_praia, direita=Praia())
#		self.banhista = Elemento(BANHISTA, x=100, y=200, cena=self.cena)
        
#	def vai(self):
#		"""" Mostra a cena da praia """
#		self.cena.vai()
        #Cena(cena_praia).vai()

#if __name__ == "__main__":
#	Calcada().vai()


