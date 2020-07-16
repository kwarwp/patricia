# patricia.kristen.main.py

from _spy.vitollino.main import Cena, Elemento, STYLE, Text
from browser import document # importa o DOM para atribuir o evento de teclado

cont = 0 #contador index da matriz

class Eventos:
    """ Associa um evento a uma imagem e captura eventos de teclado. """
    CENA_corredor_1 = link1 = "https://i.imgur.com/L71ZV6Z.png"
    CENA_corredor_2 = link2 = "https://i.imgur.com/5Qno2fs.png"
    CENA_corredor_3 = link3 = "https://i.imgur.com/gZ5wc0h.png"
    CENA_corredor_4 = link4 = "https://i.imgur.com/xI8i7Nc.png"
    CENA_corredor_5 = link5 = "https://i.imgur.com/GLVctqb.png"
    
    BONECO = "https://i.imgur.com/k63kwfa.png"
    
    
    matrizFase = [[link,(60,260),],     #matrizFase = [[local_imagem_fase, x_inicial, y_inicial]...]
                  [link3,450,50],
                  [link4,50,430],
                  [link5,200,50]]

    STYLE["width"] = 640 #tamanho da cena
    
    def __init__(self):
        self.ambiente = Cena(self.CENA_corredor_1)
        self.pos_x = 100
        self.pos_y = 40
        self.boneco = Elemento(self.BONECO, x=self.pos_x, y=self.pos_y, width, height, cena=self.ambiente)
        
        document.bind("keydown", self.anda_boneco)  # captura o evento de teclado
           
    def vai(self):
        """ mostra corredor do labirinto """
        self.ambiente.vai()
    
    def anda_boneco(self, ev=None):
    
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
            self.ambiente = Cena(self.matrizFase[cont][0]) #lê a cena que está descrita na primeira coluna da matriz
            STYLE["width"] = 640 
            self.pos_x = matrizFase[cont][1]
            self.pos_y = matrizFase[cont][2]
            #self.boneco = Elemento(self.BONECO, x=self.pos_x, y=self.pos_y, width, height, cena=self.ambiente)
            self.boneco = Elemento(self.BONECO, x=self.pos_x, y=self.pos_y, 80, 80, cena=self.ambiente)
            #self.boneco.x = 100#int(matrizFase[cont][1]) #posição x_inicial da fase, descrita na matriz pela segunda coluna
            #self.boneco.y = 100#int(matrizFase[cont][2]) #posição y_inicial da fase descita pela terceira coluna
            self.ambiente.vai()
            cont = cont + 1
            if cont > 3: #Regulador do contador. Precisa alterar a programação para voltar a fase em um portal de retorno
                cont = 0
            
        #se atingiu o bau, ganhou o jogo.
        # FALTA se estiver na cena certa e na posição certa, avisa que ganhou o jogo
        
if __name__ == "__main__":
    Eventos().vai()
    
