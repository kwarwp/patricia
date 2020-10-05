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

IMG_WIDTH = 150
IMG_HEIGHT = 150

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
        
    def vai(self):
        from _spy.vitollino.main import Cena, Elemento, STYLE
        
        cena = Cena()
        
        fase_1 = Elemento(IMG_FASE_1, tit="Fase 1", x=0, y=0, width=IMG_WIDTH, height=IMG_HEIGHT, cena=cena)
        cena.vai()

    
    
def start_game():
    fase1 = kwarwp_main(vitollino=vitollino, medidas=medidas, mapa=MAPA_FASE_1, indios=(Fase1,))
    fase2 = kwarwp_main(vitollino=vitollino, medidas=medidas, mapa=MAPA_FASE_2, indios=(Fase2,))
    fase3 = kwarwp_main(vitollino=vitollino, medidas=medidas, mapa=MAPA_FASE_3, indios=(Fase3Indio1,Fase3Indio2))


def main(vitollino, medidas):
    Game().vai()
        
    
if __name__ == "__main__":
    main(Jogo, STYLE)
