# patricia.angie.kwarwpteste.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto kwarwp - classe de testes

.. codeauthor:: Monica Novellino <monicanovellino@gmail.com@local.tipo>

Changelog
---------
.. versionadded::    20.09
        Descreva o que você adicionou no código.

"""
from _spy.vitollino.main import Jogo
from unittest import TestCase
# from unittest.mock import MagicMock
from angie.kwarwptora import Kwarwp, Indio
from angie.kwarwpart import Piche, Vazio, Oca, Tora, NULO
#sys.path.insert(0, os.path.abspath('../../libs'))

class Test_Kwarwp(TestCase):
    """ Teste do Jogo para ensino de programação.

    Vamos aqui definir um conjunto de URLs identificadoras das peças.
    """
    ABERTURA = "https://i.imgur.com/dZQ8liT.jpg"
    INDIO = "https://imgur.com/UCWGCKR.png"
    OCA = "https://imgur.com/dZQ8liT.jpg"
    PICHE = "https://imgur.com/tLLVjfN.png"
    TORA = "https://imgur.com/0jSB27g.png"
