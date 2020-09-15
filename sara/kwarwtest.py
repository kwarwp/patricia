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
# O import do TestCase está dando erro, Exception: <TypeError: Cannot read property '$methods' of undefined>
from unittest import TestCase
# from unittest.mock import MagicMock
from sara.kwarwp import Kwarwp, Indio
from sara.kwarwpart import Piche, Vazio, Oca, Tora, NULO
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
        """Troca o Elemento original pelo fake, na "maternidade"""
        Vazio.VITOLLINO.c = FakeCena
        """Troca a Cena original pelo fake, na "maternidade"""


    def testa_cria(self):
        """ Cria o ambiente de programação Kwarwp."""
        self.set_fake()
        """instrumentaliza os objetos Vitollino"""
        cena = self.k.cria()
        self.assertIn(self.INDIO, self.elts)
        """Aqui perguntamos se a imagem do índio foi parar no dicionário elts"""


    def testa_cria_indio(self):
        """ Cria o índio com a fábrica."""
        self.set_fake()
        cena = self.k.cria()
        coisa = self.k.taba[3,3]
        """Nesta posição da taba está colocada a vaga que tem o índio.

        É esperado que coisa.ocupante aponte para o índio criado.
        """
        self.assertIsInstance(coisa.ocupante,  Indio, f"but ocupante was {coisa.ocupante}")
        """Queremos saber se o objeto que está nesta vaga é uma instância da classe Indio.

        O terceiro parâmetro é uma mensagem que será enviada se o teste falhar.
        """
        self.assertEqual(100, coisa.lado, f"but coisa.lado was {coisa.lado}")
        indio = self.elts[self.INDIO]
        self.assertEqual(coisa.ocupante.indio, indio, f"but coisa.ocupante.indio was {coisa.ocupante.indio}")
        self.assertEqual((0, 0), indio.pos, f"but indio.pos was {indio.pos}")


    def testa_empurra_tora(self):
        """ Vai até a tora e empurra. O método set_fake não é usado."""
        cena = self.k.cria()
        vaga_tora = self.k.taba[1, 3]
        self.assertEqual(vaga_tora.taba,  self.k, f"but taba was {vaga_tora.taba}")
        tora = vaga_tora.ocupante
        pos = tora.posicao
        self.assertEqual((1, 3),  pos, f"but last pos was {pos}")
        indio = self.k.o_indio
        indio.esquerda()
        indio.anda()  # se posiciona diante da tora
        pos = indio.posicao
        self.assertEqual((2, 3),  pos, f"but indio pos was {pos}")
        vaga = indio.vaga  #  a vaga que o índio estava antes
        indio.empurra()  # agora empurra a tora
        pos = tora.posicao  # a tora estava em (1,3), checar se foi para (0,3)
        self.assertEqual((0, 3),  pos, f"but tora pos was {pos}")
        self.assertEqual(vaga.ocupante,  NULO, f"but vaga ocupante was {vaga.ocupante}")
        """Garantir que a vaga onde o índio estava foi desocupada"""
        vaga = indio.vaga
        indio.empurra()
        pos = tora.posicao #  a tora estava contra a parede, deve permanecer em (0,3)
        self.assertEqual((0, 3),  pos, f"but tora new pos was {pos}")
        self.assertEqual(vaga.ocupante,  indio, f"but vaga new  ocupante {vaga.ocupante}")
        """Garantir que o índio não se mexeu e continua na mesma vaga"""
        vaga = tora.vaga
        indio.pega()
        pos = tora.posicao
        self.assertEqual((1, 3),  pos, f"but tora taken pos was {pos}")
        self.assertEqual(vaga.ocupante,  NULO, f"but vaga taken  ocupante {vaga.ocupante}")
        self.assertEqual(tora.vaga,  indio, f"but tora vaga {tora.vaga}")
        indio.larga()  # larga a tora para ver se não deu um erro
        pos = tora.posicao  # verifica se as posições e as vagas estão ok
        self.assertEqual((0, 3),  pos, f"but tora drop pos was {pos}")
        self.assertEqual(vaga.ocupante,  tora, f"but vaga drop  ocupante {vaga.ocupante}")
        self.assertEqual(tora.vaga,  vaga, f"but tora drop vaga {tora.vaga}")
        
def main():
    import unittest
    import kwarwp.htmlrunner as htmlrun
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Kwarwp)
    htmlrun.HTMLTestRunner().run(suite)
    print("teste")

if __name__ == "__main__":
    main()