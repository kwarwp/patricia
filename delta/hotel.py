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
IMG_WIDTH=200
IMG_HEIGHT=200
class Carta():
	def _init_(self,imagem,posicao,cena):
		self.imagem=imagem
		self.posicao=posicao
		pos_x = 50 + self.posicao[0]*IMG_WIDTH
		pos_y = 50 + self.posicao[1]*IMG_HEIGHT
		Elemento(IMG_VERSO, x=pos_x, y=pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=cena)
	def cartas():
		if self.verso:
			Elemento(IMG_VERSO, x=pos_x, y=pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=cena)
		else: 
			Elemento(self.imagem, x=pos_x, y=pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=cena)
class Jogo:
	def vai(self):
		self.matriz()
	"matriz 2x2"
	def matriz(self):
		self.cena = Cena()
		list_cards=self.embaralha()
		self.card1a = Carta(IMG_LINUX, list_cards[0], self.cena)
		self.card1b = Carta(IMG_PYCHARM, list_cards[1], self.cena)
		self.card2a = Carta(IMG_LINUX, list_cards[2], self.cena)
		self.card2b = Carta(IMG_LINUX, list_cards[3], self.cena)
		self.cena.vai()
	def embaralha(self):   
		list_cards =  [(0,0), (1,0),(2,0),(3,0)]
		random.shuffle(list_cards,random.random)
		return list_cards
if __name__ == "__main__":
    Jogo().vai()
	

