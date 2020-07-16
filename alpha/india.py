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
        Contador adicionado para gerar as seguintes fases e posiçoes iniciais em função da linha da matriz
        

"""

#FALTA - melhorar o código: criar as classes, funções, passar parametros
#FALTA - Mapear os pontos dos ambientes (x e Y) para mudar para a cena correta
#FALTA - VErifica se esta na cena correta e se chegou no baú do tesouro

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document # importa o DOM para atribuir o evento de teclado

cont = 0 #contador index da matriz

class Eventos:
    """ Associa um evento a uma imagem e captura eventos de teclado. """
    CENA_corredor_1 = link1 = "https://i.imgur.com/L71ZV6Z.png"
    
    
    BONECO = "https://i.imgur.com/k63kwfa.png"


    STYLE["width"] = 640 #tamanho da cena
    
    def __init__(self):
        #self.x1 = 100
        #self.y1 = 40
        self.ambiente = Cena(self.CENA_corredor_1)
        self.boneco = Elemento(self.BONECO, x=100, y=200, cena=self.ambiente)
        document.bind("keydown", self.anda_boneco)  # captura o evento de teclado
           
    def vai(self):
        """ mostra corredor do labirinto """
        self.ambiente.vai()
    
    def anda_boneco(self, ev=None):
        link2 = "https://i.imgur.com/5Qno2fs.png"
        matrizFase = [[link2,60,300],     #matrizFase = [[local_imagem_fase, x_inicial, y_inicial]...]
                      ["https://i.imgur.com/gZ5wc0h.png",450,50],
                      ["https://i.imgur.com/xI8i7Nc.png",50,430],
                      ["https://i.imgur.com/GLVctqb.png",200,50]]
                       
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
            global cont #contador estanciado fora do def para gerar a linha a ser lida na matrizFase
            self.ambiente = Cena(self.link2) #lê a cena que está descrita na primeira coluna da matriz
            STYLE["width"] = 640
            #self.x2 = 100#int(matrizFase[cont][1]) #posição x_inicial da fase, descrita na matriz pela segunda coluna
            #self.y2 = 100#int(matrizFase[cont][2]) #posição y_inicial da fase descita pela terceira coluna
            
            self.boneco = Elemento(self.BONECO, x=100, y=200, cena=self.ambiente)
            self.boneco.x = 100
            self.boneco.y = 100
            self.ambiente.vai()
            cont = cont + 1
            if cont > 3: #Regulador do contador. Precisa alterar a programação para voltar a fase em um portal de retorno
                cont = 0
            
        #se atingiu o bau, ganhou o jogo.
        # FALTA se estiver na cena certa e na posição certa, avisa que ganhou o jogo
        
if __name__ == "__main__":
    Eventos().vai()
    
