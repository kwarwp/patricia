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
from browser.html import SPAN
TAMANHO = 600
STYLE.update(width=TAMANHO, height=f"{TAMANHO}px")


class Tabuleiro:
    MADEIRA = "https://i.imgur.com/8mPjfYk.jpg"
    TABULEIRO = "https://i.imgur.com/yAeV5D6.jpg"
    MINITAB = "https://i.imgur.com/S3QJlDZ.jpg"
    def __init__(self):
        self.lado = TAMANHO // 8
        self.tabuleiro = Cena(self.MADEIRA)
        margin = self.lado // 3
        self.tabua = self.table(self.tabuleiro, self.TABULEIRO, mx=margin, my=margin)
        mx, my = self.lado//3, 0.66 * self.lado
        self.tab_alto = self.table(self.tabuleiro, self.MINITAB, 2, 4, 0, 1, 50, 50)
        self.tab_lado = self.table(self.tabuleiro, self.MINITAB, 4, 2, 5, 4, 50, 60)
        
    def vai(self):
        self.tabuleiro.vai()
    
    def table(self, base, fundo, linhas=5, colunas=5, dx=0, dy=3, mx=0, my=0):
        def casa(x, y):
            t = self.lado
            x, y = t * (x + dx) + mx, t * (y + dy) - my
            casa = Elemento(fundo, x=x, y=y, w=t, h=t, cena=base)
            casa.style.fontSize = "30px"
            casa.elt <= SPAN("", style={"fontSize":"90px", "margin-top":"-60px"})
        return [[casa(i, j) for j in range(linhas)] for i in range(colunas)]


if __name__ == "__main__":
    Tabuleiro().vai()