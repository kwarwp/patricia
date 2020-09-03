# patricia.soraya.kwarapp1.py
# SPDX-License-Identifier: GPL-3.0-or-later

""" Projeto descrição: Construir tela Kwarwp

.. codeauthor:: Isabel Hortencia  <hortencia.garnica@nce.urj.br>

Changelog
---------
.. versionadded::    03.09
       Criar um Mapa de inicio
"""


class Vazio():
    """ Cria um espaço vazio na taba, para alojar os elementos do desafio.
        :param imagem: A figura representando o espaço vazio (normalmente transparente).
        :param x: Coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
    """
    VITOLLINO = None
    """Referência estática para obter o engenho de jogo"""
    LADO = None
    """Referência estática para definir o lado do piso da casa"""

    def __init__(self, imagem, x, y, cena, taba, ocupante=None):

        self.lado = lado = Vazio.LADO or 100 # o lado previsto no tabuleiro
        self.posicao = (x//lado,y//lado-1) #o retorno será sempre um inteiro
        self.vazio = Vazio.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena) # o x e o y são substituiddos pelo mapa
        self._nada = Vazio.VITOLLINO.a() # descobrir o pq disso
        self.acessa = self._acessa #
        """É um método dinâmico que varia com o estado da vaga. Inicialmente é _aceesa, ou seja, vago e aceitanto ecupante"""
        self.ocupante = ocupante or self #Importante para o funcionamento dos métodos abaixo
        """O ocupante será definido pelo acessa, por default é o vazio"""
        self.acessa(ocupante)
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado leniente, aceitando saidas"""
        self.taba = taba
        """ Agora recebe um argumento taba, para que ache os vazios adjacentes"""
        
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
    
    def pegar(self, requisitante): 
        self.ocupante.pegar(requisitante)
        
    def empurrar(self, empurrante,azimute):
        """ Consulta o ocupante atual se há permissão para empurrá-lo na direção do azimute.
            :param requistante: O ator querendo empurrar o objeto.
            :param azimute: A direção que se quer empurrar  o ocupante.
        """
        #self.ocupante.empurrar(requisitante, azimute)    
        # Resgate do code funcional do Paulo
        if type(self.ocupante) is Tora:
            self.ocupante.empurrar(requisitante, azimute)    
    
    def acessar(self, ocupante, azimute):
        """ Obtém o Vazio adjacente na direção dada pelo azimute e envio ocupante para lá.
        """
        destino = (self.posicao[0]+azimute.x, self.posicao[1]+azimute.y)
        """A posição para onde o índio vai depende do vetor de azimute corrente"""     

        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            vaga.acessa(ocupante)

        
    def limpa(self):
        """ Pedido por um ocupante para ele seja eliminado do jogo.
        """    
        self._nada.ocupa(self.ocupante)
        """a figura do ocupante vai ser anexada ao elemento nada, que não é apresentado"""
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair
        
    @property
    def elt(self): 
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso do espaço vazio, vai retornar um elemento que não contém nada.
        """
        return self.vazio.elt
        #return self._nada.elt #essa linha antes fazia com que o piche "colasse" no sol


class Piche(Vazio):

    def __init__(self, imagem, x, y, cena, taba):
        # from sucuri.coral import Kwarwp
        self.taba = taba
        self.vaga = taba
        self.lado = lado = Vazio.LADO or 100
        self.posicao = (x//lado,y//lado-1)
        self.vazio = Vazio.VITOLLINO.a(imagem, w=lado, h=lado, x=0, y=0, cena=cena)
        self._nada = Vazio.VITOLLINO.a()
        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado vago, aceitando ocupantes"""

    def sai(self):
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair        
        self.vaga.limpa()
    
    def ocupa(self, vaga):
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
        
    def _pede_sair(self):
        self.taba.fala("Você ficou preso MUAHAHAHA")
        
    @property        
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso do espaço vazio, vai retornar um elemento que não contém nada.
        """
        return self.vazio.elt


class Tora(Piche):
    """  A Tora é um pedaço de tronco cortado que o índio pode carregar ou empurrar.
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Linha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """

    def sai():
        pass

    def pegar(self, requisitante):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.
            :param requistante: O ator querendo pegar o objeto.
        """
        vaga = requisitante
        self.vaga.sai()
        # self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
        
    def empurrar(self,requisitantee):

        """ Registra o empurrante para uso no procolo e inicia dispathc com a vaga.
            :param requistante: O ator querendo pegar o objeto.
            :param azimute: O local de destino da Tora
        """
        self.requisitante= requisitante
        # continue aqui com o início do double dispatch para ocupar a vaga na direção do azimute
        """ Faz a tora empurar o vazio adjacente.
        """
        destino = (self.posicao[0]+self.azimute.x, self.posicao[1]+self.azimute.y)
        """A posição para onde a tora vai depende do vetor de azimute corrente do vazio adjacente?"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            self.vaga.acessar(self,azimute)
        
    def ocupa(self,vaga):
    
        """ Pedido por uma vaga para que ocupe a posição nela.
        :param vaga: A vaga que será ocupada pelo componente.
        No caso da tora, requisita que a vaga seja ocupada por ele.
        Também autoriza o empurrante a ocupar a vaga onde estava.
        """
        #Código usual do ocupa
        """ Pedido por uma vaga para que ocupe a posição nela.
        :param vaga: A vaga que será ocupada pelo componente.
        No caso do índio, requisita que a vaga seja ocupada por ele.
        """
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self
        # self.vaga = vaga ..ver se há necessidade
        
        #elf.requixxx(zzz) if www else None -> continue o código
        #elf.empurrante = NULO
        #elf.vaga = vaga    

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


class Oca(Piche):
    
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
        
    def sai(self):
        """ Conserta os desvios de herança do Piche. A Oca não deve sair quando a tora sai."""
        self.ocupante = self
        self.acessa = self._acessa
        
    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso da oca, vai retornar o maloc.
        """
        return self.vazio.elt
        

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