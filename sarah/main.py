# patricia.tracy.main.py
_autor_ = "Lorena Pires Griõn"

from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vittolino.main import INVENTARIO as inv

STYLE["width"] = 1150
STYLE["height"] = "550px"
tabuleiro ="http://www.infcross.com.br/mestrado/tabuleiro.jpg"

botao = "http://www.infcross.com.br/mestrado/botao.jpg"

   
def cena_principal():
    inicio = Cena(img=tabuleiro)
    inicio_e = Elemento(img=botao)
    inicio.vai()
    inicio_e.vai()
    
cena_principal() 