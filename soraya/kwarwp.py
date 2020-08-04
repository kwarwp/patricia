# patricia.soraya.kwarapp.py
# SPDX-License-Identifier: GPL-3.0-or-later

""" Descrição: Construir tela Kwarwp

.. codeauthor:: Isabel Hortencia  <hortencia.garnica@nce.urj.br>

Changelog
---------
.. versionadded::    20.07
       Criar um Mapa de inicio
"""


MAPA_INICIO = """
@....&
......
......
.#.^..
"""

MAPA_ROCHA = """
+++++++
+..+..&
+..#..+
+^.+..+
+++++++
"""

class Kwarwp():
    """ Jogo para ensino de programação.

        :param vitollino: Empacota o engenho de jogo Vitollino.
    """



    GLIFOS = {
    "&": "https://i.imgur.com/dZQ8liT.jpg",  # OCA 
    "^": "https://imgur.com/8jMuupz.png",  # INDIO 
    ".": "https://i.imgur.com/npb9Oej.png",  # VAZIO 
    "_": "https://i.imgur.com/sGoKfvs.jpg",  # SOLO 
    "#": "https://imgur.com/ldI7IbK.png",  # TORA 
    "@": "https://imgur.com/tLLVjfN.png",  # PICHE 
    "~": "https://i.imgur.com/UAETaiP.gif",  # CEU 
    "*": "https://i.imgur.com/PfodQmT.gif",  # SOL 
    "+": "https://i.imgur.com/uwYPNlz.png"  # CERCA 
    }


    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
        self.v = vitollino()
        """Cria um matriz com os elementos descritos em cada linha de texto"""
        mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas no mapa"""
        self.lado, self.col = 600//8, len(mapa[0])
        self.cena = self.cria(mapa=mapa) if vitollino else None

    def cria(self, mapa="default"):
        """ Cria o ambiente de programação Kwarwp."""
        """Cria um cenário com imagem de terra de chão batido, céu e sol"""
        lado = self.lado
        cena = self.v.c(self.GLIFOS["_"])
        ceu = self.v.a(self.GLIFOS["~"], w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(self.GLIFOS["*"], w=60, h=60, x=0, y=40, cena=cena)
        [self.cria_elemento( x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)]
        cena.vai()
        return cena

        
    def cria_elemento(self, x, y, cena):
        lado = self.lado
        return self.v.a(self.GLIFOS[imagem], w=lado, h=lado, x=i*lado, y=j*lado+lado, cena=cena)
        
        
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE["width"] = 600
    STYLE["height"] = "600px"
    Kwarwp(Jogo, mapa=MAPA_ROCHA, medidas=STYLE)