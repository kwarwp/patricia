# patricia.bravo.main.py
""" Bravo - Jogo SupyCode: aprenda a programar com python.

.. codeauthor:: Isabel Hortencia (golf) <hortencia.garnica@nce.urj.br>
.. codeauthor:: Rosilane Lessa da Fonte (hotel) <rosilanefonte@gmail.com>
.. codeauthor:: Pedro Carvalho Ramos (india) <Pedro300501@gmail.com>
.. codeauthor:: Gabrielle Alves (juliet) <gabriellealves.baa@gmail.com>

Changelog
---------
.. versionadded::    16.07
       Pagina inicial do Game
"""

from _spy.vitollino.main import Cena, Elemento, INVENTARIO, STYLE, Musica
from bravo.india import teste
#from bravo.juliet import oi
#from bravo.hotel import cena


""" imagens"""
CENAINICIO = "https://i.imgur.com/mbt7XHq.png"
PLAY = "https://i.imgur.com/QiiOf5O.png"
FUNDO= "https://i.imgur.com/cdMKAka.png"
PERGUNTA = "https://i.imgur.com/fYmNuBj.png"
CODAPRENDA = "https://i.imgur.com/hQO8Nkj.png"
STYLE ["width"] = 1340
STYLE ["height"] = "600px"

"""criando a classe gameInicio"""
class gameInicio:
    """ criando o módulo init - inicio do jogo""" 
    def __init__(self):
        gameInicio = Cena(CENAINICIO)
        gameInicio.vai()
        self.dark = Elemento("",style=dict(width="1345px",height="600px"),cena=gameInicio)
        self.play = Elemento(PLAY, x=570, y=470,w=100,h=100, cena=gameInicio, vai = self.redimensiona)

    
    def redimensiona(self,ev=0):
        """criando o módulo para ir para a bravo.india"""
        redi = Cena()
        redi.vai = self.q2
        #prox = Cena(BOTAO, direita=teste ) <-- teste aqui tem que ser chamado teste()
        prox = Cena(CODAPRENDA, direita=teste() )
        prox.vai()

    """criando o módulo para ir para a bravo.india"""
    def q2(self):
        pass
        
if __name__ == "__main__":
    gameInicio()  # .vai() a classe gameInicio não tem o método vai
    #gameInicio()