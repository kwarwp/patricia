# patricia.amanda.main.py

# _author_ Rosilane Lessa
"""
SEGUNDA TELA

"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
from kelle.main import cena
#from alexa.main import oi

STYLE["width"] = 1250
STYLE["leight"]= "550px"

class tela:
	fundo= Cena (img = "https://i.imgur.com/DwSOcuv.png")
	siga = Elemento (img="https://i.imgur.com/kRmXNkz.png", style=dict(left=180, top=380, width=150, height="150px"))
	siga2 = Elemento (img="https://i.imgur.com/kRmXNkz.png", style=dict(left=850, top=380, width=150, height="150px"))
	siga.entra(fundo)
	siga2.entra(fundo)
	fundo.vai()
	#siga.vai= cena().vai
	#siga2.vai= oi().vai
    

tela()



#from grace.main import Praia
# = "20.07"
#__author__ = "Carlo"
#STYLE["width"] = 500
#CENA_CALCADA = "https://i.imgur.com/zOxshRh.jpg"
#BANHISTA = "https://i.imgur.com/CWQ00XG.png"


#class Calcada:
#    """ Representa uma cena da calçada da praia """
 #   def __init__(self):
#        """ Mostra a cena da praia """
#         self.cena = Cena(CENA_CALCADA, direita=Praia())
 #        self.banhista = Elemento(BANHISTA, x=100, y=200, cena=self.cena)
        #Cena(CENA_CALCADA).vai()
 #    def vai(self):
 #        """ Mostra a cena da praia """
 #        self.cena.vai()
        #Cena(CENA_CALCADA).vai()
    
# if __name__ == "__main__":
#     Calcada().vai()