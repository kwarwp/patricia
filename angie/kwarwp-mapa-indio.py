# patricia.angie.kwarwp-mapa-indio.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto Kwarwp

.. codeauthor:: Monica Novellino <monicanovellino@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Montando o jogo usando mapa e o índio

"""
MAPA_INICIO = """
@....&
......
.....#
.#.^..
"""
    
MAPA_CERCA = """
++++++
.....&
......
...^..
++++++
"""
MAPA_ROCHA = """
+++++++
+..+..&
+..%..+
+^.+..+
+++++++
"""

class Indio():

    def __init__(self, imagem, x, y, cena):
        self.lado = lado = Kwarwp.LADO
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)

    def anda(self):
        """ Faz o índio caminhar na direção em que está olhando.
        """
        self.posicao = (self.posicao[0], self.posicao[1]-1)
        """Assumimos que o índio está olhando para cima, decrementamos a posição **y**"""
        self.indio.y = self.posicao[1]*self.lado
        self.indio.x = self.posicao[0]*self.lado

    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        self.anda()

class Kwarwp():
    """ Jogo para ensino de programação.

        :param vitollino: Empacota o engenho de jogo Vitollino.
    """
    VITOLLINO = None
    """Referência estática para obter o engenho de jogo."""
    LADO = None
    """Referência estática para definir o lado do piso da casa."""

    #self.o_indio = None XXXX -> etava no lugar errado, mandei para XXX[1]XXXX
    """Instância do personagem principal, o índio, vai ser atribuído pela fábrica do índio"""
    
    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
        Kwarwp.VITOLLINO = self.v = vitollino()
        """Cria um matriz com os elementos descritos em cada linha de texto"""
        self.mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas no mapa"""
        self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        Kwarwp.LADO = self.lado
        #XXX[1]XXXX ---> aqui que tinha que estar

        self.o_indio = None
        """Instância do personagem principal, o índio, vai ser atribuído pela fábrica do índio"""
        w, h = self.col *self.lado, self.lin *self.lado
        self.taba = {}
        """Dicionário que a partir de coordenada (i,J) localiza um piso da taba"""
        medidas.update(width=w, height=f"{h}px")
        self.cena = self.cria(mapa=self.mapa) if vitollino else None
        
    def cria(self, mapa="  "):
        
        from collections import namedtuple as nt
        Fab = nt("Fab", "objeto imagem")

        IMGUR = "https://imgur.com/"
        IIMGUR = "https://i.imgur.com/"
        fabrica = {
        "&": Fab(self.coisa, f"{IIMGUR}dZQ8liT.jpg"), # OCA
        "^": Fab(self.indio, f"{IMGUR}8jMuupz.png"), # INDIO
        ".": Fab(self.coisa, f"{IIMGUR}npb9Oej.png"), # VAZIO
        "_": Fab(self.coisa, f"{IIMGUR}sGoKfvs.jpg"), # SOLO
        "#": Fab(self.coisa, f"{IMGUR}ldI7IbK.png"), # TORA
        "@": Fab(self.coisa, f"{IIMGUR}tLLVjfN.png"), # PICHE
        "~": Fab(self.coisa, f"{IMGUR}UAETaiP.gif"), # CEU
        "*": Fab(self.coisa, f"{IMGUR}PfodQmT.gif"), # SOL
        "+": Fab(self.coisa, f"{IMGUR}uwYPNlz.png"),  # CERCA
        "%": Fab(self.coisa, f"{IMGUR}Ry3Vmsn.png") #ROCHA
        }

        mapa = mapa if mapa != "" else self.mapa

        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].imagem)
        ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena)

        self.taba = {(i, j): fabrica[imagem].objeto(
            fabrica[imagem].imagem, x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
            
        ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado, x=0, y=0, cena=cena, vai= self.executa)
        """No argumento *vai*, associamos o clique no céu com o método **executa ()** desta classe"""

        cena.vai()
        return cena
    
    def coisa(self, imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)        
        
    def indio(self, imagem, x, y, cena):
        self.o_indio = Indio(imagem, x=x, y=y, cena=cena)
        return self.o_indio
        
    def executa(self, *_):
        """ Ordena a execução do roteiro do índio.
        """
        self.o_indio.executa()

if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    #XXX[2]XXX faltou estas duas linhas do STYLE para esticar o solo
    STYLE["width"] = 600
    STYLE["heigth"] = "500px"
    Kwarwp(Jogo, mapa=MAPA_INICIO)
