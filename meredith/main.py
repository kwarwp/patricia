# patricia.meredith.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" 
Projeto para Estudo do Tutorial. 

.. codeauthor:: Erica Scheffel <ericascheffel@nce.ufrj.br>

"""
from collections import namedtuple as nt, deque
from kwarwp.kwarwpart import Vazio, Piche, Oca, Tora, NULO

IMGUR = "https://imgur.com/"
"""Prefixo do site imgur."""

MAPA_INICIO = """
@....&
......
......
.#.^..
"""
"""Mapa com o posicionamento inicial dos elementos."""
Ponto = nt("Ponto", "x y")
"""Par de coordenadas na direção horizontal (x) e vertiacal (y)."""
Rosa = nt("Rosa", "n l s o")
"""Rosa dos ventos com as direções norte, leste, sul e oeste."""

from _spy.vitollino.main import Cena, Elemento, STYLE

class JogoProxy():
    """ Proxy que enfileira comandos gráficos.
    :param vitollino: Empacota o engenho de jogo Vitollino.
    :param elt: Elemento que vai ser encapsulado pelo proxy.
    :param proxy: Referência para o objeto proxy parente.
    :param master: Determina se este elemento vai ser mestre de comandos."""

    def __init__(self, vitollino=None, elt=None, proxy=None, master=False):
        class AdaptaElemento(vitollino.a):
            """ Adapta um Elemento do Vitollino para agrupar ocupa e pos."""        

            def ocupa(self, ocupante=None, pos=(0, 0)):
                # super().elt.pos = pos
                #vitollino.a.pos.fset(self, pos)
                ocupante = ocupante or NULO
                ocupante.pos = pos
                # print(f"AdaptaElemento pos: {self.pos}")
                super().ocupa(ocupante) if ocupante else None

            def fala(self, texto):
                self.elt.html = texto
    
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
        :return: Proxy para um Elemento construído com estes argumentos."""
        return JogoProxy(elt=self.ae(*args, **kwargs), vitollino=self.v, proxy=self)

    def e(self, *args, **kwargs):
        """Método fábrica - Encapsula a criação de elementos ativos, que executam scripts
        :param args: coleção de argumentos posicionais.
        :param kwargs: coleção de argumentos nominais.
        :return: Proxy para um Elemento construído com estes argumentos."""    
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
        :return: Uma Cena do Vitollino construída com estes argumentos."""
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

class Vazio():
    """ Cria um espaço vazio na taba, para alojar os elementos do desafio.
    :param imagem: A figura representando o espaço vazio (normalmente transparente).
    :param x: Coluna em que o elemento será posicionado.
    :param y: Cinha em que o elemento será posicionado.
    :param cena: Cena em que o elemento será posicionado."""    
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
        """ Pedido por um ocupante para que desocupe a posição nela."""        
        self.ocupante = NULO
        self.acessa = self._acessa
        self.sair = self._sair

    def limpa(self):
        """ Pedido por um ocupante para ele seja eliminado do jogo."""        
        self._nada.ocupa(self.ocupante)
        """a figura do ocupante vai ser anexada ao elemento nada, que não é apresentado"""
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair

    def pegar(self, requisitante):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.
            :param requistante: O ator querendo pegar o objeto."""        
        self.ocupante.pegar(requisitante)
        
    def empurrar(self, requisitante, azimute):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.
            :param requistante: O ator querendo pegar o objeto."""        
        self.ocupante.empurrar(requisitante, azimute)

    def _valida_acessa(self, ocupante):
        """ Consulta o ocupante atual se há permissão para substituí-lo pelo novo ocupante.
            :param ocupante: O canditato a ocupar a posição corrente."""        
        self.ocupante.acessa(ocupante)
        
    def _acessa(self, ocupante):
        """ Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.        
        A responsabilidade de ocupar definitivamente a vaga é do candidato a ocupante
        Caso ele esteja realmente apto a ocupar a vaga e deve cahamar de volta ao vazio
        com uma chamada ocupou.
            :param ocupante: O canditato a ocupar a posição corrente."""        
        ocupante.ocupa(self)

    def acessar(self, ocupante, azimute):
        """ Faz o índio caminhar na direção em que está olhando."""        
        destino = (self.posicao[0]+azimute.x, self.posicao[1]+azimute.y)
        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            vaga.acessa(ocupante)

    def _sair(self):
        """Objeto tenta sair e recebe autorização para seguir"""
        self.ocupante.siga()      
    
    def _pede_sair(self):
        """Objeto tenta sair e consulta o ocupante para seguir"""
        self.ocupante.sair()      

    def ocupou(self, ocupante, pos=(0,0)):
        """ O candidato à vaga decidiu ocupá-la e efetivamente entra neste espaço.        
        :param ocupante: O canditato a ocupar a posição corrente.
        :param pos: A posição (atitude) do sprite do ocupante.
        Este ocupante vai entrar no elemento do Vitollino e definitivamente se tornar
        o ocupante da vaga. Com isso ele troca o estado do método acessa para primeiro
        consultar a si mesmo, o ocupante corrente usando o protocolo definido em
        **_valida_acessa ()**"""        
        self.vazio.ocupa(ocupante, pos)
        self.ocupante = ocupante
        self.acessa = self._valida_acessa
        self.sair = self._pede_sair

    @property        
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro.
        No caso do espaço vazio, vai retornar um elemento que não contém nada."""        
        return self._nada.elt
        
    def ocupa(self, vaga, *_):
        """ Pedido por uma vaga para que ocupe a posição nela.
        No caso do espaço vazio, não faz nada."""        
        pass
        
    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela."""        
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair
        
class Piche(Vazio):
    """ Poça de Piche que gruda o índio se ele cair nela.
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio."""

    def __init__(self, imagem, x, y, cena, taba):
        self.taba = taba
        self.vaga = taba
        self.lado = lado = self.LADO or 100
        self.posicao = (x//lado,y//lado-1)
        self.vazio = self.VITOLLINO.a(imagem, w=lado, h=lado, x=0, y=0, cena=cena)
        #self._nada = Kwarwp.VITOLLINO.a()
        self.ocupante = NULO
        self.empurrante = NULO        
        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado vago, aceitando ocupantes"""
        
    @property        
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso do espaço vazio, vai retornar um elemento que não contém nada."""        
        return self.vazio.elt

    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        :param vaga: A vaga que será ocupada pelo componente.
        No caso do piche, requisita que a vaga seja ocupada por ele."""
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga

    def _pede_sair(self):
        """Objeto tenta sair mas não é autorizado"""
        self.taba.fala("Você ficou preso no piche")

