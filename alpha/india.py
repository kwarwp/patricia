# patricia.alpha.india.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""Jogo de Labirinto com cenas. 
   
   Calabouço de Barro.

.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

Classe neste módulo:

    :py:class:`Eventos` Gera a cena, personagem e a movimentação

Changelog
---------
.. versionadded::    20.07

   Criando a lógica do jogo e o layout das fases.
        
   Contador adicionado para gerar as seguintes fases em função da linha da matriz.
        
   Contador adicionado para gerar as seguintes posições iniciais em função do índice da lista.        
"""

#FALTA - melhorar o código: criar as classes, funções, passar parametros
#FALTA - VErifica se esta na cena correta e se chegou no baú do tesouro

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document # importa o DOM para atribuir o evento de teclado

cont = 0 #contador index da matriz

class Eventos:
    """ Associa um evento a uma imagem
    """
    CENA_corredor_1 = "https://i.imgur.com/L71ZV6Z.png"
    CENA_corredor_2 = "https://i.imgur.com/5Qno2fs.png"
    CENA_corredor_3 = "https://i.imgur.com/gZ5wc0h.png"
    CENA_corredor_4 = "https://i.imgur.com/xI8i7Nc.png"
    CENA_corredor_5 = "https://i.imgur.com/GLVctqb.png"
    
    listaFase = [CENA_corredor_2,    #listaFase = [local_imagem_fase,...]
                 CENA_corredor_3,
                 CENA_corredor_4,
                 CENA_corredor_5,]
              
    BONECO = "https://i.imgur.com/k63kwfa.png"


    STYLE["width"] = 640 #tamanho da cena
    
    def __init__(self):        
        """Gera o início do jogo com a posição do personagem e a primeira cena

           :return: self.boneco com parâmetros (personagem, poisção_x, posição_y, cenário)
        """
        self.x1 = 100
        self.y1 = 40
        self.ambiente = Cena(self.CENA_corredor_1)
        self.boneco = Elemento(self.BONECO, x=self.x1, y=self.y1, cena=self.ambiente)
        document.bind("keydown", self.anda_boneco)  # captura o evento de teclado
           
    def vai(self):
        """ :return: Cenário do labirinto.
        """
        self.ambiente.vai()
    
    def anda_boneco(self, ev=None):  
        matrizPosicaoInicial = [[60,280],     #matrizPosicaoInicial = [[x_inicial, y_inicial]...]
                                [450,50],
                                [50,430],
                                [200,50]]
                       
        """" Faz o boneco caminhar com a catura das setas. 
        
            :param ev: Importa evento de teclado através do browser.
            :retun: self.boneco.x como a posição x do personagem e self.boneco.y como a posição y
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
            
        #estudo da parede
            #if self.boneco.x <= 80
            
        """:if: O personagem atingiu uma porta, muda para a próxima cena
        """
        # FALTA mapear os pontos, criar função para passar parametros ou chamar outra classe
        #ideia de cria uma matriz com os pontos de localização do portal
        
        if self.boneco.x > 400 and self.boneco.y > 200:
            global cont #contador estanciado fora do def para gerar a linha a ser lida na lista/MAtriz
            self.ambiente = Cena(self.listaFase[cont]) #lê a cena que está descrita no primeiro ítem da lista
            STYLE["width"] = 640
            self.x2 = int(matrizPosicaoInicial[cont][0]) #posição x_inicial da fase, descrita na matriz pela primeira coluna
            self.y2 = int(matrizPosicaoInicial[cont][1]) #posição y_inicial da fase descita pela segunda coluna
            
            self.boneco = Elemento(self.BONECO, x=self.x2, y=self.y2, cena=self.ambiente)
            """:Contador: cont: Varia a cada momento que o *if* é satisfeito a ser utilizado em cada cenário e posicição   
               :param self.ambiente: Novos cenários das seguintes fases.
               :param self.x2: Posição x inicial das novas fases.
               :param self.y2: Posição y inicial das novas fases.
            """
            self.boneco.x = self.x2
            self.boneco.y = self.y2
            self.ambiente.vai()
            cont = cont + 1
            if cont > 3: #Regulador do contador. Precisa alterar a programação para voltar a fase em um portal de retorno
                cont = 0
            
        #se atingiu o bau, ganhou o jogo.
        # FALTA se estiver na cena certa e na posição certa, avisa que ganhou o jogo
        
if __name__ == "__main__":
    Eventos().vai()
    
