# patricia.kathryn.kwarwp6.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Montagem orientada do Kwarwp do zero! Parte 7

.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com

Changelog
---------
.. versionadded::    20.08
        Melhorando a movimentação do índio para a direita e a esquerda

"""
from collections import namedtuple as nt

IMGUR = "https://imgur.com/"
MAPA_INICIO = """
+++++++++
+...+..@+
+.......+
+...@###+
+^..+.&.+
+++++++++
"""
mapa_2 = """
...@..
......
..@&..
......
...^..
"""
class Kwarwp():
    VITOLLINO = None
    LADO = None

    def __init__(self, vitollino=None, mapa=mapa_2, medidas={}):    
        Kwarwp.VITOLLINO = self.v = vitollino()
        self.mapa = mapa.split()
        self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        Kwarwp.LADO = self.lado
        w, h = self.col*self.lado, self.lin*self.lado
        medidas.update(width=w, height=f"{h}px")
        self.taba = {}       
        self.o_indio = None
        self.cena = self.cria(mapa=self.mapa) if vitollino else None
            
    def cria(self, mapa = "  "):
        Fab = nt("Fab", "objeto imagem")
        fabrica = {
        "&": Fab(self.maloc, f"{IMGUR}dZQ8liT.jpg"), # OCA
        "^": Fab(self.indio, f"{IMGUR}UCWGCKR.png"), # INDIO
        ".": Fab(self.vazio, f"{IMGUR}npb9Oej.png"), # VAZIO
        "_": Fab(self.coisa, f"{IMGUR}sGoKfvs.jpg"), # SOLO
        "#": Fab(self.coisa, f"{IMGUR}ldI7IbK.png"), # TORA  
        "@": Fab(self.barra, f"{IMGUR}tLLVjfN.png"), # PICHE
        "~": Fab(self.coisa, f"{IMGUR}UAETaiP.gif"), # CEU
        "*": Fab(self.coisa, f"{IMGUR}PfodQmT.gif"), # SOL
        "+": Fab(self.coisa, f"{IMGUR}uwYPNlz.png")} # CERCA

        mapa = mapa if mapa != "" else self.mapa
        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].imagem)
        
        self.ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado-10, x=0, y=0, cena=cena, vai=self.executa,
                   style={"padding-top": "10px", "text-align": "center"})
        """No argumento *vai*, associamos o clique no céu com o método **executa ()** desta classe.
           O *ceu* agora é um argumento de instância e por isso é referenciado como **self.ceu**.
        """
        sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena, vai=self.esquerda)
        """No argumento *vai*, associamos o clique no sol com o método **esquerda ()** desta classe."""
        
        self.taba = {(i, j): 
            fabrica[imagem].objeto(fabrica[imagem].imagem, x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}            
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
        self.o_indio.executa()
    
    def coisa(self, imagem, x, y, cena):
        coisa = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        return vaga
        
    def vazio(self, imagem, x, y, cena):
        vaga = Vazio(imagem, x=x, y=y, cena=cena, ocupante=self)
        return vaga
        
    def indio(self, imagem, x, y, cena):
        self.o_indio = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=self.o_indio)
        return vaga
    
    def maloc(self, imagem, x, y, cena):
        """ Cria uma maloca na arena do Kwarwp na posição definida.
    
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
    
        Cria uma vaga vazia e coloca o componente dentro dela.
        """
        coisa = Oca(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        return vaga
    
    def barra(self, imagem, x, y, cena):
        """ Cria uma armadilha na arena do Kwarwp na posição definida.
    
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
    
        Cria uma vaga vazia e coloca o componente dentro dela.
        """
        coisa = Piche(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        return vaga
    
    def sai(self, *_):
        """ O Kwarwp é aqui usado como uma vaga falsa, o pedido de sair é ignorado."""
        pass
    
    def ocupa(self, *_):
        pass
        
"""Par de coordenadas na direção horizontal (x) e vertiacal (y)."""
Ponto = nt("Ponto", "x y")
"""Rosa dos ventos com as direções norte, leste, sul e oeste."""
Rosa = nt("Rosa", "n l s o")

class Indio():
    """Constante com os pares ordenados que representam os vetores unitários dos pontos cardeais."""
    AZIMUTE = Rosa(Ponto(0, -1),Ponto(1, 0),Ponto(0, 1),Ponto(-1, 0),)
    def __init__(self, imagem, x, y, cena, taba):
        """índio olhando para o norte"""
        self.azimute = self.AZIMUTE.n
        
        self.taba = taba
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado, y//lado)
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        
        """Este x provisoriamente distingue o índio de outras coisas construídas com esta classe"""
        self.x = x
        if x:
            """Define as proporções da folha de sprites"""
            self.indio.siz = (lado*3, lado*4)
            self.mostra()
            
    def executa(self):
        self.anda()
    
    def sai(self):
        pass
        
    @property
    def elt(self):
        return self.indio.elt
    
    def ocupa(self, vaga):
        self.vaga = vaga
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
    
    def acessa(self, ocupante):
        pass
        
    def mostra(self):
        """ Modifica a figura (Sprite) do índio mostrando para onde está indo."""
        sprite_col = sum(self.posicao) % 3
        """Faz com que três casas adjacentes tenha valores diferentes para a coluna do sprite"""
        sprite_lin = self.AZIMUTE.index(self.azimute)
        """A linha do sprite depende da direção dque índio está olhando"""
        self.indio.pos = (-self.lado*sprite_col, -self.lado*sprite_lin)
        self.anda()#adiciona o comando anda para retonar a imagem para o lado que o indio virou

    def esquerda(self):
        """ Faz o índio mudar da direção em que está olhando para a esquerda."""
        self.azimute = self.AZIMUTE[self.AZIMUTE.index(self.azimute)-1]
        self.executa()

    def direita(self):
        """ Faz o índio mudar da direção em que está olhando para a direita."""
        self.azimute = self.AZIMUTE[self.AZIMUTE.index(self.azimute)-3]
        self.mostra()

    def fala(self, texto=""):
        """ O índio fala um texto dado.
    
        :param texto: O texto a ser falado.
        """
        self.taba.fala(texto)
        
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
        """ Faz o índio caminhar na direção em que está olhando.
        """
        destino = (self.posicao[0]+self.azimute.x, self.posicao[1]+self.azimute.y)
        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
        vaga.acessa(self)  
        
class Vazio():
    def __init__(self, imagem, x, y, cena, ocupante=None):
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado, y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        self.ocupante = ocupante or self
        self.acessa(ocupante)
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado leniente, aceitando saidas"""
        
    def _valida_acessa(self, ocupante):
        self.ocupante.acessa(ocupante)
        
    def sai(self):
        self.ocupante = self
        self.acessa = self._acessa    
        
    def _sair(self):
        """Objeto tenta sair e secebe autorização para seguir"""
        self.ocupante.siga()

    def _pede_sair(self):
        """Objeto tenta sair e consulta o ocupante para seguir"""
        self.ocupante.sair()        
        
    def _acessa(self, ocupante):
        ocupante.ocupa(self)
        
    def ocupou(self, ocupante):
        self.vazio.ocupa(ocupante)
        self.ocupante = ocupante
        self.acessa = self._valida_acessa
        self.sair = self._pede_sair#chamar o pede_sair assim como o acessa chama o valida_acessa
        
    def ocupa(self, vaga):
        pass
        
    @property
    def elt(self):
        return self.vazio.elt
        
class Piche(Vazio):
    """ Poça de Piche que gruda o índio se ele cair nela.

        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :param taba: Representa a taba onde o índio faz o desafio.
    """

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
        return self.barra.elt
        
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
        return self.maloc.elt
        
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo
    from _spy.vitollino.main import STYLE
    Kwarwp(Jogo, medidas=STYLE)
