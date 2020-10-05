# patricia.sara.game.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Paulo Assumpção <paulo.assump@gmail.com>

Changelog
---------
.. versionadded::    20.10
        Modulo game.

"""


from _spy.vitollino.main import Jogo, STYLE
from sara.kwarwp import main as kwarwp_main, Indio

MAPA_FASE_1 = """
@....&
......
......
.#.p..
"""

MAPA_FASE_2 = """
@....&
....@@
...#.#
.#.p..
"""

MAPA_FASE_3 = """
....@&
..@...
.....#
.#.p$.
"""

IMG = "https://i.imgur.com/dZQ8liT.jpg"

IMG_WIDTH = 50
IMG_HEIGHT = 50

class Fase1(Indio):
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        self.esquerda()
        self.anda()
        self.pega()
        self.direita()
        self.anda()
        self.anda()
        self.anda()
        self.esquerda()
        self.anda()
        self.larga()
        self.esquerda()
        self.esquerda()
        self.anda()
        self.anda()
        self.anda()
        self.anda()

class Fase2(Indio):
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        self.esquerda()
        self.esquerda()
        self.esquerda()
        self.anda()
        self.anda()
        self.esquerda()
        self.pega()
        self.anda()
        self.larga()
        self.esquerda()
        self.anda()
        self.anda()
        self.pega()
        self.esquerda()
        self.esquerda()
        self.esquerda()
        self.larga()
        self.esquerda()
        self.anda()
        self.esquerda()
        self.anda()
        self.esquerda()
        self.esquerda()
        self.esquerda()
        self.anda()
        self.pega()
        self.direita()
        self.anda()
        self.anda()
        self.anda()
        self.esquerda()
        self.anda()
        self.larga()
        self.esquerda()
        self.esquerda()
        self.anda()
        self.anda()
        self.anda()
        self.anda()
        
        
class Fase3Indio1(Indio):
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        self.anda()
        self.direita()
        self.pega()
        self.esquerda()
        self.anda()
        self.anda()
        self.anda()
        self.direita()
        self.larga()

class Fase3Indio2(Indio):
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        self.anda()
        self.direita()
        self.pega()
        self.esquerda()
        self.anda()
        self.anda()
        self.anda()
        self.direita()
        self.larga()

    

class Game:
    
    def __init__(self, vitollino, medidas):
        self.vitollino = vitollino
        self.medidas = medidas
    
    def vai(self):
        from _spy.vitollino.main import Cena, Elemento, STYLE
        
        cena = Cena()
        
        fase_1 = Elemento(IMG, tit="Fase 1", x=50, y=0, width=IMG_WIDTH, height=IMG_HEIGHT, cena=cena)
        fase_1.elt.bind("click", self.run_fase_1)
        
        fase_2 = Elemento(IMG, tit="Fase 2", x=200, y=0, width=IMG_WIDTH, height=IMG_HEIGHT, cena=cena)
        fase_2.elt.bind("click", self.run_fase_2)
        
        fase_3 = Elemento(IMG, tit="Fase 3", x=350, y=0, width=IMG_WIDTH, height=IMG_HEIGHT, cena=cena)
        fase_3.elt.bind("click", self.run_fase_3)
        
        cena.vai()
        
    def run_fase_1(self, env=None):
        kwarwp_main(vitollino=self.vitollino, medidas=self.medidas, mapa=MAPA_FASE_1, indios=(Fase1,))
    
    def run_fase_2(self, env=None):
        kwarwp_main(vitollino=self.vitollino, medidas=self.medidas, mapa=MAPA_FASE_2, indios=(Fase2,))
        
    def run_fase_3(self, env=None):
        kwarwp_main(vitollino=self.vitollino, medidas=self.medidas, mapa=MAPA_FASE_3, indios=(Fase3Indio1,Fase3Indio2))


def main(vitollino, medidas):
    Game(vitollino, medidas).vai()
        
    
if __name__ == "__main__":
    main(Jogo, STYLE)
