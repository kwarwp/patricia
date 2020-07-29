# patricia.delta.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Delta - Projeto sem descrição, (mude esta linha).

.. codeauthor:: Paulo Assumpção (golf) <mail@local.tipo>

.. codeauthor:: Anni Provietti (hotel) <mail@local.tipo>


.. codeauthor:: Emanuelle Simas (india) <ellesimas@gmail.com>

.. codeauthor:: Nome Sobrenome (juliet) <mail@local.tipo>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""
from _spy.vitollino.main import Cena, Elemento, STYLE
from delta.hotel import Game


TELA_INICIAL = "https://i.pinimg.com/originals/ff/7c/78/ff7c780990c7f867de2061645d9eff86.gif"
PEGADINHA = "https://i.imgur.com/JuvyDuW.png"
CLIQUE = "https://i.imgur.com/nJvb4wI.png"


STYLE["width"] = 600


class start:
    ''' Gera uma classe onde há tela inicial e dois elementos.
    
    '''

    def __init__(self):
        self.inicio = Cena(TELA_INICIAL, direita= Game())
        self.pegadinha = Elemento(PEGADINHA, tit="PLAY", texto = "Não é TOUCH", x=260, y=170, w=50, h=50, cena =self.inicio)
        self.pegadinha = Elemento(PEGADINHA, tit="MOUSE", x=380, y=285, w=60, h=60, vai = Game(), cena =self.inicio)
          
    def vai(self):
        self.inicio.vai()
        
class end:
    pass
    
    
if __name__=="__main__":
    start().vai()