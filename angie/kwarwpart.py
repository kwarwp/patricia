# patricia.angie.kwarwpart.py
# SPDX-License-Identifier: GPL-3.0-or-later

""" Jogo para ensino de programação Python.

    .. codeauthor:: monica novellino <monicanovellino@gmail.com>

    Classes neste módulo:
        - :py:class:`Vazio`     Espaço vago na arena do desafio.
        - :py:class:`Oca`       Destino final da aventura.
        - :py:class:`Piche`     Uma armadilha para prender o índio.
        - :py:class:`Tora`      Uma tora que o índio pode pegar.
        - :py:class:`Nulo`      Objeto nulo passivo a todas as requisições.

    Changelog
    ---------
    .. versionadded::    20.08.b0
        Moveu :class:`Vazio`, :class:`Oca`, :class:`Piche` para cá.
        Adicionou :class:`Tora` e classe :class:`Nulo`
    .. versionadded::    20.10
       Permite jogar a tora no piche
    .. versionadded::    20.10
       Permite empurrar a tora
        
"""


class JogoProxy():

    """ Proxy que enfileira comandos gráficos.

    :param vitollino: Empacota o engenho de jogo Vitollino.
    :param elt: Elemento que vai ser encapsulado pelo proxy.
    :param proxy: Referência para o objeto proxy parente.
    :param master: Determina se este elemento vai ser mestre de comandos.
    """

    def __init__(self, vitollino=None, elt=None, proxy=None, master=False):
        class AdaptaElemento(vitollino.a):
            """ Adapta um Elemento do Vitollino para agrupar ocupa e pos.

            """

            def ocupa(self, ocupante=None, pos=(0, 0)):
                # super().elt.pos = pos
                #vitollino.a.pos.fset(self, pos)
                ocupante = ocupante or NULO
                ocupante.pos = pos
                # print(f"AdaptaElemento pos: {self.pos}")
                super().ocupa(ocupante) if ocupante else None

        self.v = vitollino
        self.proxy = proxy or self
        self.master = master # or NULO
        self._corrente = self
        self.comandos = []
        self._ativa = False
        """Cria um referência para o jogo do vitollino"""
        self.ae = AdaptaElemento
        """Cria um referência o Adapador de Eelementos"""
        self.elt = elt

    @property
    def siz(self):
        """Propriedade tamanho"""
        return self.elt.siz

    def a(self, *args, **kwargs):
        """Método fábrica - Encapsula a criação de elementos

        :param args: coleção de argumentos posicionais.
        :param kwargs: coleção de argumentos nominais.
        :return: Proxy para um Elemento construído com estes argumentos.

        """
        return JogoProxy(elt=self.ae(*args, **kwargs), vitollino=self.v, proxy=self)

    def e(self, *args, **kwargs):
        """Método fábrica - Encapsula a criação de elementos ativos, que executam scripts

        :param args: coleção de argumentos posicionais.
        :param kwargs: coleção de argumentos nominais.
        :return: Proxy para um Elemento construído com estes argumentos.

        """
        return JogoProxy(elt=self.ae(*args, **kwargs), vitollino=self.v, proxy=self, master=True)

    def cria(self):
        """Fábrica do JogoProxy"""
        return self

    @property
    def corrente(self):
        """Retorna o proxy master acertado no parente"""
        return self.proxy._corrente

    @corrente.setter
    def corrente(self, mestre):
        """Estabelece o proxy master"""
        self._corrente = mestre

    def ativa(self):
        """Ativa bufferização do JogoProxy"""
        # JogoProxy.ATIVA = True
        self._ativa = True
        self.proxy.corrente = self

    def lidar(self, metodo_command):
        """Lida com modo de operação do JogoProxy - bufferizado ou não"""
        self.ativa() if self.master else None
        print(self._ativa, self.proxy._ativa, metodo_command)
        self.corrente._enfileira(metodo_command) if self.proxy._ativa else self._executa(metodo_command)

    def c(self, *args, **kwargs):
        """Método fábrica - Encapsula a criação de cenas - apenas delega.

        :param args: coleção de argumentos posicionais.
        :param kwargs: coleção de argumentos nominais.
        :return: Uma Cena do Vitollino construída com estes argumentos.

        """
        return self.v.c(*args, **kwargs)

    @siz.setter
    def siz(self, value):
        """Propriedade tamanho"""
        self.elt.siz = value

    @property
    def pos(self):
        """Propriedade posição"""
        return self.elt.pos

    @property
    def x(self):
        """Propriedade posição x"""
        return self.elt.x

    @property
    def y(self):
        """Propriedade posição y"""
        return self.elt.y

    @pos.setter
    def pos(self, value):
        """Propriedade posição"""
        def _command(val=value):
            self.elt.pos = val
        self.lidar(_command)

    def ocupa(self, ocupante=None, pos=(0, 0)):
        """Muda a posição e atitude de um elemento"""
        def _command(val=ocupante):
            destino = val.elt if val else None
            self.elt.ocupa(destino, pos)
        self.lidar(_command)

    def _enfileira(self, metodo_command):
        """Coloca um comando na fila"""
        self.comandos.append(metodo_command)

    def _executa(self, metodo_command):
        """Executa imediamente um comando, não põe na fila"""
        metodo_command()

    def executa(self, *_):
        """Tira e executa um comando na fila"""
        self.comandos.pop(0)() if self.comandos else None


