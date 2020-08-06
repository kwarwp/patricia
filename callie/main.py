# patricia.callie.main.py
# Rio de Janeiro, 5 de agosto de 2020
"""   Implementação do mapa no Kwarwp

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

.. version:: 20.01.1

"""
from _spy.vitollino.main import Jogo, STYLE
from collections import namedtuple as nt

#largura e altura, respectivamente
#STYLE["width"] = 700
#STYLE["height"] = "600px"

IMGUR = "https://i.imgur.com/"

Fab = nt("Fab", "objeto imagem")
        
fabrica ={"#": Fab(self.coisa, f"{IMGUR}uwYPNlz.png"), # CERCA
         "^": Fab(self.indio, f"{IMGUR}8jMuupz.png"), # INDIO
         ".": Fab(self.vazio, f"{IMGUR}npb9Oej.png"), #VAZIO
         "_": Fab(self.coisa, f"{IMGUR}sGoKfvs.jpg"), #SOLO
         "&": Fab(self.coisa, f"{IMGUR}dZQ8liT.jpg"), #OCA
         "@": Fab(self.coisa, f"{IMGUR}tLLVjfN.png"), #PICHE
         "*": Fab(self.coisa, f"{IMGUR}PfodQmT.gif"), #SOL
         "~": Fab(self.coisa, f"{IMGUR}UAETaiP.gif"), #CEU
         "|": Fab(self.coisa, f"{IMGUR}ldI7IbK.png")  # TORA 
         }

MAPA_INICIAL= """
             #######
             #..#..#
             #..@..&
             #..#..#
             #######
"""

class Indio():

    def __init__(self, imagem, x, y, cena):
        self.lado = lado = Kwarwp.LADO
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
    
class Kwarwp():
    """ Jogo para ensino de programação.

        :param vitollino: Empacota o engenho de jogo Vitollino.
        :param mapa: Texto representando o mapa do desafio
        :param medidas: Dicionário usado para redimensionar a tela
    """
    VITOLLINO = None
    """Referência estática para obter o engenho de jogo"""
    LADO = None
    """Referência estática para definir o lado do piso da casa"""

    def __init__(self, vitollino=None, mapa = MAPA_INICIAL, medidas = {}):
        Kwarwp.VITOLLINO = self.v = vitollino()
        # Notação anterior self.v = vitollino()
        """Transforma o texto matriz, explicitando o bloco de strings para cada linha."""
        self.mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas no mapa
        
           .. note::
              Tente aplicar o seguinte script: > MAPA_INICIO = X 
              > y = x.split() > z = len(y[0])  > print(x,y,z) 
              LEN(MAPA[0]) acessa o primeiro item indexado em zero, retornando sua 'quantidade'
              
        """
        self.lado, self.coluna, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        Kwarwp.LADO = self.lado
        w,h = self.coluna*self.lado, self.lin*self.lado
        self.taba = {}
        """Dicionário que a partir de coordenada (i,J) localiza um piso da taba"""
        medidas.update(width=w, height=f"{h}px")
        self.cena = self.cria(mapa=self.mapa) if vitollino else None

    def cria(self, mapa=""):
        
        mapa = mapa if mapa != "" else self.mapa

        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].imagem)
        ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena)
        
        self.taba = {(i, j): fabrica[imagem].objeto(
              fabrica[imagem].imagem, x=i*lado, y=j*lado+lado, cena=cena)
              for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
              
        cena.vai()
        return cena
    
    def coisa(self,imagem,x,y,cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        
    def indio(self, imagem,x,y,cena):
        lado = self.lado
        return Indio(imagem, x=x, y=y, cena=cena)



if __name__ == "__main__":
    Kwarwp(Jogo) 