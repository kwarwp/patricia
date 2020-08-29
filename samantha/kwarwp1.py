# patricia.samantha.kwarwp1.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto Kwarwp da Raquel.

.. codeauthor:: Raquel  <raquelmachado4993@gmail.com>

Changelog
---------
.. versionadded::  29.08
        Seguindo tutorial - Criando a cena do jogo Kwarwp usando o Vitollino - Inserindo as cercas no mapa
"""

MAPA_INICIO = """
+++++++
+..+..&
+..#..+
+^.+..+
+++++++
"""


class Kwarwp():
    """ Arena onde os desafios ocorrem.
    
        :param vitollino: Empacota o engenho de jogo Vitollino.
        :param mapa: Um texto representando o mapa do desafio.
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
    "+": "https://i.imgur.com/uwYPNlz.png"  # Cerca
    }
    
    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
        self.v = vitollino()
        """Cria um matriz com os elementos descritos em cada linha de texto"""
        mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas no mapa"""
        self.lado, self.col = 600//8, len(mapa[0]) 
        self.cena = self.cria(mapa=mapa) if vitollino else None
        
    def cria(self, mapa="  "):
        """Cria um cenário com imagem de terra de chão batido, céu e sol"""
        lado = self.lado
        cena = self.v.c(self.GLIFOS["_"])
        ceu = self.v.a(self.GLIFOS["~"], w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(self.GLIFOS["*"], w=60, h=60, x=0, y=40, cena=cena)
        """Posiciona os elementos segundo suas posições i, j na matriz mapa"""
        [self.cria_elemento( x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)]
        cena.vai()
        return cena
        
    def cria_elemento(self, x, y, cena):
        lado = self.lado
        return self.v.a(self.GLIFOS[imagem], w=lado, h=lado, x=i*lado, y=j*lado+lado, cena=cena)   
    
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE.update(width=500, height="400px")
    Kwarwp(Jogo)