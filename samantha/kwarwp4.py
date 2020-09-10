# patricia.samantha.kwarwp4.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Testando - EMPURRA A TORA

.. codeauthor:: Raquel M. M. Fernandes <raquelmachado4993@gmail.com>

Changelog
---------
.. versionadded::    10.09
        

"""
class Nulo:
    """Objeto nulo que responde passivamente a todas as requisições."""
    def __init__(self):
        self.pegar = self.ocupa = self.empurrar = self.nulo
        
    def nulo(self, *_, **__):
        """Método nulo, responde passivamente a todas as chamadas.
        
        :param _: aceita todos os argumentos posicionais.
        :param __: aceita todos os argumentos nomeados.
        :return: retorna o próprio objeto nulo.
        """
        return self 

NULO = Nulo()

class Vazio():
    """ Cria um espaço vazio na taba, para alojar os elementos do desafio.

        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Referência onde ele pode encontrar a taba.
        :param ocupante: Objeto que ocupa inicialmente a vaga.
    """
    VITOLLINO, LADO = None, None
    
    def __init__(self, imagem, x, y, cena, taba, ocupante=None):
        self.lado = lado = self.LADO # or 100
        self.taba = taba
        self.posicao = (x//lado,y//lado-1)
        self.vazio = self.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self._nada = self.VITOLLINO.a()
        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.ocupante = ocupante or NULO
        """O ocupante se não for fornecido é encenado pelo próprio vazio, agindo como nulo"""
        self.acessa(ocupante)
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado leniente, aceitando saidas"""
        
    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela.
        """
        self.ocupante = NULO
        self.acessa = self._acessa
        self.sair = self._sair

    def limpa(self):
        """ Pedido por um ocupante para ele seja eliminado do jogo.
        """
        self._nada.ocupa(self.ocupante)
        """a figura do ocupante vai ser anexada ao elemento nada, que não é apresentado"""
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair