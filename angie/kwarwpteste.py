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
from kwarwp.kwarapp import Kwarwp, Indio
from kwarwp.kwarwpart import Piche, Vazio, Oca, Tora, NULO
#sys.path.insert(0, os.path.abspath('../../libs'))

class Test_Kwarwp(TestCase):
    """ Teste do Jogo para ensino de programação.
    
    """
    ABERTURA = "https://i.imgur.com/dZQ8liT.jpg"
    INDIO = "https://imgur.com/UCWGCKR.png"
    OCA = "https://imgur.com/dZQ8liT.jpg"
    PICHE = "https://imgur.com/tLLVjfN.png"
    TORA = "https://imgur.com/0jSB27g.png"
    
    def setUp(self):
        elts = self.elts = {}
        class FakeTaba:
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
        elts = self.elts = {}
        class FakeCena:
            def __init__(self, *_, **__):
                pass
            def vai(self, *_, **__):
                pass
            
        class FakeElemento:
            def __init__(self, img=0, x=0, y=0, w=0, h=0, vai=None, elts=elts, **kwargs):
                elts[img] = self
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
        Vazio.VITOLLINO.c = FakeCena
        
    def testa_cria(self):
        """ Cria o ambiente de programação Kwarwp."""
        self.set_fake()
        cena = self.k.cria()
        # self.assertIn("Vitollino_cria",  str(cena), cena)
        self.assertIn(self.INDIO, self.elts)

    def testa_cria_indio(self):
        """ Cria o índio com a fábrica."""
        self.set_fake()
        cena = self.k.cria()
        coisa = self.k.taba[3,3]
        self.assertIsInstance(coisa.ocupante,  Indio, f"but ocupante was {coisa.ocupante}")
        self.assertEqual(100, coisa.lado, f"but coisa.lado was {coisa.lado}")
        indio = self.elts[self.INDIO]
        self.assertEqual(coisa.ocupante.indio, indio, f"but coisa.ocupante.indio was {coisa.ocupante.indio}")
        self.assertEqual((0, 0), indio.pos, f"but indio.pos was {indio.pos}")

    def testa_cria_tora(self):
        """ Cria a tora com a fábrica."""
        self.set_fake()
        cena = self.k.cria()
        coisa = self.k.taba[1,3]
        self.assertIsInstance(coisa.ocupante,  Tora, f"but ocupante was {coisa.ocupante}")
        self.assertEqual(100, coisa.lado, f"but coisa.lado was {coisa.lado}")
        tora = self.elts[self.TORA]
        self.assertEqual(coisa.ocupante.vazio, tora, f"but coisa.ocupante.indio was {coisa.ocupante.vazio}")
        self.assertEqual((0, 0), tora.pos, f"but tora.pos was {tora.pos}")
        
    def testa_empurra_tora(self):
        """ Vai até a tora e empurra."""
        cena = self.k.cria()
        vaga_tora = self.k.taba[1, 3]
        self.assertEqual(vaga_tora.taba,  self.k, f"but taba was {vaga_tora.taba}")
        tora = vaga_tora.ocupante
        pos = tora.posicao
        self.assertEqual((1, 3),  pos, f"but last pos was {pos}")
        indio = self.k.o_indio
        indio.esquerda()
        indio.anda()
        pos = indio.posicao
        self.assertEqual((2, 3),  pos, f"but indio pos was {pos}")
        vaga = indio.vaga
        indio.empurra()
        pos = tora.posicao
        self.assertEqual((0, 3),  pos, f"but tora pos was {pos}")
        self.assertEqual(vaga.ocupante,  NULO, f"but vaga ocupante was {vaga.ocupante}")
        vaga = indio.vaga
        indio.empurra()
        pos = tora.posicao
        self.assertEqual((0, 3),  pos, f"but tora new pos was {pos}")
        self.assertEqual(vaga.ocupante,  indio, f"but vaga new  ocupante {vaga.ocupante}")
        vaga = tora.vaga
        indio.pega()
        pos = tora.posicao
        self.assertEqual((1, 3),  pos, f"but tora taken pos was {pos}")
        self.assertEqual(vaga.ocupante,  NULO, f"but vaga taken  ocupante {vaga.ocupante}")
        self.assertEqual(tora.vaga,  indio, f"but tora vaga {tora.vaga}")
        # vaga = tora.vaga
        indio.larga()
        pos = tora.posicao
        self.assertEqual((0, 3),  pos, f"but tora drop pos was {pos}")
        self.assertEqual(vaga.ocupante,  tora, f"but vaga drop  ocupante {vaga.ocupante}")
        self.assertEqual(tora.vaga,  vaga, f"but tora drop vaga {tora.vaga}")
        return indio, tora

    def testa_cria_piche_oca(self):
        """ Cria piche com a fábrica."""
        self.set_fake()
        cena = self.k.cria()
        coisa = self.k.taba[0,0]
        self.assertIsInstance(coisa.ocupante,  Piche, f"but ocupante was {coisa.ocupante}")
        self.assertEqual(100, coisa.lado, f"but coisa.lado was {coisa.lado}")
        tora = self.elts[self.PICHE]
        self.assertEqual(coisa.ocupante.vazio, piche, f"but coisa.ocupante.indio was {coisa.ocupante.vazio}")
        self.assertEqual((0, 0), piche.pos, f"but tora.pos was {tora.pos}")

    def testa_pega_tora_elimina_piche(self):
        """ Vai até a tora e pega e usa para eliminar o piche."""
        cena = self.k.cria()

        vaga_tora = self.k.taba[1, 3]
        self.assertEqual(vaga_tora.taba,  self.k, f"but taba was {vaga_tora.taba}")
        tora = vaga_tora.ocupante
        pos = tora.posicao
        self.assertEqual((1, 3),  pos, f"but last pos was {pos}")
        indio = self.k.o_indio
        indio.esquerda()
        indio.anda()
        pos = indio.posicao
        self.assertEqual((2, 3),  pos, f"but indio pos was {pos}")
        vaga = indio.vaga
        indio.pega()
        indio.anda()
        pos = indio.posicao
        self.assertEqual((2, 3),  pos, f"but indio pos was {pos}")
        """verifica se o indio andou para o lugar certo"""
        
        #
        self.assertEqual((2, 3),  pos, f"but indio pos was {pos}")
        """verifica se o indio andou para o lugar certo"""
        
        
        indio.direita()
        indio.anda()
        self.assertEqual((2, 3),  pos, f"but indio pos was {pos}")
        """verifica se o indio andou para o lugar certo"""
        r
        indio.anda()
        indio.larga()
        
        return indio, tora
        
    def testa_pega_tora(self):
        """ Vai até a tora e pega."""
        cena = self.k.cria()

        vaga_tora = self.k.taba[1, 3]
        self.assertEqual(vaga_tora.taba,  self.k, f"but taba was {vaga_tora.taba}")
        tora = vaga_tora.ocupante
        pos = tora.posicao
        self.assertEqual((1, 3),  pos, f"but last pos was {pos}")
        indio = self.k.o_indio
        indio.esquerda()
        indio.anda()
        pos = indio.posicao
        self.assertEqual((2, 3),  pos, f"but indio pos was {pos}")
        vaga = indio.vaga
        indio.pega()
        
        return indio, tora
        
    def testa_larga_tora(self):
        """ Vai até a tora pega e larga."""
        cena = self.k.cria()
        vaga_tora = self.k.taba[1, 3]
        self.assertEqual(vaga_tora.taba,  self.k, f"but taba was {vaga_tora.taba}")
        tora = vaga_tora.ocupante
        pos = tora.posicao
        self.assertEqual((1, 3),  pos, f"but last pos was {pos}")
        indio = self.k.o_indio
        indio.esquerda()
        indio.anda()
        pos = indio.posicao
        self.assertEqual((2, 3),  pos, f"but indio pos was {pos}")
        vaga = indio.vaga
        indio.pega()
        pos = tora.posicao
        self.assertEqual((1, 3),  pos, f"but tora taken pos was {pos}")
        self.assertEqual(vaga.ocupante,  NULO, f"but vaga taken  ocupante {vaga.ocupante}")
        self.assertEqual(tora.vaga,  indio, f"but tora vaga {tora.vaga}")
        # vaga = tora.vaga
        indio.larga()
        return indio, tora

    def testa_pega_vazio_oca_piche(self):
        """ Vai até a piche, oca e vazio e tenta pegar."""

    def testa_move_indio(self):
        """ Move o índio, andando em frente."""

    def testa_prende_indio(self):
        """ Tenta mover o índio, mas fica preso."""

    def testa_chega_taba_indio(self):
        """ Chega no seu destino, tenta mover o índio, mas fica preso."""

    def testa_esquerda_indio(self):
        """ Move o índio, andando em frente, esquerda, frente."""
        cena = self.k.cria()
        self.assertEqual((3, 3),  self.k, f"but taba was {vaga_tora.taba}")
        indio = self.k.o_indio
        indio.esquerda()
        indio.anda()
        pos = indio.posicao
        self.assertEqual((2, 3),  pos, f"but indio pos was {pos}")
        
        
    def testa_volta_indio(self):
        """ Move o índio, andando em frente, meia volta, frente."""
    
def main():
    # from unittest import main
    # main()

    import unittest
    import kwarwp.htmlrunner as htmlrun
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Kwarwp)
    htmlrun.HTMLTestRunner().run(suite)        
    
if __name__ == "__main__":
    main()