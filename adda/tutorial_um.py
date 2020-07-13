# patricia.adda.tutorial_um.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Tutorial Um - respondendo dúvidas do SuperPython.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

- Como associar um evento a uma imagem
- Como combinar cenas em salas diferentes
- Como capturar o teclado

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""
from _spy.vitollino.main import Cena, Elemento

class Eventos:
    """ Associa um evento a uma imagem. """
    CENA_CALCADA = "https://i.imgur.com/zOxshRh.jpg"
    BANHISTA = "https://i.imgur.com/CWQ00XG.png"
    DARK_SIDE = "https://i.imgur.com/BKitDgi.png"
    
    def __init__(self):
        self.calcada = Cena(self.CENA_CALCADA)
        self.banhista = Elemento(self.BANHISTA, , x=100, y=200, cena=self.calcada)
        self.dark_side = Elemento(self.DARK_SIDE, , x=-1100, y=100, cena=self.calcada)
        self.calcada.elt.bind("keypress", self.anda_banhista)
        self.calcada.elt.setAttribute("tabindex", 0)
        self.calcada.elt.focus()
        
        self.banhista.elt.bind("mouseover", self.ve_dark)
        self.banhista.elt.bind("mouseout", self.ve_dark)
        self.muda = 1200
        
    def vai(self):
        self.calcada.vai()
        
    def anda_banhista(self, ev=None):
        keys = dict(x=1, y=-1)
        print(ev.keyCode)
        
        
    def ve_dark(self, ev=None):
        print(self.muda)
        self.dark_side.y += self.muda
        self.muda = - self.muda
        
        
        
if __name__ == "__main__":
    Eventos().vai()