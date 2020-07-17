# patricia.adda.tutorial_um.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Tutorial Um - respondendo dúvidas do SuperPython.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

- Como associar um evento a uma imagem
- Como combinar cenas em salas diferentes
- Como capturar o teclado

Classes neste modulo:

    :py:class:`Eventos` Exemplo de capturar eventos de mouse e teclado.

Changelog
---------
.. versionadded::    20.07
        Documentação do tutorial.

.. versionadded::    20.07.1
        Inclui um import.

"""
from _spy.vitollino.main import Cena, Elemento
from browser import document # importa o DOM para atribuir o evento de teclado
from adda.praia import cena

class Eventos:
    """ Associa um evento a uma imagem e captura eventos de teclado. """
    CENA_CALCADA = "https://i.imgur.com/zOxshRh.jpg"
    BANHISTA = "https://i.imgur.com/CWQ00XG.png"
    DARK_SIDE = "https://i.imgur.com/BKitDgi.png"
    
    def __init__(self):
        self.calcada = Cena(self.CENA_CALCADA, direita=cena)
        self.banhista = Elemento(self.BANHISTA, x=100, y=200, cena=self.calcada)
        self.dark_side = Elemento(self.DARK_SIDE, x=100, y=100, cena=self.calcada)
        self.dark_side.o = 0  # faz a opacidade virar zero, não mostra o letreiro
        document.bind("keydown", self.anda_banhista)  # captura o evento de teclado
        
        self.banhista.elt.bind("mouseover", self.ve_dark)  # usa o evento para mostrar "dark side"
        self.banhista.elt.bind("mouseout", self.ve_dark)  # usa o mesmo evento para ocultar "dark side"
        self.muda = 1
        
    def vai(self):
        """ mostra a cena da calçada. """
        self.calcada.vai()
        
    def anda_banhista(self, ev=None):
        """" Faz o banhista caminhar com a captura das setas. 
        
            :param ev: estrutura enviada pelo evento onde se recupera informações.
        """
        key = ev.keyCode # recupera o código da tecla enviada no evento
        # os códigos 37 e 38 são a seta para esquerda e para direita
        # se não for nenhum deles, anda zero
        key = key - 38 if key in [37, 39] else 0
        self.banhista.x += key # muda a posição de mais um ou menos um
        
    def ve_dark(self, ev=None):
        """" Faz o letreiro mostrar ou ocultar quando se passa o mouse no banhista. 
        
            :param ev: estrutura enviada pelo evento onde se recupera informações.
        """
        self.dark_side.o = self.muda  # muda a opacidade do letreiro
        self.muda = abs(self.muda - 1)  # chaveia para na próxima chamada inverter
        
        
        
if __name__ == "__main__":
    Eventos().vai()
