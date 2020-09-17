# patricia.sara.kwarwtest.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto Kwarwp (módulo de teste)

.. codeauthor:: Paulo Assumpção <paulo.assump@gmail.com>

Changelog
---------
.. versionadded::    15.08
        Modulo de teste do jogo Kwarwp

"""
from _spy.vitollino.main import Jogo
from unittest import TestCase
#from unittest.mock import MagicMock

from sara.kwarwp import Kwarwp
from sara.kwarwp import Indio

from sara.kwarwpart import Vazio
from sara.kwarwpart import Piche
from sara.kwarwpart import Oca 
from sara.kwarwpart import Tora
from sara.kwarwpart import NULO
#sys.path.insert(0, os.path.abspath('../../libs'))

IMGUR = 'https://i.imgur.com/'

class Test_Kwarwp(TestCase):
    """ Teste do Jogo para ensino de programação.
    
    """
    
    ABERTURA = f"{IMGUR}dZQ8liT.jpg"
    INDIO = f"{IMGUR}UCWGCKR.png"
    OCA = f"{IMGUR}dZQ8liT.jpg"
    PICHE = f"{IMGUR}tLLVjfN.png"
    TORA = f"{IMGUR}0jSB27g.png"
    
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
        print(self.elts)
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
        """ Cria o piche e a oca com a fábrica."""
        self.set_fake()
        cena = self.k.cria()
        coisa = self.k.taba[1,3]
        self.assertIsInstance(coisa.ocupante,  Piche, f"but ocupante was {coisa.ocupante}")
        self.assertEqual(100, coisa.lado, f"but coisa.lado was {coisa.lado}")
        piche = self.elts[self.Piche]
        self.assertEqual(coisa.ocupante.vazio, piche, f"but coisa.ocupante.indio was {coisa.ocupante.vazio}")
        self.assertEqual((0, 0), piche.pos, f"but tora.pos was {tora.pos}")


    def testa_cria_tora(self):
        """ Cria a tora com a fábrica."""
        pass


    def testa_pega_tora_elimina_piche(self):
        """ Vai até a tora e pega e usa para eliminar o piche."""
        pass


    def testa_pega_tora(self):
        """ Vai até a tora e pega."""  
        cena = self.k.cria()
        pass


    def testa_larga_tora(self):
        """ Vai até a tora pega e larga."""
        pass


    def testa_pega_vazio_oca_piche(self):
        """ Vai até a piche, oca e vazio e tenta pegar."""
        pass

    def testa_move_indio(self):
        """ Move o índio, andando em frente."""
        pass

    def testa_prende_indio(self):
        """ Tenta mover o índio, mas fica preso."""
        pass

    def testa_chega_taba_indio(self):
        """ Chega no seu destino, tenta mover o índio, mas fica preso."""
        pass

    def testa_esquerda_indio(self):
        """ Move o índio, andando em frente, esquerda, frente."""
        pass

    def testa_volta_indio(self):
        """ Move o índio, andando em frente, meia volta, frente."""
        pass

def main():
    # from unittest import main
    # main()

    import unittest
    import kwarwp.htmlrunner as htmlrun
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Kwarwp)
    htmlrun.HTMLTestRunner().run(suite)        
    
if __name__ == "__main__":
    main()