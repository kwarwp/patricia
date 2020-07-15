# patricia.echo.main.py
""" Jogo Olimpíadas de Matemática20.07
        * NEW: O jogo original
"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
""" tabuleiro = Cena (img ="https://www.ibilce.unesp.br/Home/Departamentos/Matematica/2cejta/avancando-com-o-resto.png") """
img ="http://www.infcross.com.br/mestrado/tabuleiro.jpg"
img.resize(800,600,Image.ANTIALIAS)
tabuleiro = Cena (img)
tabuleiro.vai()