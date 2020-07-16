# patricia.tracy.main.py
autor = "Lorena Pires Griõn"

from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vittolino.main import INVENTARIO as inv

tabuleiro ="http://www.infcross.com.br/mestrado/tabuleiro.jpg"
botao = "https://imgur.com/oC9lAgW"

   
def cena_principal():
    inicio = Cena(img=tabuleiro)
    inicio_e = Elemento (img = botao, tit="Gravidade", style = dict(left= 70,top=170,bottom=100))
    inicio.vai()
    inicio_e.vai()
    
cena_principal()