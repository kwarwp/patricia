# patricia.tracy.main.py
__autor__ = "Lorena Pires Griõn"


from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
""" tabuleiro = Cena (img ="https://www.ibilce.unesp.br/Home/Departamentos/Matematica/2cejta/avancando-com-o-resto.png") """
STYLE["width"] = 1150
STYLE["height"] = "550px"
img ="http://www.infcross.com.br/mestrado/tabuleiro.jpg"
botao = "https://imgur.com/oC9lAgW"
tabuleiro = Cena (img)
botaovai = Cena(botao)
tabuleiro.vai()
botao.vai()