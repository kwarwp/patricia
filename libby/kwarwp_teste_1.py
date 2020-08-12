# kwarwp.kwarwp.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Aula Kwarwp Charles.

.. codeauthor:: Charles Pimentel <pimentelufrj@gmail.com>

Changelog
---------
.. versionadded::    12.08
        Parte_3.

"""

from collections import namedtuple as nt

IMGUR = "https://imgur.com/"
"""Prefixo do site imgur."""
MAPA_INICIO = """
@....&
......
......
.#.^..
"""

Ponto = nt("Ponto", "x y")

Rosa = nt("Rosa", "n l s o")

class Vazio():
    
    def __init__(self, imagem, x, y, cena, ocupante=None):
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado,y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        
        self.ocupante = ocupante or self
        
        self.acessa(ocupante)
        self.sair = self._sair
        
        
    def _valida_acessa(self, ocupante):
        
        self.ocupante.acessa(ocupante)
        
    def _acessa(self, ocupante):
    
        ocupante.ocupa(self)
    
    def _sair(self):
        
        self.ocupante.siga()      
    
    def _pede_sair(self):
        
        self.ocupante.sair()      

    def ocupou(self, ocupante):
        alida_acessa ()**
        
        self.vazio.ocupa(ocupante)
        self.ocupante = ocupante
        self.acessa = self._valida_acessa
        self.sair = self._pede_sair

    @property        
    def elt(self):
        
        return self._nada.elt
        
    def ocupa(self, vaga):
        
        pass
        
    def sai(self):
        
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair
        


class Indio():
    
    AZIMUTE = Rosa(Ponto(0, -1),Ponto(1, 0),Ponto(0, 1),Ponto(-1, 0),)
      
    def __init__(self, imagem, x, y, cena, taba):
        self.lado = lado = Kwarwp.LADO
        self.azimute = self.AZIMUTE.n
        
        self.taba = taba
        self.vaga = self
        self.posicao = (x//lado,y//lado)
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self.x = x
        
        if x:
            self.indio.siz = (lado*3, lado*4)
            
            self.mostra()
    
    def mostra(self):
        
        sprite_col = sum(self.posicao) % 3
        
        sprite_lin = self.AZIMUTE.index(self.azimute)
        
        self.indio.pos = (-self.lado*sprite_col, -self.lado*sprite_lin)
    
    def esquerda(self):
        
        self.azimute = self.AZIMUTE[self.AZIMUTE.index(self.azimute)-1]
        self.mostra()
    
    def direita(self):
        
        self.azimute = self.AZIMUTE[self.AZIMUTE.index(self.azimute)-3]
        self.mostra()
    
    def fala(self, texto=""):
        
        self.taba.fala(texto)

    def anda(self):
        
        self.vaga.sair()      

    def sair(self):
        
        self.vaga.ocupante.siga()      

    def siga(self):
        
        self._anda()       

    def _anda(self):
        
        destino = (self.posicao[0]+self.azimute.x, self.posicao[1]+self.azimute.y)
        
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            
            vaga.acessa(self)
        
    def sai(self):
        
        pass
         
    def executa(self):
        
        self.anda()

    @property        
    def elt(self):
        
        return self.indio.elt
        
    def ocupa(self, vaga):
        
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
        if self.x:
            self.mostra()
        
    def acessa(self, ocupante):
        
        pass
        


class Piche(Vazio):


    def __init__(self, imagem, x, y, cena, taba):
        self.taba = taba
        self.vaga = taba
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado,y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=0, y=0, cena=cena)
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        
        self.sair = self._sair
        
        
    def ocupa(self, vaga):
        
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
    
    def _pede_sair(self):
        
        self.taba.fala("Você ficou preso no piche")       


class Oca(Piche):
        
    def _pede_sair(self):
        
        self.taba.fala("Você chegou no seu objetivo")       
        
    def _acessa(self, ocupante):
        
        self.taba.fala("Você chegou no seu objetivo")       
        ocupante.ocupa(self)


class Kwarwp():
    
    VITOLLINO = None
    
    LADO = None
    
    
    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
        Kwarwp.VITOLLINO = self.v = vitollino()
        self.mapa = mapa.split()
        
        self.taba = {}
        
        self.o_indio = None
    
        self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        
        Kwarwp.LADO = self.lado
        w, h = self.col *self.lado, self.lin *self.lado
        medidas.update(width=w, height=f"{h}px")
        self.cena = self.cria(mapa=self.mapa) if vitollino else None

    def cria(self, mapa=""):
        
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
        "|": Fab(self.coisa, f"{IMGUR}uwYPNlz.png")  # CERCA       
        }
    
        mapa = mapa if mapa != "" else self.mapa
        
        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].imagem)
        self.ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado-10, x=0, y=0, cena=cena, vai=self.executa,
                       style={"padding-top": "10px", "text-align": "center"})
        
        sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena, vai=self.esquerda)
        
        self.taba = {(i, j): fabrica[imagem].objeto(fabrica[imagem].imagem, x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
        
        cena.vai()
        return cena
        
    def fala(self, texto=""):
        
        self.ceu.elt.html = texto
        pass
        
    def sai(self, *_):
        pass
        
    def ocupa(self, *_):
        pass
        
    def esquerda(self, *_):
        
        self.o_indio.esquerda()
        
    def executa(self, *_):
        
        self.o_indio.executa()
        
    def maloc(self, imagem, x, y, cena):
        
        coisa = Oca(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        return vaga
        
    def barra(self, imagem, x, y, cena):
        
        coisa = Piche(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        return vaga
        
    def coisa(self, imagem, x, y, cena):
    
        coisa = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        return vaga
        
    def vazio(self, imagem, x, y, cena):
        
        vaga = Vazio(imagem, x=x, y=y, cena=cena, ocupante=self)
        
        return vaga
        
    def indio(self, imagem, x, y, cena):
         
        self.o_indio = Indio(imagem, x=1, y=0, cena=cena, taba=self)
        
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=self.o_indio)
        return vaga

def main(vitollino, medidas={}):
    
    Kwarwp(vitollino, medidas=medidas)
        
    
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE.update(width=600, height="500px")
    main(Jogo, STYLE)
