# patricia.roxanne.main.py

from _spy.vitollino.main import *

STYLE['width'] = 740

fundo_jogo = 'https://i.pinimg.com/originals/7f/d6/54/7fd654e4ed2675f4606bd72177eb1fb2.jpg'

class JogoDaVelha:
	def __init__(self, fundo_jogo):
		self.fundo_jogo = Cena(img=fundo_jogo)
        
        
JogoDaVelha(fundo_jogo)