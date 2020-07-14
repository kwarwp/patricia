# patricia.naomi.main.py
#_author_= "Anni"
#nome="Papai Noel"
import random
from _spy.vitollino.main import Cena, Elemento
numero_de_presentes=2**45
#print("Olá,",nome,"!")
#print("Quantos presentes você pode distribuir?",numero_de_presentes)
class Eventos:
	py_charm="http://activufrj.nce.ufrj.br/file/info/ProgOO/Card_pycharm.png"
	tes_te="https://i.imgur.com/CWQ00XG.png"
	def _init_ (self):
	
		self.pycharm=Cena(self.py_charm)
		self.teste=Cena(self.tes_te)
	
	
	def vai(self):
	#s=[1,3,5,7,9]
	#random.shuffle(s,random.random)
	#print(s)
		self.teste.vai()