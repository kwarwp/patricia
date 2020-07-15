# patricia.delta.hotel.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Anni Provietti <anniprovietti@gmail.com>

Changelog
---------
.. versionadded::    20.07
        

"""

import random
from _spy.vitollino.main import Cena, Elemento, Texto
from browser import document


""" Imagens do Jogo da Memória: verso, pycharm, linux

"""
IMG_PYCHARM="http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline"
IMG_LINUX="http://activufrj.nce.ufrj.br/file/ProgOO/Card_Linux.png?disp=inline"
IMG_VERSO="http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline"
IMG_ALTURA=200
IMG_LARGURA=200
class Carta():
	def _init_(self,imagem,posicao,cena):
		self.imagem=imagem
		self.posicao=posicao
		pos_x = 50 + self.position[0]*IMG_WIDTH
		pos_y = 50 + self.position[1]*IMG_HEIGHT
		Elemento(self.imagem, x=pos_x, y=pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=cena)
	
class Jogo():
	def vai(self):
		self.matriz()
"matriz 2x2"
	def matriz_2x2(self):
		self.cena = Cena()
		self.card1a = Card(IMG_PYCHARM, list_cards[0], self.cena)
		self.card1b = Card(IMG_PYCHARM, list_cards[1], self.cena)
        
        self.card2a = Card(IMG_LINUX, list_cards[2], self.cena)
        self.card2b = Card(IMG_LINUX, list_cards[3], self.cena)
        
       
        self.cena.vai()
        
        random.shuffle(carta,random.random)
	"""def posicao(self):
		self.carta1=Elemento(self.carta[0],,x=200,y=400)"""
	carta[2].vai()
	

embaralha()