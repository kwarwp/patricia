# patricia.sucuri.coralpart.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Kwarwp no Vitollino

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    20.08
        - Estudo da Herança 

"""

class Vazio():
    """ Cria um espaço vazio na taba, para alojar os elementos do desafio.
        :param imagem: A figura representando o espaço vazio (normalmente transparente).
        :param x: Coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
    """

    def __init__(self, imagem, x, y, cena, ocupante=None):
        self.lado = lado = Kwarwp.LADO # o lado previsto no tabuleiro
        self.posicao = (x//lado,y//lado-1) #o retorno será sempre um inteiro
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena) # o x e o y são substituiddos pelo mapa
        self._nada = Kwarwp.VITOLLINO.a() # descobrir o pq disso
        self.acessa = self._acessa #
        """É um método dinâmico que varia com o estado da vaga. Inicialmente é _aceesa, ou seja, vago e aceitanto ecupante"""
        self.ocupante = ocupante or self #Importante para o funcionamento dos métodos abaixo
        """O ocupante será definido pelo acessa, por default é o vazio"""
        self.acessa(ocupante)
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado leniente, aceitando saidas"""
        
    def _sair(self):
        self.ocupante.siga()

    def _pede_sair(self):
        self.ocupante.sair()
        
    def _valida_acessa(self, ocupante): 
        """ ESTE É O ESTADO OCUPADO
             Consulta o ocupante atual se há permissão para substituí-lo pelo novo ocupante.
            :param ocupante: O canditato a ocupar a posição corrente.
        """
        self.ocupante.acessa(ocupante)
        
    def _acessa(self, ocupante):
        """ESTE É O ESTADO VAGO
        Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.
        A responsabilidade de ocupar definitivamente a vaga é do candidato a ocupante
        Caso ele esteja realmente apto a ocupar a vaga e deve cahamar de volta ao vazio
        com uma chamada ocupou.
        :param ocupante: O canditato a ocupar a posição corrente.
        """
        ocupante.ocupa(self)
    
    def ocupou(self, ocupante):
        """ O candidato à vaga decidiu ocupá-la e efetivamente entra neste espaço.
        :param ocupante: O canditato a ocupar a posição corrente.
        Este ocupante vai entrar no elemento do Vitollino e definitivamente se tornar
        o ocupante da vaga. Com isso ele troca o estado do método acessa para primeiro
        consultar a si mesmo, o ocupante corrente usando o protocolo definido em
        **_valida_acessa ()**
        """
        self.vazio.ocupa(ocupante)
        self.ocupante = ocupante
        self.acessa = self._valida_acessa
        self.sair = self._pede_sair    
    
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        No caso do espaço vazio, não faz nada.
        """
        pass
        
    def sai(self): #
        """ Pedido por um ocupante para que desocupe a posição nela.
        """
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair
    
    @property
    def elt(self): 
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso do espaço vazio, vai retornar um elemento que não contém nada.
        """
        return self.vazio.elt
        #return self._nada.elt essa linha antes fazia com que o piche "colasse" no sol


class Tora(Piche):

    def __init__(self, imagem, x, y, cena, taba):
        self.taba = taba
        self.vaga = taba
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado,y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=0, y=0, cena=cena)
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado vago, aceitando ocupantes"""

    def ocupa(self, vaga):
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
        
    def _pede_sair(self):
        self.taba.fala("Você ficou preso MUAHAHAHA")
    


class Piche(Vazio):

    def __init__(self, imagem, x, y, cena, taba):
        self.taba = taba
        self.vaga = taba
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado,y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=0, y=0, cena=cena)
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado vago, aceitando ocupantes"""

    def ocupa(self, vaga):
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
        
    def _pede_sair(self):
        self.taba.fala("Você ficou preso MUAHAHAHA")

class Oca(Piche):

    def __init__(self, imagem, x, y, cena, taba):
        self.taba = taba
        self.vaga = taba
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado,y//lado-1)
        self.maloc = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=0, y=0, cena=cena) #ACHO QUE DEVE TROCAR POR PICHE AQUI
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado vago, aceitando ocupantes"""
    
    def _pede_sair(self):
        """Objeto tenta sair mas não é autorizado"""
        self.taba.fala("Você chegou no seu objetivo")
        
    def _acessa(self, ocupante):
        """ Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.

        A responsabilidade de ocupar definitivamente a vaga é do candidato a ocupante
        Caso ele esteja realmente apto a ocupar a vaga e deve cahamar de volta ao vazio
        com uma chamada ocupou.

            :param ocupante: O canditato a ocupar a posição corrente.
        """
        self.taba.fala("Você chegou no seu objetivo")
        ocupante.ocupa(self)        

    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso da oca, vai retornar o maloc.
        """
        return self.maloc.elt
        

class Nulo():
    
    def __init__(self):
        self.pegar = self.ocupa = self.nulo

    def nulo(self, *_, **__):
        """Método nulo, responde passivamente a todas as chamadas.

        :param _: aceita todos os argumentos posicionais.
        :param __: aceita todos os argumentos nomeados.
        :return: retorna o próprio objeto nulo.
        """
        return self

NULO = Nulo()


if __name__ == "__main__":
    