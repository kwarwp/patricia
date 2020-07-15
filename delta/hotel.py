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
	
	
    
	
	
		
	
	    
	def __init__(self):
		self.tabuleiro = Cena(self.CENA_TABULEIRO)
		  
		self.carta[0]= Elemento(self.CARTA_PYCHARM, ,x=100,y=300 , cena=self.tabuleiro)
		self.carta[1]= Elemento(self.CARTA_VERSO, , x=200, y=300, cena=self.tabuleiro)
		
           
        
       # self.pycharm=Elemento(self.CARTA_PYCHARM,,X=100,y=300,cena=self.tabuleiro)
	#def embaralhar(self):
		
		random.shuffle(self.carta,random.random)
		   
	
        
	def vai(self):
		""" mostra a cena da calçada. """
		self.tabuleiro.vai()
		
        
        	 
    	 
           

    
   
	#def mostrar_carta(self):
		#self.s.vai()
        
    
        
if __name__ == "__main__":
    Eventos().vai()



    

