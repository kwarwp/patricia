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
class Kwarwp():
    VITOLLINO = None
    LADO = None

    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):    
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
        "&": Fab(self.coisa, f"{IMGUR}dZQ8liT.jpg"), # OCA
        "^": Fab(self.indio, f"{IMGUR}8jMuupz.png"), # INDIO
        ".": Fab(self.vazio, f"{IMGUR}npb9Oej.png"), # VAZIO
        "_": Fab(self.coisa, f"{IMGUR}sGoKfvs.jpg"), # SOLO
        "#": Fab(self.coisa, f"{IMGUR}ldI7IbK.png"), # TORA  
        "@": Fab(self.coisa, f"{IMGUR}tLLVjfN.png"), # PICHE
        "~": Fab(self.coisa, f"{IMGUR}UAETaiP.gif"), # CEU
        "*": Fab(self.coisa, f"{IMGUR}PfodQmT.gif"), # SOL
        "+": Fab(self.coisa, f"{IMGUR}uwYPNlz.png")}  # CERCA

        mapa = mapa if mapa != "" else self.mapa

        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].imagem)
        
        ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado, x=0, y=0, cena=cena, vai= self.executa) 
        sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena)
        
        self.taba = {(i, j): 
            fabrica[imagem].objeto(fabrica[imagem].imagem, x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
            
        cena.vai()
        return cena
        
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
        # self.o_indio = Indio(imagem, x=x, y=y, cena=cena)
        self.o_indio = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=self.o_indio)
        return vaga
        
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
    """    
    def anda(self):
        destino = (self.posicao[0]+1, self.posicao[1]-1)
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            vaga.acessa(self)"""
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
        
    def _valida_acessa(self, ocupante):
        self.ocupante.acessa(ocupante)
        
    def _acessa(self, ocupante):
        ocupante.ocupa(self)
        
    def ocupou(self, ocupante):
        self.vazio.ocupa(ocupante)
        self.ocupante = ocupante
        self.acessa = self._valida_acessa
        
    def ocupa(self, vaga):
        pass
        
    def sai(self):
        self.ocupante = self
        self.acessa = self._acessa
        
    @property
    def elt(self):
        return self._nada.elt
                
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo
    from _spy.vitollino.main import STYLE
    Kwarwp(Jogo, medidas=STYLE)