class Oca(Piche):
    """ A Oca é o destino final do índio, não poderá sair se ele entrar nela.
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio."""
    
    def _pede_sair(self):
        """Objeto tenta sair mas não é autorizado"""
        self.taba.fala("Você chegou no seu objetivo")

    def _acessa(self, ocupante):
        """ Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.
        A responsabilidade de ocupar definitivamente a vaga é do candidato a ocupante
        Caso ele esteja realmente apto a ocupar a vaga e deve cahamar de volta ao vazio
        com uma chamada ocupou.
        :param ocupante: O canditato a ocupar a posição corrente."""
        self.taba.fala("Você chegou no seu objetivo")
        ocupante.ocupa(self)
        
class Tora(Piche):
    """  A Tora é um pedaço de tronco cortado que o índio pode carregar ou empurrar.
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Linha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio."""    

    def pegar(self, requisitante):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.
            :param requistante: O ator querendo pegar o objeto."""        
        vaga = requisitante
        self.vaga.sai()
        # self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
        
    def empurrar(self, empurrante, azimute):
        """ Consulta o ocupante atual se há permissão para pegar e entregar ao requistante.
            :param requistante: O ator querendo pegar o objeto.
        """
        self.empurrante = empurrante
        self.vaga.acessar(self, azimute)
        self.empurrante = NULO
        
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        :param vaga: A vaga que será ocupada pelo componente.
        No caso do índio, requisita que a vaga seja ocupada por ele.
        """
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.empurrante.ocupa(self.vaga) if self.empurrante is not NULO else None
        self.empurrante.fala(self.empurrante.posicao) if self.empurrante is not NULO else None
        self.vaga = vaga

    @property
    def posicao(self):
        """ A propriedade posição faz parte do protocolo do double dispatch com o Indio .
        No caso da tora, retorna o a posição do atributo **self.vaga**."""        
        return self.vaga.posicao

    @posicao.setter
    def posicao(self, _):
        """ A propriedade posição faz parte do protocolo do double dispatch com o Indio .
        No caso da tora, é uma propriedade de somente leitura, não executa nada."""        
        pass

    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso da tora, retorna o elt do elemento do atributo **self.vazio**."""        
        return self.vazio.elt

    def _acessa(self, ocupante):
        """ Pedido de acesso a essa posição, delegada ao ocupante pela vaga.
        :param ocupante: O componente candidato a ocupar a vaga já ocupada pelo índio.
        No caso da tora, ela age como um obstáculo e não prossegue com o protocolo."""        
        pass
        
class Pedra(Tora):
    """  A Pedra é um uma coisa muito pesada que o índio só consegue empurrar.
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
        pass
        
class Nulo:
    """Objeto nulo que responde passivamente a todas as requisições."""
    def __init__(self):
        self.pegar = self.ocupa = self.nulo

    def nulo(self, *_, **__):
        """Método nulo, responde passivamente a todas as chamadas.
        :param _: aceita todos os argumentos posicionais.
        :param __: aceita todos os argumentos nomeados.
        :return: retorna o próprio objeto nulo."""        
        return self

NULO = Nulo()

class Indio():
    from collections import namedtuple as nt
    Ponto = nt("Ponto", "x y")
    """Par de coordenadas na direção horizontal (x) e vertiacal (y)."""
    Rosa = nt("Rosa", "n l s o")
    """Rosa dos ventos com as direções norte, leste, sul e oeste."""
    """ Faz o índio caminhar na direção em que está olhando."""
    
    AZIMUTE = Rosa(Ponto(0, -1),Ponto(1, 0),Ponto(0, 1),Ponto(-1, 0),)
    """Constante com os pares ordenados que representam os vetores unitários dos pontos cardeais."""
    def __init__(self, imagem, x, y, cena, taba, vitollino=None):
        self.vitollino = vitollino or Vazio.VITOLLINO
        self.lado = lado = Kwarwp.LADO
        self.azimute = self.AZIMUTE.n
        """índio olhando para o norte"""
        self.taba = taba
        self.vaga = self
        self.ocupante = NULO
        self.posicao = (x//lado,y//lado)
        self.indio = self.vitollino.e(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self.x = x
        """Este x provisoriamente distingue o índio de outras coisas construídas com esta classe"""
        if x:
            self.indio.siz = (lado*3, lado*4)
            """Define as proporções da folha de sprites"""
            self.gira()
            
    def ativa(self):
        """ Ativa o proxy do índio para enfileirar comandos."""
        #self.vitollino.ativa()
        self.indio.ativa()

    def passo(self):
        self.indio.executa()
            
    def pega(self):
        """tenta pegar o objeto que está diante dele"""
        destino = (self.posicao[0]+self.azimute.x, self.posicao[1]+self.azimute.y)
        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            vaga.pegar(self)

    def larga(self):
        """tenta largar o objeto que está segurando"""
        destino = (self.posicao[0]+self.azimute.x, self.posicao[1]+self.azimute.y)
        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            # self.ocupante.largar(vaga)
            vaga.acessa(self.ocupante)

    def ocupou(self, ocupante):
        """ O candidato à vaga decidiu ocupá-la e efetivamente entra neste espaço.
        :param ocupante: O canditato a ocupar a posição corrente.
        Este ocupante vai entrar no elemento do Vitollino e definitivamente se tornar
        o ocupante da vaga. Com isso ele troca o estado do método acessa para primeiro
        consultar a si mesmo, o ocupante corrente usando o protocolo definido em
        **_valida_acessa ()**"""    
        self.indio.ocupa(ocupante)
        self.ocupante = ocupante
        
    def mostra(self):
        """ Modifica a figura (Sprite) do índio mostrando para onde está indo. """
        sprite_col = sum(self.posicao) % 3
        """Faz com que três casas adjacentes tenha valores diferentes para a coluna do sprite"""
        sprite_lin = self.AZIMUTE.index(self.azimute)
        """A linha do sprite depende da direção dque índio está olhando"""
        self.indio.pos = (-self.lado*sprite_col, -self.lado*sprite_lin)

    def esquerda(self):
        """ Faz o índio mudar da direção em que está olhando para a esquerda."""
        self.azimute = self.AZIMUTE[self.AZIMUTE.index(self.azimute)-1]
        self.mostra()

    def direita(self):
        """ Faz o índio mudar da direção em que está olhando para a direita."""
        self.azimute = self.AZIMUTE[self.AZIMUTE.index(self.azimute)-3]
        self.mostra()

    def fala(self, texto=""):
        """ O índio fala um texto dado.
        :param texto: O texto a ser falado."""    
        self.taba.fala(texto)        
    
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar."""
        self.anda()
        
    def sai(self):
        """ Rotina de saída falsa, o objeto Indio é usado como uma vaga nula."""
        pass
        
    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso do índio, retorna o elt do elemento do atributo **self.indio**."""
        return self.indio.elt

    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        :param vaga: A vaga que será ocupada pelo componente.
        No caso do índio, requisita que a vaga seja ocupada por ele. """
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga

    def acessa(self, ocupante):
        """ Pedido de acesso a essa posição, delegada ao ocupante pela vaga.
        :param ocupante: O componente candidato a ocupar a vaga já ocupada pelo índio.
        No caso do índio, ele age como um obstáculo e não prossegue com o protocolo."""
        pass
     
    def anda(self):
        """Objeto tenta sair, tem que consultar a vaga onde está"""
        self.vaga.sair()

    def sair(self):
        """Objeto de posse do índio tenta sair e é autorizado"""
        self.vaga.ocupante.siga()

    def siga(self):
        """Objeto tentou sair e foi autorizado"""
        self._anda()

    def _anda(self):
        """ Faz o índio caminhar na direção em que está olhando."""
        destino = (self.posicao[0]+self.azimute.x, self.posicao[1]+self.azimute.y)
        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            vaga.acessa(self)

class Kwarwp():
    """ Jogo para ensino de programação.
    :param vitollino: Empacota o engenho de jogo Vitollino."""    
    VITOLLINO = None
    """Referência estática para obter o engenho de jogo."""
    LADO = None    
    """Referência estática para definir o lado do piso da casa."""
    
    def __init__(self, vitollino=None, mapa=None, medidas={}, indios=()):
        Vazio.VITOLLINO = self.v = vitollino()
        self.vitollino = vitollino
        """Referência estática para obter o engenho de jogo."""
        self.mapa = (mapa or MAPA_INICIO).split()
        """Cria um matriz com os elementos descritos em cada linha de texto"""
        self.taba = {}
        """Cria um dicionário com os elementos traduzidos a partir da interpretação do mapa"""
        self.o_indio = NULO
        self.os_indios = []
        """Instância do personagem principal, o índio, vai ser atribuído pela fábrica do índio"""
        self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        """Largura da casa da arena dos desafios, número de colunas e linhas no mapa"""
        Vazio.LADO = self.lado
        """Referência estática para definir o lado do piso da casa."""
        w, h = self.col *self.lado, self.lin *self.lado
        medidas.update(width=w, height=f"{h}px")
        self.indios = deque(indios or [Indio])
        self.cena = self.cria(mapa=self.mapa) if vitollino else None
                    
    def cria(self, mapa=" "):
        """ Fábrica de componentes.
        :param mapa: Um texto representando o mapa do desafio."""
        Fab = nt("Fab", "objeto imagem")
        """Esta tupla nomeada serve para definir o objeto construido e sua imagem."""
        
        fabrica = {
        "&": Fab(self.maloc, f"{IMGUR}dZQ8liT.jpg"), # OCA
        "^": Fab(self.indio, f"{IMGUR}UCWGCKR.png"), # INDIO
        "$": Fab(self.indio, f"{IMGUR}nvrwu0r.png"), # INDIA
        "p": Fab(self.indio, f"{IMGUR}HeiupbP.png"), # PAJE
        ".": Fab(self.vazio, f"{IMGUR}npb9Oej.png"), # VAZIO
        "_": Fab(self.coisa, f"{IMGUR}sGoKfvs.jpg"), # SOLO
        "#": Fab(self.atora, f"{IMGUR}0jSB27g.png"), # TORA
        "@": Fab(self.barra, f"{IMGUR}tLLVjfN.png"), # PICHE
        "~": Fab(self.coisa, f"{IMGUR}UAETaiP.gif"), # CEU
        "*": Fab(self.coisa, f"{IMGUR}PfodQmT.gif"), # SOL
        "|": Fab(self.coisa, f"{IMGUR}uwYPNlz.png")}  # CERCA
         
        """Dicionário que define o tipo e a imagem do objeto para cada elemento."""
        mapa = mapa if mapa != "" else self.mapa
        """Cria um cenário com imagem de terra de chão batido, céu e sol"""
        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].imagem)
        self.ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado-10, x=0, y=0, cena=cena, vai=self.passo,
                   style={"padding-top": "10px", "text-align": "center"})
        """No argumento *vai*, associamos o clique no céu com o método **executa ()** desta classe.
        O *ceu* agora é um argumento de instância e por isso é referenciado como **self.ceu**."""
    
        sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena, vai=self.executa)
        """No argumento *vai*, associamos o clique no sol com o método **esquerda ()** desta classe."""
        self.taba = {(i, j): fabrica[imagem].objeto(fabrica[imagem].imagem, x=i*lado, y=j*lado+lado, cena=cena)
             for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
        """Posiciona os elementos segundo suas posições i, j na matriz mapa"""
        cena.vai()
        return cena   
        
    def passo(self, *_):
        """ Ordena a execução do roteiro do índio."""
        # self.o_indio.esquerda()
        # self.v.executa()
        # self.o_indio.passo()
        [indio.passo() for indio in self.os_indios]          
        
    def fala(self, texto=""):
        """ O Kwarwp é aqui usado para falar algo que ficará escrito no céu."""
        self.ceu.elt.html = texto
        pass

    def esquerda(self, *_):
        """ Ordena a execução do roteiro do índio."""
        self.o_indio.esquerda()
        
    def executa(self, *_):
        """ Ordena a execução do roteiro do índio."""   
        # self.v.ativa()
        # JogoProxy.ATIVA = True
        # self.o_indio.ativa()
        # self.o_indio.executa()
        # [indio.ativa() and indio.executa() for indio in self.os_indios]
        self.os_indios[0].ativa()
        self.v.ativa()
        self.os_indios[0].executa()  
        
    def maloc(self, imagem, x, y, cena):
        """ Cria uma maloca na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        Cria uma vaga vazia e coloca o componente dentro dela."""
        coisa = Oca(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        return vaga
        
    def apedra(self, imagem, x, y, cena):
        """ Cria uma pedra na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        Cria uma vaga vazia e coloca o componente dentro dela.
        """
        coisa = Pedra(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa, taba=self)
        coisa.vazio.vai = lambda *_: self.o_indio.larga()
        return vaga    
    
    def barra(self, imagem, x, y, cena):
        """ Cria uma armadilha na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        Cria uma vaga vazia e coloca o componente dentro dela."""
        coisa = Piche(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa, taba=self)
        return vaga
        
    def sai(self, *_):
        """ O Kwarwp é aqui usado como uma vaga falsa, o pedido de sair é ignorado."""
        pass

    def ocupa(self, *_):
        """ O Kwarwp é aqui usado como um ocupante falso, o pedido de ocupar é ignorado."""
        pass
           
    def coisa(self,imagem, x, y, cena):
        """ Cria um elemento na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        Cria uma vaga vazia e coloca o componente dentro dela."""
        coisa = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        """o índio tem deslocamento zero, pois é relativo à vaga"""
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        """Aqui o índio está sendo usado para qualquer objeto, enquanto não tem o próprio"""
        return vaga
        
    def vazio(self, imagem, x, y, cena):
        """ Cria um espaço vazio na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado."""
        vaga = Vazio(imagem, x=x, y=y, cena=cena, ocupante=self)
        """ O Kwarwp é aqui usado como um ocupante nulo, que não ocupa uma vaga vazia."""
        return vaga   
    
    def indio(self, imagem, x, y, cena):
        """ Cria o personagem principal na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado."""
        self.o_indio = self.indios[0](imagem, x=1, y=0, cena=cena, taba=self, vitollino=self.v)
        """ O índio tem deslocamento zero, pois é relativo à vaga.
        O **x=1** serve para distinguir o indio de outros derivados."""
        self.o_indio.indio.vai = lambda *_: self.o_indio.pega()
        """o índio.vai é associado ao seu próprio metodo pega"""
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=self.o_indio)
        self.os_indios.append(self.o_indio)
        self.indios.rotate()
        """recebe a definição do próximo índio"""
        return vaga
        
    def ocupa(self, *_):
        """ O Kwarwp é aqui usado como um ocupante falso, o pedido de ocupar é ignorado."""
        pass
        
    def atora(self, imagem, x, y, cena):
        """ Cria uma tora na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
         Cria uma vaga vazia e coloca o componente dentro dela."""
        coisa = Tora(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa, taba=self)
        coisa.vazio.vai = lambda *_: self.o_indio.larga()
        return vaga
    
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo
    STYLE["width"]=600
    STYLE["height"]=500
    Kwarwp(Jogo)    
