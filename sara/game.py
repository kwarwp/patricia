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

IMG_FASE_1 = f"https://activufrj.nce.ufrj.br/file/ProgOO/fase1.png"
IMG_FASE_2 = f"https://activufrj.nce.ufrj.br/file/ProgOO/fase2.png"
IMG_FASE_3 = f"https://activufrj.nce.ufrj.br/file/ProgOO/fase3.png"
IMG_OCA = f"https://i.imgur.com/dZQ8liT.jpg"
IMG_FUNDO = f"https://i.imgur.com/sGoKfvs.jpg"

IMG_WIDTH_OCA = 50
IMG_HEIGHT_OCA = 50

IMG_WIDTH_FUNDO = 150
IMG_HEIGHT_FUNDO = 300

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
        self.direita()
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
        self.direita()
        self.larga()
        self.esquerda()
        self.anda()
        self.esquerda()
        self.anda()
        self.direita()
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
        self.esquerda()
        self.anda()
        self.pega()
        self.direita()
        self.anda()
        self.larga()
        self.direita()
        self.anda()
        self.anda()
        self.esquerda()
        self.anda()
        self.direita()
        self.anda()
        self.esquerda()
        self.anda()


class Fase3Indio2(Indio):
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        self.anda()
        self.direita()
        self.pega()
        self.esquerda()
        self.anda()
        self.larga()
        self.direita()
        self.anda()
        self.esquerda()
        self.anda()
        self.anda()
    

class Game:
    
    def __init__(self, vitollino, medidas):
        self.vitollino = vitollino
        self.medidas = medidas
    
    def vai(self):
        from _spy.vitollino.main import Cena, Elemento
        
        cena = Cena(IMG_FUNDO)

        Elemento(IMG_FASE_1, x=80, y=5, width=IMG_WIDTH_FUNDO, height=IMG_HEIGHT_FUNDO, cena=cena)
        fase_1 = Elemento(IMG_OCA, tit="Fase 1", x=100, y=20, width=IMG_WIDTH_OCA, height=IMG_HEIGHT_OCA, cena=cena)
        fase_1.elt.bind("click", self.run_fase_1)
        
        Elemento(IMG_FASE_2, x=230, y=5, width=IMG_WIDTH_FUNDO, height=IMG_HEIGHT_FUNDO, cena=cena)
        fase_2 = Elemento(IMG_OCA, tit="Fase 2", x=250, y=20, width=IMG_WIDTH_OCA, height=IMG_HEIGHT_OCA, cena=cena)
        fase_2.elt.bind("click", self.run_fase_2)
        
        Elemento(IMG_FASE_3, x=380, y=5, width=IMG_WIDTH_FUNDO, height=IMG_HEIGHT_FUNDO, cena=cena)
        fase_3 = Elemento(IMG_OCA, tit="Fase 3", x=400, y=20, width=IMG_WIDTH_OCA, height=IMG_HEIGHT_OCA, cena=cena)
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
    STYLE.update(width=600, height="500px")
    main(Jogo, STYLE)
