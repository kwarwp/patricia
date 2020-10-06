# patricia.samantha.kwarwp7.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto final - três desafios
FASE 1.Na primeira aventura o índio precisa vencer obstáculos 
para chegar até a caverna!
FASE 2. Na segunda fase o índio precisa tomar cuidado para não cair na toca do tatu!
FASE 3. Na terceira fase o índio precisa chegar até a caverna sem cair no córrego!
PARA JOGAR, COMENTE OU DESCOMENTE OS DESAFIOS NA DEF MAIN! 
.. codeauthor:: Raquel M. M. Fernandes - raquelmachado4993@gmail.com

Changelog
---------
.. versionadded::    06.10
    
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
|...@...|
|@....^.|
"""

MAPA_INICIAL2= """
T.oaooaoa
a...ao..&
a......ao
o.oaoa..o
a..o....a
oa^..o..o
"""

MAPA_INICIAL3= """
ccccccccc
c...e...c
m....e.ec
e...e...c
e.r.e.e.c
ec^c..e.c
"""

class Kaiowa(Indio):
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
       #roteiro desafio 1
       #self.esquerda()
       #self.anda()
       #self.anda()
       #self.anda()
       #self.anda()
       #self.direita()
       #self.anda()
       #self.anda()
       #self.anda()
       #self.direita()
       #self.anda()
        
       #roteiro desafio2
       #self.direita()
       #self.anda()
       #self.anda()
       #self.esquerda()
       #self.anda()
       #self.direita()
       #self.anda()
       #self.anda()
       #self.esquerda()
       #self.anda()
       #self.anda()
       #self.anda()
       #self.direita()
       #self.anda()
       #self.anda()
       
       #roteiro desafio 3
        self.empurra()
        self.anda()
        self.empurra()
        self.anda()
        self.empurra()
        self.anda()
        self.esquerda()
        self.anda()
        self.anda()
       

class Vitollino(Jogo):
    """ Empacota o engenho de jogo Vitollino """
    pass

def main(vitollino, medidas):
    #return kwarwp_main(vitollino=vitollino, medidas=medidas, mapa=MAPA_INICIAL, indios=(Kaiowa,))
    #return kwarwp_main(vitollino=vitollino, medidas=medidas, mapa=MAPA_INICIAL2, indios=(Kaiowa,))
    return kwarwp_main(vitollino=vitollino, medidas=medidas, mapa=MAPA_INICIAL3, indios=(Kaiowa,))
        
    
if __name__ == "__main__":
    main(Jogo, STYLE)
