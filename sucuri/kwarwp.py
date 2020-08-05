"""   Implementação do mapa no Kwarwp

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

.. version:: 20.01.1

"""
from _spy.vitollino.main import Jogo, STYLE

#largura e comprimento, respectivamente
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
    '''O GLIFOS corresponde ao dicionário que guarda a imagem dos elementos
    '''
    GLIFOS = {"&": "https://i.imgur.com/dZQ8liT.jpg",  # OCA ⛺
             "^": "https://imgur.com/8jMuupz.png",  # INDIO 
             ".": "https://i.imgur.com/uwYPNlz.png",  # CERCA 
             "_": "https://i.imgur.com/sGoKfvs.jpg",  # SOLO 
             "#": "https://imgur.com/ldI7IbK.png",  # TORA 
             "@": "https://imgur.com/tLLVjfN.png",  # PICHE 
             "~": "https://i.imgur.com/UAETaiP.gif",  # CEU 
             "*": "https://i.imgur.com/PfodQmT.gif"  # SOL ☀
               }

    def __init__(self, vitollino=None, mapa = MAPA_INICIO, medidas = {}):
        self.v = vitollino()
        '''Gera uma matriz de acordo com a quantidade de elementos no dicionário'''
        self.cena = self.cria(cenario=cenario) if vitollino else None
        
    def cercado(self):
        ''' Gera o cercado da cena
        '''
        cerca_baixo = (self.v.a(self.CERCA, w=100, h=100, x=0, y=400, cena=cena), 
                      self.v.a(self.CERCA, w=100, h=100, x=100, y=400, cena=cena),
                      self.v.a(self.CERCA, w=100, h=100, x=200, y=400, cena=cena),
                      self.v.a(self.CERCA, w=100, h=100, x=300, y=400, cena=cena),
                      self.v.a(self.CERCA, w=100, h=100, x=400, y=400, cena=cena),
                      self.v.a(self.CERCA, w=100, h=100, x=500, y=400, cena=cena))
                 
        cerca_esquerda = (self.v.a(self.CERCA, w=100, h=100, x=0, y=100, cena=cena), 
                         self.v.a(self.CERCA, w=100, h=100, x=0, y=200, cena=cena),
                         self.v.a(self.CERCA, w=100, h=100, x=0, y=300, cena=cena),
                         self.v.a(self.CERCA, w=100, h=100, x=0, y=400, cena=cena)) 
                          
        cerca_cima = (self.v.a(self.CERCA, w=100, h=100, x=0, y=100, cena=cena), 
                     self.v.a(self.CERCA, w=100, h=100, x=100, y=100, cena=cena),
                     self.v.a(self.CERCA, w=100, h=100, x=200, y=100, cena=cena),
                     self.v.a(self.CERCA, w=100, h=100, x=300, y=100, cena=cena),
                     self.v.a(self.CERCA, w=100, h=100, x=400, y=100, cena=cena),
                     self.v.a(self.CERCA, w=100, h=100, x=500, y=100, cena=cena))
                          
        cerca_direita = (self.v.a(self.CERCA, w=100, h=100, x=500, y=100, cena=cena), 
                        self.v.a(self.CERCA, w=100, h=100, x=500, y=300, cena=cena),
                        self.v.a(self.CERCA, w=100, h=100, x=500, y=400, cena=cena))
                 
    def cria(self, cenario="default"):
        """ Cria o ambiente de programação Kwarwp."""
        cena = self.v.c(self.SOLO)
        indio = self.v.a(self.INDIO, w=100, h=100, x=200, y=300, cena=cena)
        oca = self.v.a(self.OCA, w=100, h=100, x=500, y=200, cena=cena)
        #tora = self.v.a(self.TORA, w=100, h=100, x=100, y=400, cena=cena)
        piche = self.v.a(self.PICHE, w=100, h=100, x=100, y=200, cena=cena)
        ceu = self.v.a(self.CEU, w=600, h=100, x=0, y=0, cena=cena)
        sol = self.v.a(self.SOL, w=60, h=60, x=0, y=40, cena=cena)
        cerca = self.cercado()
        cena.vai()
        #return cena
    
if __name__ == "__main__":
    Kwarwp(Jogo) 