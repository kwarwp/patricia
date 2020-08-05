# patricia.soraya.kwarapp.py
# SPDX-License-Identifier: GPL-3.0-or-later

""" Descrição: Construir tela Kwarwp

.. codeauthor:: Isabel Hortencia  <hortencia.garnica@nce.urj.br>

Changelog
---------
.. versionadded::    20.07
       Criar um Mapa de inicio
"""
from collections import namedtuple as nt
Fab = nt("Fab", "objeto imagem")

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
        :param mapa: Um texto representando o mapa do desafio.
        :param medidas: Um dicionário usado para redimensionar a tela.
    """
     VITOLLINO = None
    """Referência estática para obter o engenho de jogo."""
    LADO = None
    """Referência estática para definir o lado do piso da casa."""




"""    GLIFOS = {
    "&": "https://i.imgur.com/dZQ8liT.jpg",  # OCA 
    "^": "https://imgur.com/8jMuupz.png",  # INDIO 
    ".": "https://i.imgur.com/npb9Oej.png",  # VAZIO 
    "_": "https://i.imgur.com/sGoKfvs.jpg",  # SOLO 
    "#": "https://imgur.com/ldI7IbK.png",  # TORA 
    "@": "https://imgur.com/tLLVjfN.png",  # PICHE 
    "~": "https://i.imgur.com/UAETaiP.gif",  # CEU 
    "*": "https://i.imgur.com/PfodQmT.gif",  # SOL 
    "+": "https://i.imgur.com/uwYPNlz.png"  # CERCA 
    }"""

    fabrica = {
    "&": Fab(self.coisa, f"{IMGUR}dZQ8liT.jpg"), # OCA
    "^": Fab(self.indio, f"{IMGUR}8jMuupz.png"), # INDIO
    ".": Fab(self.vazio, f"{IMGUR}npb9Oej.png"), # VAZIO
    "_": Fab(self.coisa, f"{IMGUR}sGoKfvs.jpg"), # SOLO
    "#": Fab(self.coisa, f"{IMGUR}ldI7IbK.png"), # TORA
    "@": Fab(self.coisa, f"{IMGUR}tLLVjfN.png"), # PICHE
    "~": Fab(self.coisa, f"{IMGUR}UAETaiP.gif"), # CEU
    "*": Fab(self.coisa, f"{IMGUR}PfodQmT.gif"), # SOL
    "|": Fab(self.coisa, f"{IMGUR}uwYPNlz.png")  # CERCA
    }

    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
        """ self.v = vitollino()
        Cria um matriz com os elementos descritos em cada linha de texto
        mapa = mapa.split()
        Largura da casa da arena dos desafios, número de colunas no mapa
        self.lado, self.col = 600//8, len(mapa[0])
        self.cena = self.cria(mapa=mapa) if vitollino else None"""
        
        Kwarwp.VITOLLINO = self.v = vitollino()
        """Cria um matriz com os elementos descritos em cada linha de texto"""
        self.mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas no mapa"""
        self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        Kwarwp.LADO = self.lado
        w, h = self.col *self.lado, self.lin *self.lado
        self.taba = {}
        """Dicionário que a partir de coordenada (i,J) localiza um piso da taba"""
        medidas.update(width=w, height=f"{h}px")
        self.cena = self.cria(mapa=self.mapa) if vitollino else None

    """def cria(self, mapa="default"):
        Cria o ambiente de programação Kwarwp.
        Cria um cenário com imagem de terra de chão batido, céu e sol
        lado = self.lado
        cena = self.v.c(self.GLIFOS["_"])
        ceu = self.v.a(self.GLIFOS["~"], w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(self.GLIFOS["*"], w=60, h=60, x=0, y=40, cena=cena)
        [self.cria_elemento( x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)]
        cena.vai()
        return cena"""

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

        
    """def cria_elemento(self, x, y, cena):
        lado = self.lado
        return self.v.a(self.GLIFOS[imagem], w=lado, h=lado, x=i*lado, y=j*lado+lado, cena=cena)"""

    def coisa(self, imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)



class Indio():
    """cria a classe indio"""
    def __init__(self, imagem, x, y, cena):
        self.lado = lado = Kwarwp.LADO
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        
    def indio(self, imagem, x, y, cena):
        lado = self.lado
        return Indio(imagem, x=x, y=y, cena=cena)    
        
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE["width"] = 600
    STYLE["height"] = "600px"
    Kwarwp(Jogo, mapa=MAPA_ROCHA, medidas=STYLE)