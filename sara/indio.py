# patricia.sara.indio.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto Indio.

.. codeauthor:: Paulo Assumpcao <paulo.assump@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Criando o indio para o jogo

"""

MAPA_INICIO = """
+++++++
+..+..&
+..#..+
+^.+..+
+++++++
"""

IMGUR = 'https://i.imgur.com/'

class Indio():

    def __init__(self, imagem, x, y, cena):
        self.lado = lado = Kwarwp.LADO
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)

class Kwarwp():
    
    VITOLLINO = None
    """Referência estática para obter o engenho de jogo."""
    LADO = None
    """Referência estática para definir o lado do piso da casa."""

    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
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
        
    def cria(self, mapa=""):

        from collections import namedtuple as nt
        Fab = nt("Fab", "objeto imagem")
        
        fabrica = {
        "&": Fab(self.oca, f"{IMGUR}dZQ8liT.jpg"), # OCA
        "^": Fab(self.indio, f"{IMGUR}8jMuupz.png"), # INDIO
        ".": Fab(self.vazio, f"{IMGUR}npb9Oej.png"), # VAZIO
        "_": Fab(self.solo, f"{IMGUR}sGoKfvs.jpg"), # SOLO
        "#": Fab(self.tora, f"{IMGUR}ldI7IbK.png"), # TORA
        "@": Fab(self.piche, f"{IMGUR}tLLVjfN.png"), # PICHE
        "~": Fab(self.ceu, f"{IMGUR}UAETaiP.gif"), # CEU
        "*": Fab(self.sol, f"{IMGUR}PfodQmT.gif"), # SOL
        "|": Fab(self.cerca, f"{IMGUR}uwYPNlz.png")  # CERCA
        }
        
        mapa = mapa if mapa != "" else self.mapa

        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].imagem)
        ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena)
        
        self.taba = { (i, j): fabrica["^"].objeto(fabrica["^"].imagem, x=i*lado, y=j*lado+lado, cena=cena) for j, linha in enumerate(mapa) for i, imagem in enumerate(linha) }

        cena.vai()
        return cena

        
    def oca(self, imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)

    def vazio(self, imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)

    def solo(self, imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        
    def tora(self, imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)

    def piche(self, imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)

    def ceu(self, imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
    
    def sol(self, imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)

    def cerca(self, imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        
    def coisa(self, imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        
    def indio(self, imagem, x, y, cena):
        lado = self.lado
        return Indio(imagem, x=x, y=y, cena=cena)
        
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE.update(width=500, height="400px")
    Kwarwp(Jogo)
