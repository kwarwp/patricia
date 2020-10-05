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

MAPA_INICIO = """
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


class Kaiowa(Indio):
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
        
class Vitollino(Jogo):
    """ Empacota o engenho de jogo Vitollino """
    pass

def main(vitollino, medidas):
    return kwarwp_main(vitollino=vitollino, medidas=medidas, mapa=MAPA_INICIO, indios=(Fase1,))
        
    
if __name__ == "__main__":
    main(Jogo, STYLE)
