# patricia.soraya.main.py
# SPDX-License-Identifier: GPL-3.0-or-later

""" Jogo do Mistério da Praia.

    Descubra o mistério desta praia.

Changelog
---------
    20.07
        * NEW: O jogo original.

"""
from _spy.vitollino.main import Cena
from grace.main import praia
__version__ = "20.07"
__author__ = "Isabel Hortencia Garnica""
CENA_PRAIA = "https://i.imgur.com/zOxshRh.jpg"


class Calcada:
    """ Representa uma cena da calçada da praia """
    def vai(self):
        """ Mostra a cena da praia """
        Cena(CENA_PRAIA).vai()
    
Calcada().vai()
