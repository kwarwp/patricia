# patricia.adda.quarto.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo de Tabuleiro Quarto.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    20.07
        Criando o tabuleiro.

.. versionadded::    20.07.01
        Criando Pino e Casa.

"""
from _spy.vitollino.main import Cena, Elemento, STYLE
from browser.html import SPAN
TAMANHO = 600
STYLE.update(width=TAMANHO, height=f"{TAMANHO}px")


class Pino(Elemento):
    """ Pinos do jogo quarto variando em cor, altura, forma e buraco
    
        Observação: Uma *folha sprite* é uma imagem contendo vários desenhos com peças
        que serão usados em um jogo.
    
        :param indice: O índice do pino na *folha sprite* (cada imagem tem 8 pinos).
        :param cor: Nome da imagem sprite com um conjunto de pinos claros ou escuros.
        :param casa: Casa original onde o pino vai ser colocado.
        :param dx: o intervalo horizontal em pixels entre duas figuras de pino na *folha sprite*.
        :param dy: o intervalo vertical em pixels entre duas figuras de pino na *folha sprite*.
    """
    PINOS = {}  # Coleção de todos pinos criados, serve para localizar um pino dado o nome.
    # COR é o dicionário com duas *folhas sprite* de pinos colocados no topo e no lado.
    COR = dict(topo="https://imgur.com/Wo6skC7.png", lado="https://imgur.com/chvIdvJ.png")
    MOD = dict(topo=2, lado=4)  # Número de figuras por linha em cada *folha sprite*.
    def __init__(self, indice, cor, casa, dx=101, dy=60):
        pino, modulo = self.COR[cor], self.MOD[cor]
        x, y, nome = indice // modulo * dx , (indice % modulo) * dy, f"{cor}{indice}"
        super().__init__(pino, x=8, y=-2, w=dx, h=dy, cena=casa, tipo="auto", tit=nome, drag=True,
        style={"background-position": f"{-x}px {-y}px"})
        self.PINOS[nome] = self  # adiciona este pino criado aqui (self) no dicionário de pinos.
        
    @staticmethod
    def pino(nome):
        """ Retorna o pino localizado dado o nome."""
        return Pino.PINOS[nome]
        
    @staticmethod
    def pinos(cor, table):
        """ Cria um conjunto de pinos de uma cor e aloca no dado tabuleiro."""
        casas = enumerate([casa for linha in table for casa in linha])
        return [Pino(indice, cor, casa) for indice, casa in casas]


class Casa(Elemento):
    """ Casa do jogo quarto, podendo ser do tabuleiro central ou adjacentes.
    
        Observação: Uma *folha sprite* é uma imagem contendo vários desenhos com peças
        que serão usados em um jogo.
    
        :param base: A cena em que este tabuleiro vai entrar.
        :param fundo: A imagem que representa esta casa.
        :param livre: Indica se a casa está livre ou ocupada quando for criada.
        :param t: Tamanho (altura e largura do desenho da casa, inicia em um oitavo do tabuleiro.
        :param x: A posição absoluta horizontal em casas que esta casa vai ser colocada.
        :param y: A posição absoluta vertical em casas que esta casa vai ser colocada.
        :param dx: O deslocamento horizontal em casas que esta casa tem em relação à esquerda.
        :param dy: O deslocamento vertical em casas que esta casa tem em relação ao topo.
        :param mx: Ajuste fino horizontal em pixels do posicionamento da casa.
        :param my: Ajuste fino vertical em pixels do posicionamento da casa.
    """
    def __init__(self, base, fundo, x, y, dx=0, dy=3, mx=0, my=0, livre=False, t=TAMANHO // 8):
        x, y = t * (x + dx) + mx, t * (y + dy) - my
        dropper = {f"{nome}{pino}": lambda ev, nome_pino, *_: self.entrar(nome_pino)
                    for nome in ("lado", "topo") for pino in range(8)}
        super().__init__(fundo, x=x, y=y, w=t, h=t, cena=base, drop=dropper)
        self.livre = livre
        
    def entrar(self,nome):
        """ Permite um pino entrar nesta casa se ela estiver livre.

            :param nome: O nome do pino que vai entrar na casa.
        """
        Pino.pino(nome).entra(self) if self.livre else None
        self.livre = False


class JogoDoQuarto:
    MADEIRA = "https://i.imgur.com/8mPjfYk.jpg"
    TABULEIRO = "https://i.imgur.com/yPFsdKw.png"
    MINITAB = "https://i.imgur.com/DjKe0KY.png"
    def __init__(self):
        self.lado = TAMANHO // 8
        self.tabuleiro = Cena(self.MADEIRA)
        margin = self.lado // 3
        self.tabua = self.table(self.tabuleiro, self.TABULEIRO, mx=margin, my=margin, livre=True)
        mx, my = self.lado//3, 0.66 * self.lado
        self.tab_topo = self.table(self.tabuleiro, self.MINITAB, 2, 4, 0, 1, 50, 50)
        self.tab_lado = self.table(self.tabuleiro, self.MINITAB, 4, 2, 5, 4, 50, 60)
        self.pin_topo = Pino.pinos("topo", self.tab_topo)
        self.pin_lado = Pino.pinos("lado", self.tab_lado)  # , dy=101.5)
        
    def vai(self):
        self.tabuleiro.vai()
    
    def table(self, base, fundo, linhas=5, colunas=5, dx=0, dy=3, mx=0, my=0, livre=False):
        return [[Casa(base, fundo, i, j, dx, dy, mx, my, livre)
                for j in range(linhas)] for i in range(colunas)]


if __name__ == "__main__":
    JogoDoQuarto().vai()