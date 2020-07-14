# patricia.alpha.india.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""

















# patricia.alpha.hotel.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto ALPHA - Jogo de Labirinto com cenas.

.. codeauthor:: Monica Novellino <monicanovellino@gmail.com>

Changelog
---------
.. versionadded::    0.1
        - Planta da casa
        - Boneco andando com as setas

"""
#FALTA - melhorar o código: criar as classes, funções, passar parametros
#FALTA - Mapear os pontos dos ambientes (x e Y) para mudar para a cena correta
#FALTA - VErifica se esta na cena correta e se chegou no baú do tesouro

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document # importa o DOM para atribuir o evento de teclado

class Eventos:
    """ Associa um evento a uma imagem e captura eventos de teclado. """
    CENA_COZINHA = "https://i.imgur.com/fEcFvG5.png"
    CENA_ESCRITORIO = "https://i.imgur.com/fEcFvG5.png"
    CENA_PLANTA = "https://i.imgur.com/L71ZV6Z.png"
    
    BONECO = "https://i.imgur.com/k63kwfa.png"
    
    #tamanho da cena
    STYLE["width"] = 800
    
    def __init__(self):
        self.ambiente = Cena(self.CENA_PLANTA)
        self.boneco = Elemento(self.BONECO, , x=100, y=200, cena=self.ambiente)
        document.bind("keydown", self.anda_boneco)  # captura o evento de teclado
           
    def vai(self):
        """ mostra a cena da planta da casa. """
        self.ambiente.vai()
        
    def anda_boneco(self, ev=None):
        """" Faz o boneco caminhar com a cptura das setas. 
            :param ev: estrutura enviad pelo evento onde se recupera informações.
        """
        key = ev.keyCode # recupera o código da tecla enviada no evento
        
        # os códigos 37 e 38 são a seta para esquerda e para direita
        # os códigos 39 e 40 são a seta para cima e para baixo
        if key in [37, 39]:
            key = key - 38 
            self.boneco.x += key # muda a posição de mais um ou menos um
        elif key in [38, 40]:
            key = key - 39  
            self.boneco.y += key # muda a posição de mais um ou menos um
            
        #se o elemento atingiu uma porta, muda para a próxima cena
        # FALTA mapear os pontos, criar função para passar parametros ou chamar outra classe
        if self.boneco.x > 500 and self.boneco.y > 500:
            self.ambiente = Cena(self.CENA_COZINHA)
            STYLE["width"] = 500
            self.boneco = Elemento(self.BONECO, , x=100, y=200, cena=self.ambiente)
            self.boneco.x = 100
            self.boneco.y = 100
            self.ambiente.vai()
            
        #se atingiu o bau, ganhou o jogo.
        # FALTA se estiver na cena certa e na posição certa, avisa que ganhou o jogo
        
if __name__ == "__main__":
    Eventos().vai()
    