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
TAMANHO = 680
STYLE.update(width=TAMANHO, height=f"{TAMANHO}px")


class Pino(Elemento):
    COR = dict(topo="https://imgur.com/h6JCa7Z.png", lado="https://imgur.com/0YKD7IM.png")
    MOD = dict(topo=2, lado=4)
    def __init__(self, indice, cor, casa, dx=101, dy=100):
        pino, modulo = self.COR[cor], self.MOD[cor]
        x, y = indice // modulo * dx , (indice % modulo) * dy
        super().__init__(pino, x=2, y=-25, w=dx, h=dy, cena=casa, tipo="auto",
        style={"background-position": f"{-x}px {-y}px"})
        
    @staticmethod
    def pinos(cor, table, dy=100):
        casas = enumerate([casa for linha in table for casa in linha])
        return [Pino(indice, cor, casa, dy=dy) for indice, casa in casas]


class Casa(Elemento):
    def __init__(self, base, fundo, x, y, dx=0, dy=3, mx=0, my=0, t=TAMANHO // 8):
        x, y = t * (x + dx) + mx, t * (y + dy) - my
        super().__init__(fundo, x=x, y=y, w=t, h=t, cena=base)


class Tabuleiro:
    MADEIRA = "https://i.imgur.com/8mPjfYk.jpg"
    TABULEIRO = "https://i.imgur.com/yPFsdKw.png"
    MINITAB = "https://i.imgur.com/DjKe0KY.png"
    def __init__(self):
        self.lado = TAMANHO // 8
        self.tabuleiro = Cena(self.MADEIRA)
        margin = self.lado // 3
        self.tabua = self.table(self.tabuleiro, self.TABULEIRO, mx=margin, my=margin)
        mx, my = self.lado//3, 0.66 * self.lado
        self.tab_topo = self.table(self.tabuleiro, self.MINITAB, 2, 4, 0, 1, 50, 50)
        self.tab_lado = self.table(self.tabuleiro, self.MINITAB, 4, 2, 5, 4, 50, 60)
        self.pin_topo = Pino.pinos("topo", self.tab_topo)
        self.pin_lado = Pino.pinos("lado", self.tab_lado, dy=101.5)
        
    def vai(self):
        self.tabuleiro.vai()
    
    def table(self, base, fundo, linhas=5, colunas=5, dx=0, dy=3, mx=0, my=0):
        return [[Casa(base, fundo, i, j, dx, dy, mx, my) for j in range(linhas)] for i in range(colunas)]


if __name__ == "__main__":
    Tabuleiro().vai()