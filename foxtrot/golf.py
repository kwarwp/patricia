# patricia.foxtrot.golf.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto SuperPython World,

.. codeauthor:: Raquel Fernandes <raquelmachado4993@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Página inicial do Jogo.

"""
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
capa = "https://i.imgur.com/SI1BO9E.png"
botao_jogar = "https://i.imgur.com/F3Q0bDv.png"
botao_sobre = "https://i.imgur.com/pG9wDIz.png"

class Jogo:
    def __init__(self):
        self.capa= Cena (img=capa)
        self.capa.vai()
        self.botao_jogar=Elemento
        self.botao_sobre=Elemento
        self.botao_sobre.entra(self.capa)
        self.botao_jogar.entra(self.capa)

if __name__ == "__main__":
    Jogo().inicia()
