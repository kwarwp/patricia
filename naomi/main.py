from _spy.vitollino.main import Cena,Elemento,Texto

def cartas():
  carta=[1,2,3,4]
  carta[0]=Cena(img="http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline")
  
  carta[0].vai()
cartas()