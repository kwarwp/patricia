# patricia.amanda.main.py

# _author_ Rosilane Lessa
"""
SEGUNDA TELA

"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv

STYLE["width"] = 1250
STYLE["leight"]= "550px"

class tela:
	fundo= Cena (img = "https://i.imgur.com/DwSOcuv.png")
	siga = Elemento (img="https://i.imgur.com/kRmXNkz.png", style=dict(left=180, top=380, width=150, height="150px"))
	siga2 = Elemento (img="https://i.imgur.com/kRmXNkz.png", style=dict(left=850, top=380, width=150, height="150px"))
	siga.entra(fundo)
	siga2.entra(fundo)
	#siga.vai=fundo.vai
	#siga2.vai=fundo.vai
	fundo.vai()

tela()
