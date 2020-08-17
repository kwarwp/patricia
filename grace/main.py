# patricia.grace.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""   Implementação do mapa no Kwarwp

.. codeauthor:: 

.. version:: 20.01.1
     - Mapa altera largura e comprimento automaticamente
     - Indio tem classe única
     - função executa 
     

"""
from _spy.vitollino.main import Elemento, Cena, STYLE
from delta.main import start 

STYLE["width"] = 900
STYLE["heigth"] = 900

LIVRO = "https://comunicamack.files.wordpress.com/2016/12/livro.png"
FUNDO = "https://img.elo7.com.br/product/original/1D27E33/painel-cenario-mundo-encantado-frete-gratis-cenario.jpg"

class Introduz():


    def __init__(self):
    
        self.fundo = Cena(FUNDO, direita = start())
        self.comp1 = Elemento(LIVRO, h = 100, w = 100, x = 0, y = 0, cena = self.fundo)
        
        self.comp1.elt.bind("click", self.opcao)
    
    def chama(self):
    
       self.fundo.vai()

    def opcao(self, event = None):
        
        start().vai()
        

if __name__ == "__main__":
    Introduz().chama()