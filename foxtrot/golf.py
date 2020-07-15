# patricia.foxtrot.golf.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto SuperPython World,

.. codeauthor:: Raquel Fernandes <raquelmachado4993@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Página inicial do Jogo.

"""
from __spy.vitollino.main import Cena,Elemento,Texto

class Jogo:
    def __init__(self):
        self.capa = Cena (img= "https://i.imgur.com/0RVnppj.png")
        self.botao_jogar = Elemento (img = "https://i.imgur.com/F3Q0bDv.png")
        self.botao_sobre = Elemento (img = "https://i.imgur.com/pG9wDIz.png")

        self.botao_sobre.entra(self.capa)
        self.botao_jogar.entra(self.capa)

if __name__ == "__main__":
    Jogo().inicia()
