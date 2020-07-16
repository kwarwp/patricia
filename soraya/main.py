# patricia.soraya.main.py
__autor__ = "Isabel Hortencia Garnica"
__autor__ = "Gabriela"
__autor__ = "Pedro"
__autor__ = "Rosilene"
__version__ = "16.07.2020"

from _spy.vitollino.main import Cena, Elemento, INVENTARIO, STYLE, Musica
from texto.main import Texto

CENAINICIO = "https://i.imgur.com/mbt7XHq.png"
PLAY = "https://i.imgur.com/QiiOf5O.png"

STYLE ["width"] = 1340
STYLE ["height"] = "600px"

class gameInicio:
# start da classe, é aqui que o jogo se inicia
    def __init__(self):
        gameInicio = Cena(CENAINICIO)
        gameInicio.vai()
        dark = Elemento("",style=dict(width="1345px",height="600px"),cena=gameInicio)
        self.play = Elemento(PLAY, x=570, y=470,w=100,h=100, cena=gameInicio)

gameInicio()
