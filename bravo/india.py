# patricia.bravo.india.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Pedro Carvalho Ramos <Pedro300501@gnail.com>

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
        
        cena2 = Cena(img = fundo)
        self.cena1 = cena1 = Cena(img = fundo)
        cenas = Elemento(img = balao, style=dict(left=200, top=250, width=200, height="200px"))
        elementos = Elemento(img = balao2, style=dict(left=800, top=250, width=200, height="200px"))
        txt1 = Elemento(img = fr1, style=dict(left=400, top=150,width=400, height="150px")) 
        txt2 = Elemento(img = fr2, style=dict(left=350, top=100, width=480, height="140px"))
        txt1.entra(cena1)
        txt1.vai = cena2.vai 
        txt2.entra(cena2)
        gabi = Cena(elementof, direita=oi(), esquerda = cena2())        
        elementos.entra(cena2)
        elementos.vai = gabi.vai
        rosi = Cena(cenaf, direita=cena(),esquerda = cena2() )
        
        cenas.entra(cena2)
        cenas.vai = rosi.vai
        
   
        
    def vai(self, *_):
        """Tem que ter este método vai para ser usado como cena direita ou esquerda"""
        self.cena1.vai()


if __name__ == "__main__":
    """ A chamada de teste tem que estar dentro deste if"""
    teste().vai()    
    