class Nulo:
    """Objeto nulo que responde passivamente a todas as requisições."""
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
    
    def __init__(self, imagem, x, y, cena, ocupante=None, taba=None):
        from angie.kwarwptora import Kwarwp
        from _spy.vitollino.main import Jogo
        Kwarwp.VITOLLINO = Kwarwp.VITOLLINO or Jogo()
        self.lado = lado = Kwarwp.LADO or 100
        self.posicao = (x//lado,y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        self.taba = taba or NULO
                
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.ocupante = ocupante or NULO
        """O ocupante se não for fornecido é encenado pelo próprio vazio, agindo como nulo"""
        self.acessa(ocupante)
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado leniente, aceitando saidas"""
        
    def pegar(self, requisitante):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.

            :param requistante: O ator querendo pegar o objeto.
        """
        self.ocupante.pegar(requisitante)

        
    def _valida_acessa(self, ocupante):
        """ Consulta o ocupante atual se há permissão para substituí-lo pelo novo ocupante.

            :param ocupante: O canditato a ocupar a posição corrente.
        """
        self.ocupante.acessa(ocupante)
        
    def _acessa(self, ocupante):
        """ Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.
        
        A responsabilidade de ocupar definitivamente a vaga é do candidato a ocupante
        Caso ele esteja realmente apto a ocupar a vaga e deve cahamar de volta ao vazio
        com uma chamada ocupou.

            :param ocupante: O canditato a ocupar a posição corrente.
        """
        ocupante.ocupa(self)
        print(ocupante) 
    
    def _sair(self):
        """Objeto tenta sair e recebe autorização para seguir"""
        self.ocupante.siga()      
    
    def _pede_sair(self):
        """Objeto tenta sair e consulta o ocupante para seguir"""
        self.ocupante.sair()      

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

    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela.
        """
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair

    # Agora tem este método limpa, para eliminar o elemento ocupante do jogo.
    def limpa(self):
        """ Pedido por um ocupante para ele seja eliminado do jogo.
        """
        self._nada.ocupa(self.ocupante)
        """a figura do ocupante vai ser anexada ao elemento nada, que não é apresentado"""
        # faz as coisas normais que o método sai faz

    @property        
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .

        No caso do espaço vazio, vai retornar um elemento que não contém nada.
        """
        return self._nada.elt

    def empurrar(self, requisitante, azimute):
        """ Consulta o ocupante atual se há permissão para empurrá-lo na direção do azimute.

            :param requistante: O ator querendo empurrar o objeto.
            :param azimute: A direção que se quer empurrar  o ocupante.
        """
        self.ocupante.empurrar(requisitante, azimute)

    def acessar(self, ocupante, azimute):
        """ Obtém o Vazio adjacente na direção dada pelo azimute e envio ocupante para lá.
        """
        destino = (self.posicao[0]+azimute.x, self.posicao[1]+azimute.y)
        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        # o resto é semelhante ao código do _anda no Índio
        #inicio - trabalhando aqui
        
        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            vaga._acessa(self)
        #fim - trabalhando aqui    
            
        
class Piche(Vazio):
    """ Poça de Piche que gruda o índio se ele cair nela.

        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """

    def __init__(self, imagem, x, y, cena, taba):
        from angie.kwarwptora import Kwarwp
        from _spy.vitollino.main import Jogo
        Kwarwp.VITOLLINO = Kwarwp.VITOLLINO or Jogo()
        self.taba = taba
        self.vaga = taba
        self.lado = lado = Kwarwp.LADO or 100
        self.posicao = (x//lado,y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=0, y=0, cena=cena)
        # self._nada = Kwarwp.VITOLLINO.a()
        self.ocupante = NULO

        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado vago, aceitando ocupantes"""
        
    @property        
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .

        No caso do espaço vazio, vai retornar um elemento que não contém nada.
        """
        return self.vazio.elt
    
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        
        :param vaga: A vaga que será ocupada pelo componente.

        No caso do índio, requisita que a vaga seja ocupada por ele.
        """
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga

    def _pede_sair(self):
        """Objeto tenta sair mas não é autorizado"""
        self.taba.fala("Você ficou preso no piche")       

    # Agora Piche implementa sai:
    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela.
        """
        # faz as coisas normais que fazia quando usava o sai do Vazio
        self.vaga.limpa()

class Oca(Piche):
    """  A Oca é o destino final do índio, não poderá sair se ele entrar nela.
    
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """
    
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
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair   

class Tora(Piche):
    """  A Tora é um pedaço de tronco cortado que o índio pode carregar ou empurrar.
    
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Linha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """
        
    def pegar(self, requisitante):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.

            :param requistante: O ator querendo pegar o objeto.
        """
        vaga = requisitante
        self.vaga.sai()
        # self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga


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
        Consulta o espaço Vazio na direção do azimute em que foi empurrada. 
            :param requistante: O ator querendo pegar o objeto.
        """
        self.empurrante = empurrante
        
        # continue aqui com o início do double dispatch para ocupar a vaga na direção do azimute
        #inicio - trabalhando aqui
        #acessar(self, azimute)
        #acessa(ocupante)
        #ocupa(self)
        
        #destino = (self.posicao[0]+azimute.x, self.posicao[1]+azimute.y)
        #"""A posição para onde o índio vai depende do vetor de azimute corrente"""
        #taba = self.taba.taba
        #if destino in taba:
        #    vaga = taba[destino]
        #    """Recupera na taba a vaga para a qual o índio irá se transferir"""
        #    vaga.acessa(self)

        self.vaga.acessar(self, azimute) # acrescente o resto do comndo
        
        #fim - trabalhando aqui
        
        
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.

        :param vaga: A vaga que será ocupada pelo componente.

        No caso da tora, requisita que a vaga seja ocupada por ele.
        Também autoriza o empurrante a ocupar a vaga onde estava.
        """
        # ocódigo usual do ocupa
        #inicio - trabalhando aqui
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
        #fim - trabalhando aqui
        
        #self.empurrante # .xxx(zzz) if www else None -> continue o código
        #self.empurrante = NULO
        #self.vaga = vaga
        