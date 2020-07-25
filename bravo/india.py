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

balao = "https://i.imgur.com/fbRhlGV.jpg"#"https://i.pinimg.com/236x/d2/dd/c4/d2ddc45b2599d5fc60f03ec81c53bb6c.jpg"
balao2 = "https://i.imgur.com/rXfA4RE.jpg"#"https://i.pinimg.com/236x/14/3a/14/143a14c4535873de51301549ba96e051.jpg"
fundo = "https://i.imgur.com/N8qW02e.jpg"#"https://i.pinimg.com/originals/ca/a8/25/caa8256ded30c7703fadf79651d7833b.jpg"
fr2 = "https://i.imgur.com/9ZISyvv.jpg"#"https://i.pinimg.com/236x/7a/d6/c2/7ad6c2fdfd198c6903dee4425825ed9a.jpg"
fr1 = "https://i.imgur.com/7PtVR2E.jpg"#"https://i.pinimg.com/236x/4c/f8/6c/4cf86c786beb1c6457f31bf4fcd7ec99.jpg"
cenaf = "https://i.imgur.com/KDOzJhl.jpg"#"https://i.imgur.com/S5tAUe8.png"
elementof = "https://i.imgur.com/8so9Azk.jpg"
STYLE["width"] , STYLE["height"] = 1200, "600px"

class teste:
    """ Documente a classe aqui!"""
    
    """ tudo isto tinha que estar no __init__ !!!!!
    x = 0
    cena = Cena(img = fundo)
    cena1 = Cena(img = fundo)
    cenas = Elemento(img = balao, style=dict(left=200, top=250, width=200, height="200px"))
    elementos = Elemento(img = balao2, style=dict(left=800, top=250, width=200, height="200px"))
    txt1 = Elemento(img = fr1, style=dict(left=500, top=100, width=200, height="200px")) #Texto(cena,"Vamos aprender a programar?")
    txt2 = Elemento(img = fr2, style=dict(left=500, top=100, width=200, height="200px"))#Texto(cena,"Escolha entre cenas ou elementos para começar.")
    cena1.vai()
    txt1.entra(cena1)
    txt1.vai = cena.vai 
    txt2.entra(cena)
    txt2.vai()
    cenas.entra(cena)
    elementos.entra(cena)"""

    def __init__(self):
        #x = 0
        cena = Cena(img = fundo)
        self.cena1 = cena1 = Cena(img = fundo)
        self.cenas = Elemento(img = balao, style=dict(left=200, top=250, width=200, height="200px"), cena = cena, vai = self.redimensiona)
        self.elementos = Elemento(img = balao2, style=dict(left=800, top=250, width=200, height="200px"), cena = cena, vai = self.redimensiona1)
        txt1 = Elemento(img = fr1, style=dict(left=400, top=150,width=400, height="150px")) #Texto(cena,"Vamos aprender a programar?")
        txt2 = Elemento(img = fr2, style=dict(left=350, top=100, width=480, height="140px"))#Texto(cena,"Escolha entre cenas ou elementos para começar.")
        txt1.entra(cena1)
        txt1.vai = cena.vai 
        txt2.entra(cena)
        #txt2.vai()
        #cenas.entra(cena)
        #elementos.entra(cena)
        
    def redimensiona(self,ev=0):
        """criando o módulo para ir para a bravo.india"""
        redi = Cena()
        redi.vai = self.q2
        #prox = Cena(BOTAO, direita=teste ) <-- teste aqui tem que ser chamado teste()
        prox = Cena(cenaf, direita=teste() )
        prox.vai()
    def redimensiona1(self,ev=0):
        """criando o módulo para ir para a bravo.india"""
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
    
