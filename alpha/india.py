# patricia.alpha.india.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" 
Projeto ALPHA - Jogo de Labirinto com cenas. 

Calabouço de Barro.

.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

Changelog
---------

Código alterado de Monica Novellino <monicanovellino@gmail.com>

.. versionadded::    20.07
        Adicionei 5 imagens iniciais do labirinto e alterei o pacman (podem criar outro peronagem)
        

"""

#FALTA - melhorar o código: criar as classes, funções, passar parametros
#FALTA - Mapear os pontos dos ambientes (x e Y) para mudar para a cena correta
#FALTA - VErifica se esta na cena correta e se chegou no baú do tesouro

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document # importa o DOM para atribuir o evento de teclado

class Eventos:
    """ Associa um evento a uma imagem e captura eventos de teclado. """
    CENA_corredor_1 = link1 = "https://i.imgur.com/L71ZV6Z.png"
    CENA_corredor_2 = link2 = "https://i.imgur.com/5Qno2fs.png"
    CENA_corredor_3 = link3 = "https://i.imgur.com/gZ5wc0h.png"
    CENA_corredor_4 = link4 = "https://i.imgur.com/xI8i7Nc.png"
    CENA_corredor_5 = link5 = "https://i.imgur.com/GLVctqb.png"
    
    BONECO = "https://i.imgur.com/k63kwfa.png"
    
    matrizMapaFase = [[link2],
                      [link3],
                      [link4],
                      [link5]]
    #tamanho da cena
    STYLE["width"] = 640
    
    def __init__(self):
        self.ambiente = Cena(self.CENA_corredor_1)
        self.boneco = Elemento(self.BONECO, , x=100, y=40, cena=self.ambiente)
        document.bind("keydown", self.anda_boneco)  # captura o evento de teclado
           
    def vai(self):
        """ mostra corredor do labirinto """
        self.ambiente.vai()
    
    def portal(self,x,y):
        self.ambiente = Cena(self.matrizMapaFase[0][0])
        STYLE["width"] = 640
        self.boneco = Elemento(self.BONECO, , x=int, y=int, cena=self.ambiente)
        self.boneco.x = 60
        self.boneco.y = 240
        self.ambiente.vai()
        self.portal(self.boneco.x,self.boneco.y)
    
    def anda_boneco(self, ev=None):
        """" Faz o boneco caminhar com a cptura das setas. 
            :param ev: estrutura enviad pelo evento onde se recupera informações.
        """
        key = ev.keyCode # recupera o código da tecla enviada no evento
        
        # os códigos 37 e 38 são a seta para esquerda e para direita
        # os códigos 39 e 40 são a seta para cima e para baixo
        if key in [37, 39]:
            key = (key - 38) * 5
            self.boneco.x += key # muda a posição de mais um ou menos um
        elif key in [38, 40]:
            key = (key - 39) * 5
            self.boneco.y += key # muda a posição de mais um ou menos um
        #se o elemento atingiu uma porta, muda para a próxima cena
        # FALTA mapear os pontos, criar função para passar parametros ou chamar outra classe
        #ideia de cria uma matriz com os pontos de localização do portal
        if self.boneco.x > 400 and self.boneco.y > 200:
            self.portal()
#            def portal(self,x,y):
 #               self.ambiente = Cena(self.matrizMapaFase[0][0])
  #              STYLE["width"] = 640
   #             self.boneco = Elemento(self.BONECO, , x=int, y=int, cena=self.ambiente)
    #            self.boneco.x = 60
     #           self.boneco.y = 240
      #          self.ambiente.vai()
       #         self.portal(self.boneco.x,self.boneco.y)
            
        #se atingiu o bau, ganhou o jogo.
        # FALTA se estiver na cena certa e na posição certa, avisa que ganhou o jogo
        
if __name__ == "__main__":
    Eventos().vai()
    