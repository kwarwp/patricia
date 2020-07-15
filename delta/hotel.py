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


""" Imagens do Jogo da Memória: verso, pycharm, linux
"""
class Eventos:

	def cartas():
		carta=[0,0,0]
		carta[0]=Cena(img="http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline")
		carta[1]=Cena(img="http://activufrj.nce.ufrj.br/file/ProgOO/Card_Linux.png?disp=inline")
		carta[2]=Cena(img="http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline")
		random.shuffle(carta,random.random)
	def posicao(self):
		self.carta1=Cena(self.carta[0],,x=200,y=400)
		self.carta2=Cena(self.carta[1],,x=100,y=100)
		carta1.vai()
		carta2.vai()

if _name_=="_main_":
	Eventos().vai()