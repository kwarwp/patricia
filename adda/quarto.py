# patricia.adda.quarto.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo de Tabuleiro Quarto.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    20.07
        Criando o tabuleiro.

"""
from _spy.vitollino.main import Cena, Elemento, STYLE
TAMANHO = 600
STYLE.update(width={TAMANHO}, height=f"{TAMANHO}px")


class Tabuleiro:
    MADEIRA = "https://i.imgur.com/8mPjfYk.jpg"
    TABULEIRO = "https://i.imgur.com/ZkjApBv.jpg"
    def __init__(self):
        self.lado = TAMANHO // 8
        self.tabuleiro = Cena(self.MADEIRA)
        self.tabua = self.table(self.tabuleiro)
        
    def vai(self):
        self.tabuleiro.vai()
    
    def table(self, base, linhas=5, colunas=5, dx=0, dy=3):
        def casa(x, y):
            t = self.lado
            x, y = t * x, t * y
            casa = Elemento(self.TABULEIRO, x=x, y=y, w=t, h=t, cena=base)
        return [[casa(i, j) for i in range(linhas)] for j in range(colunas)]


if __name__ == "__main__":
    Tabuleiro().vai()