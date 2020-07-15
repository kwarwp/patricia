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

capa_do_jogo = "https://i.imgur.com/0RVnppj.png"
botao_jogar = "https://i.imgur.com/F3Q0bDv.png"
botao_sobre = "https://i.imgur.com/pG9wDIz.png"

class Jogo:
    def ___init___(self):
        self.capa = Cena (img= capa_do_jogo)
        self.botao_jogar = Elemento (img = botao_jogar)
        self.botao_sobre = Elemento (img = botao_sobre)

        self.botao_sobre.entra(self.capa)
        self.botao_jogar.entra(self.capa)
        


