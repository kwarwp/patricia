# patricia.sarah.main.py
# patricia.echo.main.py
""" Jogo Olimpíadas de Matemática20.07
        * NEW: O jogo original
        Autor: Grupo Echo (Aline, Lorena, Renato e Victoria)
"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv

""" tabuleiro = Cena (img ="https://www.ibilce.unesp.br/Home/Departamentos/Matematica/2cejta/avancando-com-o-resto.png") """

STYLE["width"] = 1150
STYLE["height"] = "550px"

tabuleiro ="http://www.infcross.com.br/mestrado/tabuleiro.jpg"
botao = "https://imgur.com/oC9lAgW.jpg"
img ="http://www.infcross.com.br/mestrado/tabuleiro.jpg"
#tabuleiro = Cena (img)
#tabuleiro.vai()


def cena_principal():
    inicio = Cena(img=tabuleiro)
    inicio_e = Elemento(img=botao)
    inicio.vai()
    inicio_e.vai()
    
cena_principal() 