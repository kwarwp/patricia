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


MAPA_INICIAL= """
#########
#...##..#
#.@.#&^.#
#.#.##|.#
#.......#
#########
"""

class Indio():
    """ Cria estrutura índio que será chamada no"""
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
        """Transforma o texto matriz, explicitando o bloco de strings para cada linha."""
        self.mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas no mapa"""
        self.lado, self.coluna, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        Kwarwp.LADO = self.lado
        w,h = self.coluna*self.lado, self.lin*self.lado
        medidas.update(width=w, height=f"{h}px")
        #medidas = STYLE
        
        self.taba = {}
        """Dicionário que a partir de coordenada (i,J) localiza um piso da taba"""
        
        self.cena = self.cria(mapa=self.mapa) if vitollino else None

    def cria(self, mapa=""):
    
        IMGUR = "https://i.imgur.com/"
        Fab = nt("Fab", "objeto url")   
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
        
        mapa = mapa if mapa != "" else self.mapa

        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].url)
        ceu = self.v.a(fabrica["~"].url, w=lado*self.coluna, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(fabrica["*"].url, w=60, h=60, x=0, y=40, cena=cena)
        
        self.taba = {(i, j): fabrica[imagem].objeto(
              fabrica[imagem].url, x=i*lado, y=j*lado+lado, cena=cena)
              for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
              
        cena.vai()
        return cena
    
    def coisa(self,imagem,x,y,cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        
    def indio(self, imagem,x,y,cena):
        lado = self.lado
        return Indio(imagem, x=x, y=y, cena=cena)
        
    def vazio(self, imagem, x,y ,cena):
        lado = self.lado
        return Indio(imagem, x=x, y=y, cena=cena)



if __name__ == "__main__":
    
    Kwarwp(Jogo, medidas = STYLE) 