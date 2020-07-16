# patricia.sarah.main.py
""" Jogo Olimpíadas de Matemática20.07
        * NEW: O jogo original
"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
""" tabuleiro = Cena (img ="https://www.ibilce.unesp.br/Home/Departamentos/Matematica/2cejta/avancando-com-o-resto.png") """
STYLE["width"] = 1250
STYLE["height"] = "590px"
img ="http://www.infcross.com.br/mestrado/tabuleiro.jpg"
tabuleiro = Cena (img)
tabuleiro.vai()