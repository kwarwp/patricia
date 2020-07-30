# patricia.soraya.kwarapp.py
# SPDX-License-Identifier: GPL-3.0-or-later

""" Descrição: Construir tela Kwarwwp

.. codeauthor:: Isabel Hortencia  <hortencia.garnica@nce.urj.br>

Changelog
---------
.. versionadded::    16.07
       Pagina inicial do Game
"""
MAPA_INICIO = """
.......
......&
...@...
.^.....
"""

class Kwarwp():
    """ Jogo para ensino de programação.

        :param vitollino: Empacota o engenho de jogo Vitollino.
    """

GLIFOS = {
"&": "https://i.imgur.com/dZQ8liT.jpg",  # OCA ⛺
"^": "https://imgur.com/8jMuupz.png",  # INDIO 
".": "https://i.imgur.com/npb9Oej.png",  # VAZIO 
"_": "https://i.imgur.com/sGoKfvs.jpg",  # SOLO 
"#": "https://imgur.com/ldI7IbK.png",  # TORA 
"@": "https://imgur.com/tLLVjfN.png",  # PICHE 
"~": "https://i.imgur.com/UAETaiP.gif",  # CEU 
"*": "https://i.imgur.com/PfodQmT.gif"  # SOL ☀
}

    
    def __init__(self, vitollino=None, cenario="default"):
        self.v = vitollino()
        self.cena = self.cria(cenario=cenario) if vitollino else None

    def cria(self, cenario="default"):
        """ Cria o ambiente de programação Kwarwp."""
        cena = self.v.c(self.SOLO)
        indio = self.v.a(self.INDIO, w=100, h=100, x=300, y=400, cena=cena)
        oca = self.v.a(self.OCA, w=100, h=100, x=500, y=100, cena=cena)
        tora = self.v.a(self.TORA, w=100, h=100, x=100, y=400, cena=cena)
        piche = self.v.a(self.PICHE, w=100, h=100, x=100, y=100, cena=cena)
        piche = self.v.a(self.CEU, w=600, h=100, x=0, y=0, cena=cena)
        sol = self.v.a(self.SOL, w=60, h=60, x=0, y=40, cena=cena)
        cena.vai()
        return cena
        
        
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE["width"] = 600
    STYLE["height"] = "500px"
    Kwarwp(Jogo)