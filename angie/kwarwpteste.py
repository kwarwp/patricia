# patricia.angie.kwarwpteste.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto kwarwp - classe de testes

.. codeauthor:: Monica Novellino <monicanovellino@gmail.com@local.tipo>

Changelog
---------
.. versionadded::    20.09
        Descreva o que você adicionou no código.

"""

from _spy.vitollino.main import Jogo
from unittest import TestCase
# from unittest.mock import MagicMock
from angie.kwarwptora import Kwarwp, Indio
from angie.kwarwpart import Piche, Vazio, Oca, Tora, NULO
#sys.path.insert(0, os.path.abspath('../../libs'))

class Test_Kwarwp(TestCase):
    """ Teste do Jogo para ensino de programação.

    Vamos aqui definir um conjunto de URLs identificadoras das peças.
    """
    ABERTURA = "https://i.imgur.com/dZQ8liT.jpg"
    INDIO = "https://imgur.com/UCWGCKR.png"
    OCA = "https://imgur.com/dZQ8liT.jpg"
    PICHE = "https://imgur.com/tLLVjfN.png"
    TORA = "https://imgur.com/0jSB27g.png"
    
    def setUp(self):
        elts = self.elts = {}
        class FakeTaba:
            """ Permite capturar as chamadas de fala """
            def __init__(self):
                self.falou = ""
            def sai(self,*_):
                pass
            def fala(self, falou):
                self.falou = falou

        self.k = Kwarwp(Jogo)
        self.t = FakeTaba()
        self.LADO = Vazio.LADO
        
    def set_fake(self):
        """Cria objetos doublê que irão espionar o que estaria sendo feito com os originais."""
        elts = self.elts = {}
        """Coleção de imagens que indicam os Elementos Vitollino que são criados"""
        class FakeCena:
            """Usado para substituir a Cena original do Vitollino"""
            def __init__(self, *_, **__):
                pass
            def vai(self, *_, **__):
            pass

        class FakeElemento:
            """Usado para substituir o Elemento original do Vitollino

            Captura a imagem recebida e coloca na coleção de imagens **self.elts**.
            Também coleta os diversos parâmetros recebidos para que possam ser averiguados.
            """
            def __init__(self, img=0, x=0, y=0, w=0, h=0, vai=None, elts=elts, **kwargs):
                elts[img] = self
                """Insere este FakeElemento no dicionário, no verbete indicado pela imagem"""
                self.img, self.x, self.y, self.w, self.h, self.vai = img, x, y, w, h, vai
                self.destino, self._pos, self._siz = [None]*3
            def ocupa(self, destino):
                self.destino = destino.elt
            @property
            def elt(self):
                return self
            @property
            def siz(self):
                return self._siz
            @property
            def pos(self):
                return self._pos
            @siz.setter
            def siz(self, value):
                self._siz = value
            @pos.setter
            def pos(self, value):
                self._pos = value
        Vazio.VITOLLINO.a = FakeElemento
        """Troca o Elemento original pelo fake, na "maternidade""""
        Vazio.VITOLLINO.c = FakeCena
        """Troca a Cena original pelo fake, na "maternidade""""
        
        
