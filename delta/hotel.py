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
def Embaralha():

	def cartas():
		carta=[0,0,0]
		carta[0]=Elemento(img="http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline")
		carta[1]=Cena(img="http://activufrj.nce.ufrj.br/file/ProgOO/Card_Linux.png?disp=inline")
		carta[2]=Cena(img="http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline")
		random.shuffle(carta,random.random)
	def posicao(self):
		self.carta1=Elemento(self.carta[0],,x=200,y=400)
		self.carta2=Cena(self.carta[1],,x=100,y=100)
	def vai():
		self.carta1.vai()
		self.carta2.vai()


Embaralha()