# patricia.anaconda.kwarwp_teste.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    20.09
        - Teste Vazio, Indio e Taba

"""
from _spy.vitollino.main import Jogo
from unittest import TestCase

from anaconda.kwarwp import Kwarwp, Indio, Vazio

class Test_Kwarwp(TestCase):
    """ Teste do Jogo para ensino de programação.

    Vamos aqui definir um conjunto de URLs identificadoras das peças.
    """
    VAZIO = "https://i.imgur.com/dZQ8liT.jpg"
    INDIO = "https://imgur.com/UCWGCKR.png"
    #OCA = "https://imgur.com/dZQ8liT.jpg"
    #PICHE = "https://imgur.com/tLLVjfN.png"
    #TORA = "https://imgur.com/0jSB27g.png"
    
class Test_Kwarwp(TestCase):
# ...
    def setUp(self):
        elts = self.elts = {}
        class FakeTaba:
            """Gera taba fake"""
            def __init__(self):
                pass
            def sai(self,*_):
                pass

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
    
def testa_cria(self):
    """ Cria o ambiente de programação Kwarwp."""
    self.set_fake()
    """instrumentaliza os objetos Vitollino"""
    cena = self.k.cria()
    self.assertIn(self.indio, self.elts)
    
    """Aqui perguntamos se a imagem do índio foi parar no dicionário elts"""

def testa_cria_indio(self):
    """ Cria o índio com a fábrica."""
    self.set_fake()
    cena = self.k.cria()
    coisa = self.k.taba[2,5]
    """Nesta posição da taba está colocada a vaga que tem o índio.

    É esperado que coisa.ocupante aponte para o índio criado.
    """
    self.assertIsInstance(coisa.ocupante,  Indio, f"but ocupante was {coisa.ocupante}")
    """Queremos saber se o objeto que está nesta vaga é uma instância da classe Indio.

    O terceiro parâmetro é uma mensagem que será enviada se o teste falhar.
    """
    self.assertEqual(100, coisa.lado, f"but coisa.lado was {coisa.lado}")
    indio = self.elts[self.indio]
    self.assertEqual(coisa.ocupante.indio, indio, f"but coisa.ocupante.indio was {coisa.ocupante.indio}")
    self.assertEqual((3, 5), indio.pos, f"but indio.pos was {indio.pos}")
    
def testa_cria_vazio(self):
    """ Cria o índio com a fábrica."""
    self.set_fake()
    cena = self.k.cria()
    coisa = self.k.taba[2,4]
    """Nesta posição da taba está colocada a vaga que tem o Vazio.

    É esperado que coisa.ocupante aponte para o vazio criado.
    """
    self.assertIsInstance(coisa.ocupante,  Vazio, f"but ocupante was {coisa.ocupante}")
    """Queremos saber se o objeto que está nesta vaga é uma instância da classe Vazio.

    O terceiro parâmetro é uma mensagem que será enviada se o teste falhar.
    """
    self.assertEqual(100, coisa.lado, f"but coisa.lado was {coisa.lado}")
    vazio = self.elts[self.vazio]
    self.assertEqual(coisa.ocupante.vazio, vazio, f"but coisa.ocupante.vazio was {coisa.ocupante.indio}")
    self.assertEqual((3, 5), vazio.pos, f"but indio.pos was {vazio.pos}")
    
def main():
    import unittest
    import kwarwp.htmlrunner as htmlrun
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Kwarwp)
    htmlrun.HTMLTestRunner().run(suite)

if __name__ == "__main__":
    main()