"""   Implementação do mapa no Kwarwp

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

.. version:: 20.01.1

"""
from _spy.vitollino.main import Jogo, STYLE

#largura e altura, respectivamente
STYLE["width"] = 600
STYLE["height"] = "500px"

MAPA_INICIO = """
@....&
......
......
.#.^..
"""


class Kwarwp():
    """ Jogo para ensino de programação.

        :param vitollino: Empacota o engenho de jogo Vitollino.
    """
    
    """O GLIFOS corresponde ao dicionário que guarda a imagem dos elementos"""
    GLIFOS = {"&": "https://i.imgur.com/dZQ8liT.jpg",  # OCA ⛺
             "^": "https://imgur.com/8jMuupz.png",  # INDIO 
             "%" : "https://i.imgur.com/uwYPNlz.png", #CERCA 
             ".": "https://i.imgur.com/npb9Oej.png",  # VAZIO 
             "_": "https://i.imgur.com/sGoKfvs.jpg",  # SOLO 
             "#": "https://imgur.com/ldI7IbK.png",  # TORA 
             "@": "https://imgur.com/tLLVjfN.png",  # PICHE 
             "~": "https://i.imgur.com/UAETaiP.gif",  # CEU 
             "*": "https://i.imgur.com/PfodQmT.gif"  # SOL ☀
               }

    def __init__(self, vitollino=None, mapa = MAPA_INICIO, medidas = {}):
        self.v = vitollino()
        """Gera uma matriz de acordo com a quantidade de elementos no dicionário"""
        mapa = mapa.split()
        """ Largura da casa da arena dos desafios, número de colunas no mapa
          
           .. note::
              Tente aplicar o seguinte script: > MAPA_INICIO = X 
              > y = x.split() > z = len(y[0])  > print(x,y,z)   
        """
        self.lado, self.col = 100, len(mapa[0])
        """ Chama cena em cria() se há a importação do vitollino"""
        self.cena = self.cria(mapa=mapa) if vitollino else None
        
    
    def cria(self, mapa=" "):
        """ Cria o ambiente de programação Kwarwp.
            
            :param mapa: Texto representando o mapa do desafio
            
            :class Jogo: Este desafio herda parâmetros da classe Elemento
            :param w: Largura em pixels do elemento na cena
            :param h: Altura em pixels do elemento na cena
            :param x: Posição x, na horizontal a partir da esquerda do elemento na cena
            :param y: Posição y, na vertical a partir do topo do elemento na cena
        """
        lado = self.lado #lado = 100
        """ self.col acima pode ser chamado col agora"""
        col = self.col
        cena = self.v.c(self.GLIFOS["_"])
        """ O céu recebe como índices de largura o lado * n° colunas, logo, se o mapa for alterado, o comprimento
            do céu também será.
        """
        ceu = self.v.a(self.GLIFOS["~"], W=lado*col, h=lado, x=0,y=0, cena=cena)
        sol = self.v.a(self.GLIFOS["*"], w=60, h=60, x=0, y=40,cena=cena)
        
        [self.cria_elemento( x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)]
        cena.vai()
        return cena
        
    def cria_elemento(self, x, y, cena):
        lado = self.lado
        return self.v.a(self.GLIFOS[imagem], w=lado, h=lado, x=i*lado, y=j*lado+lado, cena=cena)
    
if __name__ == "__main__":
    Kwarwp(Jogo) 