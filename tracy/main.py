# patricia.tracy.main.py
_autor_ = "Lorena Pires Griõn"

from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vittolino.main import INVENTARIO as inv

tabuleiro ="http://www.infcross.com.br/mestrado/tabuleiro.jpg"
botao = "https://imgur.com/oC9lAgW"

   
def cena_principal():
    inicio = Cena(img=tabuleiro)
    inicio_e = Elemento (img = botao, tit="Gravidade", style = dict(left= 70,top=170, width=1150, height=550,bottom=100))
    lado1 = Cena(img=tabuleiro, direita =inicio)

    
    inicio_e.entra(inicio)

    inicio.vai()
    
cena_principal() 