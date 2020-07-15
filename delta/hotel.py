# patricia.delta.hotel.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Anni Provietti <anniprovietti@gmail.com>

Changelog
---------
.. versionadded::    20.07
        

"""

import random
from _spy.vitollino.main import Cena, Elemento
from browser import document # importa o DOM para atribuir o evento de teclado

class Eventos:
	""" Associa um evento a uma imagem e captura eventos de teclado. """
	CENA_TABULEIRO = "http://activufrj.nce.ufrj.br/file/ProgOO/TAB_VAZIO.png?disp=inline"
	CARTA_VERSO= "http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline"
	#= "http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline"
	CARTA_PYCHARM = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline"
      CARTA_1
      CARTA_2
      CARTA_3
      CARTA_4
	
	def embaralhar(self):    
		s=[CARTA_VERSO,CARTA_PYCHARM,CARTA_3,4]

		random.shuffle(s,random.random)
      	
	def linkar (self):
		CARTA_1=s[0]
		CARTA_2=s[1]
		#CARTA_PYCHARM=s[2]
		#CARTA_VERSO=s[0]
		     
	def __init__(self):
		self.tabuleiro = Cena(self.CENA_TABULEIRO)
		self.carta1 = Elemento(self.CARTA_1, ,x=300,y=400 , cena=self.tabuleiro)
		self.carta2=Elemento(self.CARTA_2, , x=100, y=200, cena=self.tabuleiro)
		#self.verso2=Elemento(self.CARTA_VERSO2, , x=200, y=300, cena=self.tabuleiro)
        
       # self.pycharm=Elemento(self.CARTA_PYCHARM,,X=100,y=300,cena=self.tabuleiro)
        
        
	         
        
	def vai(self):
		""" mostra a cena da calçada. """
		self.tabuleiro.vai()
        
        	 
    	 
           

    
   
	#def mostrar_carta(self):
		#self.s.vai()
        
    
        
if __name__ == "__main__":
    Eventos().vai()



    

