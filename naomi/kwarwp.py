# patricia.naomi.kwarwp.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Anni Provietti <anniprovietti@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""

class Kwarwp():
    """ Jogo Kwarwp para ensino de programação.
       
       
    """
    OCA = "https://i.imgur.com/dZQ8liT.jpg"
    INDIO = "https://imgur.com/8jMuupz.png"
    SOLO = "https://i.imgur.com/sGoKfvs.jpg"
    TORA = "https://imgur.com/ldI7IbK.png"
    PICHE = "https://imgur.com/tLLVjfN.png"
    CEU = "https://i.imgur.com/UAETaiP.gif"
    SOL = "https://i.imgur.com/PfodQmT.gif"
    
    def __init__(self, vitollino=Nome, cenario="default"):
        self.V = vitollino()
        self.cena = self.cria(cenario=cenario) if vitollino else None
    def cria(self, cenario="default"):
        """ criação do ambiente de programação Kwarwp"""
        cena = self.V.c(self.SOLO)
        indio = self.V.a (self.INDIO,w=100, h=100, x=300,y=400, cena=cena)
        oca= self.V.a(self.OCA, w= 100, h=100, x=500, y=100, cena=cena)
         tora = self.V.a(self.TORA, w=100, h=100, x=100, y=400, cena=cena)
        piche = self.V.a(self.PICHE, w=100, h=100, x=100, y=100, cena=cena)
        piche = self.V.a(self.CEU, w=600, h=100, x=0, y=0, cena=cena)
        sol = self.V.a(self.SOL, w=60, h=60, x=0, y=40, cena=cena)
        cena.vai()
        return cena
