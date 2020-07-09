# patricia.adda.main.py
# SPDX-License-Identifier: GPL-3.0-or-later

""" Jogo do Mistério da Praia.

    Descubra o mistério desta praia.

Changelog
---------
    20.07
        * NEW: O jogo original.

"""
from _spy.vitollino.main import Cena
# from grace.main import Praia
__version__ = "20.07"
__author__ = "Carlo"
CENA_CALCADA = "https://i.imgur.com/zOxshRh.jpg"


class Calcada:
    """ Representa uma cena da calçada da praia """
    def vai(self):
        """ Mostra a cena da praia """
        #Cena(CENA_CALCADA, direita=Praia()).vai()
        Cena(CENA_CALCADA).vai()
    
Calcada()
