# patricia.echo.main.py
""" Jogo Olimpíadas de Matemática20.07
        * NEW: O jogo original
"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["leight"]= "550px"
tabuleiro = Cena (img ="https://www.ibilce.unesp.br/Home/Departamentos/Matematica/2cejta/avancando-com-o-resto.png")
tabuleiro.vai()