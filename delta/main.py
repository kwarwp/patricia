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
from _spy.vitollino.main import Cena, STYLE
from hotel.main import Game2x2


TELA_INICIAL = "https://i.pinimg.com/originals/ff/7c/78/ff7c780990c7f867de2061645d9eff86.gif"
TELA_MEIO = "https://i.imgur.com/FTkbaSW.jpg"


STYLE["width"] = 600


class start:

    def __init__(self):
        self.inicio = Cena(TELA_INICIAL, direita= Game2x2())
          
    def vai(self):
        self.inicio.vai()
    
class end:
    pass
    
    
if __name__=="__main__":
    start().vai()