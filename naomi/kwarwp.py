# patricia.naomi.kwarwp.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Anni Provietti <anniprovietti@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""

MAPA_INICIO = """
######
#@...&.
#.#..#.
#.#.^#
######
"""

class Kwarwp():
    """ Jogo Kwarwp para ensino de programação.
       
       
    
    OCA = "https://i.imgur.com/dZQ8liT.jpg"
    INDIO = "https://imgur.com/8jMuupz.png"
    SOLO = "https://i.imgur.com/sGoKfvs.jpg"
    TORA = "https://imgur.com/ldI7IbK.png"
    PICHE = "https://imgur.com/tLLVjfN.png"
    CEU = "https://i.imgur.com/UAETaiP.gif"
    SOL = "https://i.imgur.com/PfodQmT.gif"
    """
    GLIFOS = {
    "&": "https://i.imgur.com/dZQ8liT.jpg",  # OCA âÂÂÂÂÂÂº
    "^": "https://imgur.com/8jMuupz.png",  # INDIO 
    ".": "https://i.imgur.com/npb9Oej.png",  # VAZIO 
    "_": "https://i.imgur.com/sGoKfvs.jpg",  # SOLO 
    "#": "https://imgur.com/ldI7IbK.png",  # TORA 
    "@": "https://imgur.com/tLLVjfN.png",  # PICHE 
    "~": "https://i.imgur.com/UAETaiP.gif",  # CEU 
    "*": "https://i.imgur.com/PfodQmT.gif"  # SOL âÂÂÂÂÂÂ
    }
    
    def __init__(self, vitollino=None,mapa=MAPA_INICIO, medida={}):
        self.V = vitollino()
        """ código antigo
        self.cena = self.cria(cenario=cenario) if vitollino else None
        """
        """ cria uma matriz para cada elemento descrito na linha texto"""
        mapa=mapa.split()
        """Largura da casa da arena dos desafios, número de colunas no mapa"""
        self.lado, self.col = 100, len(mapa[0])
        self.cena = self.cria(mapa=mapa) if vitollino else None
        
    def cria(self, mapa=" "):
        """ criação do ambiente de programação Kwarwp
        cena = self.V.c(self.SOLO)
        indio = self.V.a (self.INDIO,w=100, h=100, x=300,y=400, cena=cena)
        oca= self.V.a(self.OCA, w= 100, h=100, x=500, y=100, cena=cena)
        tora = self.V.a(self.TORA, w=100, h=100, x=100, y=400, cena=cena)
        piche = self.V.a(self.PICHE, w=100, h=100, x=100, y=100, cena=cena)
        piche = self.V.a(self.CEU, w=600, h=100, x=0, y=0, cena=cena)
        sol = self.V.a(self.SOL, w=60, h=60, x=0, y=40, cena=cena)
        cena.vai()
        return cena
        """
        """Cria um cenário com imagem de terra de chão batido, céu e sol"""
        lado = self.lado
        cena = self.V.c(self.GLIFOS["_"]) 
        ceu = self.V.a(self.GLIFOS["~"], w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.V.a(self.GLIFOS["*"], w=60, h=60, x=0, y=40, cena=cena)
        [self.cria_elemento( x=i*lado, y=j*lado+lado, cena=cena)
        for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)]
        cena.vai()
        return cena
    def cria_elemento(self, x, y, cena):
        lado = self.lado
        return self.V.a(self.GLIFOS[imagem], w=lado, h=lado, x=i*lado, y=j*lado+lado, cena=cena)
    
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE.update(width=800, height="600px")
    Kwarwp(Jogo).cria()
