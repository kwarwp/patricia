# patricia.tracy.main.py
_autor_ = "Lorena Pires Griõn"

from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vittolino.main import INVENTARIO as inv

tabuleiro ="http://www.infcross.com.br/mestrado/tabuleiro.jpg"
botao = "https://imgur.com/oC9lAgW.png"

   
def cena_principal():
    inicio = Cena(img=tabuleiro)
    inicio_e = Elemento(img=botao)
    inicio.vai()
    inicio_e.vai()
    
cena_principal() 