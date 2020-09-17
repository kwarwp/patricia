# patricia/sara.kwarwp.kwarwpart.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto Kwarwp Part.
.. codeauthor:: Paulo Assumpção <paulo.assump@gmail.com>

Changelog
---------

.. versionadded::    27.08
        Remove o Piche


.. versionadded::    20.08
        Orgniazação das classes do jogo Kwarwp.
        As seguintes classes foram movidas para esse módulo:
        - Vazio, 
        - Piche, 
        - Oca, 
        - Tora, 
        - NULO

"""


class Vazio():
    """ Cria um espaço vazio na taba, para alojar os elementos do desafio.
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
    """
    
    VITOLLINO, LADO = None, None

    def __init__(self, imagem, x, y, cena, taba, ocupante=None):
        self.lado = lado = self.LADO # or 100
        self.taba = taba
        self.posicao = (x//lado,y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.ocupante = ocupante or NULO
        """O ocupante se não for fornecido é encenado pelo próprio vazio, agindo como nulo"""
        self.acessa(ocupante)
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado leniente, aceitando saidas"""


    def _valida_acessa(self, ocupante):
        #print("Ocupante da vaga: ", ocupante)
        self.ocupante.acessa(ocupante)
        
    def _sair(self):
        """Objeto tenta sair e recebe autorização para seguir"""
        #print("Vou chamar o método siga da classe ", type(self.ocupante))
        self.ocupante.siga()
        

    def _pede_sair(self):
        """Objeto tenta sair e consulta o ocupante para seguir"""
        #print("Vou chamar o método sair da classe ", type(self.ocupante))
        self.ocupante.sair()
        
        
    def _acessa(self, ocupante):
        """ Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.
        A responsabilidade de ocupar definitivamente a vaga é do candidato a ocupante
        Caso ele esteja realmente apto a ocupar a vaga e deve cahamar de volta ao vazio
        com uma chamada ocupou.
            :param ocupante: O canditato a ocupar a posição corrente.
        """
        #print("Area vazia")
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
        
        
    @property        
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso do espaço vazio, vai retornar um elemento que não contém nada.
        """
        return self.vazio.elt
        
        
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        No caso do espaço vazio, não faz nada.
        """
        pass
        
        
    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela.
        """
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair
        
        
    def pegar(self, requisitante):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.
            :param requistante: O ator querendo pegar o objeto.
        """
        self.ocupante.pegar(requisitante)
        
    def limpa(self):
        """ Pedido por um ocupante para ele seja eliminado do jogo.
        """
        self._nada.ocupa(self.ocupante)
        """a figura do ocupante vai ser anexada ao elemento nada, que não é apresentado"""
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair
        
    def empurrar(self, requisitante, azimute):
        """ Consulta o ocupante atual se há permissão para empurrá-lo na direção do azimute.

            :param requistante: O ator querendo empurrar o objeto.
            :param azimute: A direção que se quer empurrar  o ocupante.
        """
        #print("Empurrando a Tora", self.ocupante)
        
        if type(self.ocupante) is Tora:
            self.ocupante.empurrar(requisitante, azimute)
        
        
    def acessar(self, ocupante, azimute):
        """ Obtém o Vazio adjacente na direção dada pelo azimute e envio ocupante para lá.
        """
        destino = (self.posicao[0]+azimute.x, self.posicao[1]+azimute.y)

        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            vaga.acessa(ocupante)

class Piche(Vazio):
    """ Poça de Piche que gruda o índio se ele cair nela.
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """
    def __init__(self, imagem, x, y, cena, taba):
    
        from sara.kwarwp import Kwarwp
        """Importando localmente o Kwarwp para evitar referência circular."""
        from _spy.vitollino.main import Jogo
        Kwarwp.VITOLLINO = vitollino()
        # Bad Smell... Isso em cima está muito estranho, mas funciona
        
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
        """ Pedido por uma vaga para que ocupe a posição nela.
        :param vaga: A vaga que será ocupada pelo componente.
        No caso do piche, requisita que a vaga seja ocupada por ele.
        """
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga


    def _pede_sair(self):
        """Objeto tenta sair mas não é autorizado"""
        self.taba.fala("Você ficou preso no piche")
        
    @property        
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso do espaço vazio, vai retornar um elemento que não contém nada.
        """
        return self.vazio.elt
        
    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela.
        """
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair
        self.vaga.limpa()


class Tora(Piche):
    """  A Tora é um pedaço de tronco cortado que o índio pode carregar ou empurrar.
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Linha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """
    def __init__(self, imagem, x, y, cena, taba):
        super(self.__class__, self).__init__(imagem, x, y, cena, taba)
        self.empurrante = NULO
        self.indio_segurando = False


    def pegar(self, requisitante):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.
            :param requistante: O ator querendo pegar o objeto.
        """
        vaga = requisitante
        self.vaga.sai()
        # self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
        self.indio_segurando = True

    @property
    def posicao(self):
        """ A propriedade posição faz parte do protocolo do double dispatch com o Indio .
        No caso da tora, retorna o a posição do atributo **self.vaga**.
        """
        return self.vaga.posicao

    @posicao.setter
    def posicao(self, _):
        """ A propriedade posição faz parte do protocolo do double dispatch com o Indio .
        No caso da tora, é uma propriedade de somente leitura, não executa nada.
        """
        pass

    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso da tora, retorna o elt do elemento do atributo **self.vazio**.
        """
        return self.vazio.elt

    def _acessa(self, ocupante):
        """ Pedido de acesso a essa posição, delegada ao ocupante pela vaga.
        :param ocupante: O componente candidato a ocupar a vaga já ocupada pelo índio.
        No caso da tora, ela age como um obstáculo e não prossegue com o protocolo.
        """
        pass
        
    def empurrar(self, empurrante, azimute):
        """ Registra o empurrante para uso no procolo e inicia dispathc com a vaga.

            :param requistante: O ator querendo pegar o objeto.
        """
        print("A Tora está sendo empurrada") 
        
        self.empurrante = empurrante
        # continue aqui com o início do double dispatch para ocupar a vaga na direção do azimute
        self.vaga.acessar(self, azimute)
        
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.

        :param vaga: A vaga que será ocupada pelo componente.

        No caso da tora, requisita que a vaga seja ocupada por ele.
        Também autoriza o empurrante a ocupar a vaga onde estava.
        """
        # o código usual do ocupa
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)

        self.empurrante.ocupa(self.vaga) # .xxx(zzz) if www else None -> continue o código
        self.empurrante = NULO
        self.vaga = vaga


class Oca(Piche):
    """ A Oca é o destino final do índio, não poderá sair se ele entrar nela.
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """


    def _pede_sair(self):
        """Objeto tenta sair mas não é autorizado"""
        self.taba.fala("Você chegou no seu objetivo!!!")


    def _acessa(self, ocupante):
        """ Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.
        A responsabilidade de ocupar definitivamente a vaga é do candidato a ocupante
        Caso ele esteja realmente apto a ocupar a vaga e deve cahamar de volta ao vazio
        com uma chamada ocupou.
            :param ocupante: O canditato a ocupar a posição corrente.
        """
        if type(ocupante) is Indio:
            self.taba.fala("Você chegou no seu objetivo")
        ocupante.ocupa(self)

        
    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso da tora, retorna o elt do elemento do atributo **self.vazio**.
        """
        return self.vazio.elt
        
        
    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela.
        """
        self.ocupante = self
        self.acessa = self._acessa
        


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