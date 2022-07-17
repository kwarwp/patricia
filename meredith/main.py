# patricia.meredith.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" 
Projeto para Estudo do Tutorial. 

.. codeauthor:: Erica Scheffel <ericascheffel@nce.ufrj.br>

"""
from collections import namedtuple as nt
from kwarwp.kwarwpart import Vazio, Piche, Oca, Tora, NULO

IMGUR = "https://imgur.com/"
"""Prefixo do site imgur."""

MAPA_INICIO = """
@....&
......
......
.#.^..
"""

from _spy.vitollino.main import Cena, Elemento, STYLE

class Vazio():
    """ Cria um espaço vazio na taba, para alojar os elementos do desafio.
    :param imagem: A figura representando o espaço vazio (normalmente transparente).
    :param x: Coluna em que o elemento será posicionado.
    :param y: Cinha em que o elemento será posicionado.
    :param cena: Cena em que o elemento será posicionado."""    

    def __init__(self, imagem, x, y, cena, ocupante=None):
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado,y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.ocupante = ocupante or self
        """O ocupante será definido pelo acessa, por default é o vazio"""
        self.acessa(ocupante)
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado leniente, aceitando saidas"""
        
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
        
    def ocupou(self, ocupante):
        """ O candidato à vaga decidiu ocupá-la e efetivamente entra neste espaço.
        :param ocupante: O canditato a ocupar a posição corrente.
        Este ocupante vai entrar no elemento do Vitollino e definitivamente se tornar
        o ocupante da vaga. Com isso ele troca o estado do método acessa para primeiro
        consultar a si mesmo, o ocupante corrente usando o protocolo definido em
        **_valida_acessa ()**"""    
        self.vazio.ocupa(ocupante)
        self.ocupante = ocupante
        self.acessa = self._valida_acessa
        
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        No caso do espaço vazio, não faz nada."""
        pass
        
    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela."""
        self.ocupante = self
        self.acessa = self._acessa
        
    def _sair(self):
        """Objeto tenta sair e secebe autorização para seguir"""
        self.ocupante.siga()

    def _pede_sair(self):
        """Objeto tenta sair e consulta o ocupante para seguir"""
        self.ocupante.sair()   
        
    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso do espaço vazio, vai retornar um elemento que não contém nada."""
        return self._nada.elt
        
class Piche(Vazio):
    """ Poça de Piche que gruda o índio se ele cair nela.
        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio."""

    def __init__(self, imagem, x, y, cena, taba):
        from kwarwp.kwarapp import Kwarwp
        """Importando localmente o Kwarwp para evitar referência circular."""
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
    def __init__(self, imagem, x, y, cena, taba):
        self.lado = lado = Kwarwp.LADO
        self.azimute = self.AZIMUTE.n
        """índio olhando para o norte"""
        self.taba = taba
        self.vaga = self
        self.posicao = (x//lado,y//lado)
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self.x = x
        """Este x provisoriamente distingue o índio de outras coisas construídas com esta classe"""
        if x:
            self.indio.siz = (lado*3, lado*4)
            """Define as proporções da folha de sprites"""
            self.mostra()
            
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
    
    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
        #self.v = vitollino()
        Kwarwp.VITOLLINO = self.v = vitollino()
        """Cria um matriz com os elementos descritos em cada linha de texto"""
        self.mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas no mapa"""
        self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        Kwarwp.LADO = self.lado
        w, h = self.col *self.lado, self.lin *self.lado
        self.taba ={}
        """Dicionário que a partir de coordenada (i,J) localiza um piso da taba"""
        medidas.update(width=w, height=f"{h}px")
        self.cena = self.cria(mapa=self.mapa) if vitollino else None
        self.o_indio = None
        """Instância do personagem principal, o índio, vai ser atribuído pela fábrica do índio"""
            
    def cria(self, mapa=" "):
        from collections import namedtuple as nt
        Fab = nt("Fab", "objeto imagem")
        
        fabrica = {
        "&": Fab(self.coisa, f"https://imgur.com/zUbUHO7.png"), # OCA
        "^": Fab(self.indio, f"https://imgur.com/8jMuupz.png"), # INDIO
        ".": Fab(self.vazio, f"https://i.imgur.com/npb9Oej.png"), # VAZIO
        "_": Fab(self.coisa, f"https://i.imgur.com/sGoKfvs.jpg"), # SOLO
        "#": Fab(self.coisa, f"https://imgur.com/izPRRu7.png"), # TORA
        "@": Fab(self.coisa, f"https://imgur.com/eMEESZW.png"), # PICHE
        "~": Fab(self.coisa, f"https://i.imgur.com/UAETaiP.gif"), # CEU 
        "*": Fab(self.coisa, f"https://i.imgur.com/PfodQmT.gif")} # SOL
        
        """ Cria um cenário com imagem de terra de chão batido, céu e sol."""
        """O mapa pode pode ser o definido no argumento ou atributo da instância do Kwarwp."""
        mapa = mapa if mapa != "" else self.mapa

        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].imagem)
        self.ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado-10, x=0, y=0, cena=cena, vai=self.executa,
                   style={"padding-top": "10px", "text-align": "center"})
        """No argumento *vai*, associamos o clique no céu com o método **executa ()** desta classe.
        O *ceu* agora é um argumento de instância e por isso é referenciado como **self.ceu**."""
    
        sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena, vai=self.esquerda)
        """No argumento *vai*, associamos o clique no sol com o método **esquerda ()** desta classe."""
        self.taba = {(i, j): fabrica[imagem].objeto(fabrica[imagem].imagem, x=i*lado, y=j*lado+lado, cena=cena)
             for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
        """Posiciona os elementos segundo suas posições i, j na matriz mapa"""
        cena.vai()
        return cena   
        
    def fala(self, texto=""):
        """ O Kwarwp é aqui usado para falar algo que ficará escrito no céu."""
        self.ceu.elt.html = texto
        pass

    def esquerda(self, *_):
        """ Ordena a execução do roteiro do índio."""
        self.o_indio.esquerda()

    def executa(self, *_):
        """ Ordena a execução do roteiro do índio."""
        self.o_indio.executa()
    
    def executa(self, *_):
        """ Ordena a execução do roteiro do índio."""   
        self.o_indio.executa()  
        
    def maloc(self, imagem, x, y, cena):
        """ Cria uma maloca na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        Cria uma vaga vazia e coloca o componente dentro dela."""
        coisa = Oca(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        return vaga

    def barra(self, imagem, x, y, cena):
        """ Cria uma armadilha na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        Cria uma vaga vazia e coloca o componente dentro dela."""
        coisa = Piche(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
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
        # self.o_indio = Indio(imagem, x=x, y=y, cena=cena)
        self.o_indio = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        """o índio tem deslocamento zero, pois é relativo à vaga"""
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=self.o_indio)
        return vaga 
        
    def ocupa(self, *_):
        """ O Kwarwp é aqui usado como um ocupante falso, o pedido de ocupar é ignorado."""
        pass
    
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo
    STYLE["width"]=600
    STYLE["height"]=500
    Kwarwp(Jogo)    
