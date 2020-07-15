import random
from _spy.vitollino.main import Cena,Elemento,Texto

def cartas():
	carta=[1,2,3]
	carta[0]=Cena(img="http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline")
	carta[0]=Cena(img="http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline")
	carta[1]=Cena(img="http://activufrj.nce.ufrj.br/file/ProgOO/Card_Linux.png?disp=inline")
	carta[2]=Cena(img="http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline")
	random.shuffle(carta,random.random)
	carta[0].vai()=carta[0](x=400,y=500)
	carta[1].vai()  
  
cartas()