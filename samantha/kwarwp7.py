# patricia.samantha.kwarwp7.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto final - três desafios
FASE 1.
Nessa primeira aventura o índio precisa vencer obstáculos 
para chegar até a caverna!

.. codeauthor:: Raquel M. M. Fernandes - raquelmachado4993@gmail.com

Changelog
---------
.. versionadded::    27.09
    
"""

from _spy.vitollino.main import Jogo, STYLE
from samantha.kwarwp9 import main as kwarwp_main, Indio
MAPA_INICIO = """
@....&
......
.....#
.#.p`.
"""

MAPA_INICIAL= """
|||||||||
|@..@...|
|..&|.@.|
|..@|...|
|...@.r.|
|@....^.|
"""

MAPA_INICIAL2= """
T.|@||@|&
@...@|...
@......@|
|.|@|@..|
@..|....@
|@^..|..|
"""

MAPA_INICIAL3= """
@@@@@@@@@
@...|...@
&....|.|@
|...|...@
|.#.|.|.@
|@^@..|.@
"""

class Kaiowa(Indio):
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        self.empurra()
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
    return kwarwp_main(vitollino=vitollino, medidas=medidas, mapa=MAPA_INICIAL, indios=(Kaiowa,))
        
    
if __name__ == "__main__":
    main(Jogo, STYLE)
