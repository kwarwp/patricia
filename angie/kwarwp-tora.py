# patricia.angie.kwarwp-tora.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto Kwarwp.

.. codeauthor:: Monica Novellino - monicanovellino@gmail.com

Changelog
---------
.. versionadded::    20.08
        ìndio movimenta tora

"""
from collection import namedtuple as nt
from kwarwp.kwarwppart import Vazio, Piche, Oca, Tora, NULO

"""Prefixo do site IMGUR"""
IMGUR = "https://imgur.com/"
        
MAPA_INICIO = """
@....&
......
.....#
.#.^..
"""
    

Ponto = nt("Ponto", "x y")
"""Par de coordenadas na direção horizontal (x) e vertiacal (y)."""
Rosa = nt("Rosa", "n l s o")
"""Rosa dos ventos com as direções norte, leste, sul e oeste."""

class Indio():

    AZIMUTE = Rosa(Ponto(0, -1),Ponto(1, 0),Ponto(0, 1),Ponto(-1, 0),)
    """Constante com os pares ordenados que representam os vetores unitários dos pontos cardeais."""

    def __init__(self, imagem, x, y, cena, taba):
        self.lado = lado = Kwarwp.LADO
        self.azimute = self.AZIMUTE.n
        """índio olhando para o norte"""
        self.taba = taba
        self.vaga = self
        self.posicao = (x//lado,y//lado)
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self.x = x
        """Este x provisoriamente distingue o índio de outras coisas construídas com esta classe"""
        if x:
            self.indio.siz = (lado*3, lado*4)
            """Define as proporções da folha de sprites"""
            self.mostra()


if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE["width"] = 600
    STYLE["heigth"] = "500px"
    Kwarwp(Jogo, mapa=MAPA_INICIO)
    