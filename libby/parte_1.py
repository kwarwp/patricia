# patricia.libby.parte_1.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Aula Kwarwp Charles.

.. codeauthor:: Charles Pimentel <pimentelufrj@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Parte_1.

"""

# SPDX-License-Identifier: GPL-3.0-or-later
class Kwarwp():
    """ Jogo para ensino de programação.

        :param vitollino: Empacota o engenho de jogo Vitollino.
    """
    OCA = "https://i.imgur.com/dZQ8liT.jpg"
    INDIO = "https://imgur.com/8jMuupz.png"
    SOLO = "https://i.imgur.com/sGoKfvs.jpg"
    TORA = "https://imgur.com/ldI7IbK.png"
    PICHE = "https://imgur.com/tLLVjfN.png"
    CEU = "https://i.imgur.com/UAETaiP.gif"
    SOL = "https://i.imgur.com/PfodQmT.gif"
    CERCA = "https://i.imgur.com/uwYPNlz.png"

    def __init__(self, vitollino=None, cenario="default"):
        self.v = vitollino()
        self.cena = self.cria(cenario=cenario) if vitollino else None

    def cria(self, cenario="default"):
        """ Cria o ambiente de programação Kwarwp."""
        cena = self.v.c(self.SOLO)
        indio = self.v.a(self.INDIO, w=100, h=100, x=100, y=400, cena=cena)
        oca = self.v.a(self.OCA, w=100, h=100, x=500, y=100, cena=cena)
        tora = self.v.a(self.TORA, w=100, h=100, x=100, y=250, cena=cena)
        piche = self.v.a(self.PICHE, w=100, h=100, x=0, y=100, cena=cena)
        ceu = self.v.a(self.CEU, w=600, h=100, x=0, y=0, cena=cena)
        sol = self.v.a(self.SOL, w=60, h=60, x=0, y=40, cena=cena)

        cerca = self.v.a(self.CERCA, w=100, h=100, x=300, y=100, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=300, y=200, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=300, y=400, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=300, y=500, cena=cena)
        
        cerca = self.v.a(self.CERCA, w=100, h=100, x=500, y=500, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=400, y=500, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=200, y=500, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=200, y=500, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=100, y=500, cena=cena)
        
        cerca = self.v.a(self.CERCA, w=100, h=100, x=0, y=500, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=0, y=400, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=0, y=300, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=0, y=200, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=0, y=100, cena=cena)
        
        cerca = self.v.a(self.CERCA, w=100, h=100, x=100, y=100, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=200, y=100, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=400, y=100, cena=cena)
             
        cerca = self.v.a(self.CERCA, w=100, h=100, x=500, y=200, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=500, y=300, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=500, y=400, cena=cena)
        cerca = self.v.a(self.CERCA, w=100, h=100, x=500, y=500, cena=cena)
        
        cena.vai()
        return cena
        
    def cria_elemento(self, x, y, cena):
        
        lado = self.lado
        return self.v.a(self.GLIFOS[imagem], w=lado, h=lado, x=i*lado, y=j*lado+lado, cena=cena)

def main(vitollino):
    Kwarwp(vitollino)
        
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE.update(width=600, height="500px")
    main(Jogo)