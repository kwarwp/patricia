# patricia.bravo.india.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Pedro Carvalho Ramos <mail@local.tipo>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""

from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from browser import html, alert, timer
from random import choice, shuffle
from bravo.juliet import oi
from bravo.hotel import cena

balao = "https://i.imgur.com/fbRhlGV.jpg"
balao2 = "https://i.imgur.com/rXfA4RE.jpg"
fundo = "https://i.imgur.com/N8qW02e.jpg"
fr2 = "https://i.imgur.com/9ZISyvv.jpg"
fr1 = "https://i.imgur.com/7PtVR2E.jpg"
cenaf = "https://i.imgur.com/KDOzJhl.jpg"
elementof = "https://i.imgur.com/8so9Azk.jpg"
STYLE["width"] , STYLE["height"] = 1200, "600px"

class teste:
    """ Classe responsavel por permitir a escolha
    entre o que sera aprendido,e ira chamar os outros codigos"""
    
    def __init__(self):
        
        cena = Cena(img = fundo)
        self.cena1 = cena1 = Cena(img = fundo)
        self.cenas = Elemento(img = balao, style=dict(left=200, top=250, width=200, height="200px"), cena = cena, vai = self.redimensiona)
        self.elementos = Elemento(img = balao2, style=dict(left=800, top=250, width=200, height="200px"), cena = cena, vai = self.redimensiona1)
        txt1 = Elemento(img = fr1, style=dict(left=400, top=150,width=400, height="150px")) #Texto(cena,"Vamos aprender a programar?")
        txt2 = Elemento(img = fr2, style=dict(left=350, top=100, width=480, height="140px"))#Texto(cena,"Escolha entre cenas ou elementos para começar.")
        txt1.entra(cena1)
        txt1.vai = cena.vai 
        txt2.entra(cena)
        
    def redimensiona(self,ev=0):
        """criando o módulo para ir para a bravo.cena"""
        redi = Cena()
        redi.vai = self.q2
        #prox = Cena(BOTAO, direita=teste ) <-- teste aqui tem que ser chamado teste()
        prox = Cena(cenaf, direita=teste() )
        prox.vai()
    def redimensiona1(self,ev=0):
        """criando o módulo para ir para a bravo.oi"""
        redi = Cena()
        redi.vai = self.q2
        #prox = Cena(BOTAO, direita=teste ) <-- teste aqui tem que ser chamado teste()
        prox = Cena(elementof, direita=teste() )
        prox.vai()        

    """criando o módulo para ir para a bravo.india"""
    def q2(self):
        pass
        
    def vai(self, *_):
        """Tem que ter este método vai para ser usado como cena direita ou esquerda"""
        self.cena1.vai()


if __name__ == "__main__":
    """ A chamada de teste tem que estar dentro deste if"""
    teste().vai()    
    
