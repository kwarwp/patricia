# patricia.meredith.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" 
Projeto para Estudo do Tutorial. 

.. codeauthor:: Erica Scheffel <ericascheffel@nce.ufrj.br>

"""
MAPA_INICIO = """
@....&
......
......
.#.^..
"""

from _spy.vitollino.main import Cena, Elemento, STYLE

class Indio():
    def __init__(self, imagem, x, y, cena):
        self.lado = lado = Kwarwp.LADO
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)

class Kwarwp():
    """ Jogo para ensino de programação.
    :param vitollino: Empacota o engenho de jogo Vitollino.
    """
    VITOLLINO = None
    """Referência estática para obter o engenho de jogo."""
    LADO = None    
    """Referência estática para definir o lado do piso da casa."""
    
    """GLIFOS = {
    "&": "https://imgur.com/zUbUHO7.png", # OCA
    "^": "https://imgur.com/8jMuupz.png", # INDIO
    ".": "https://i.imgur.com/npb9Oej.png", # VAZIO
    "_": "https://i.imgur.com/sGoKfvs.jpg", # SOLO
    "#": "https://imgur.com/kNoAnjR.png", # TORA
    "@": "https://imgur.com/eMEESZW.png", # PICHE
    "~": "https://i.imgur.com/UAETaiP.gif", # CEU 
    "*": "https://i.imgur.com/PfodQmT.gif"} # SOL"""

    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
        #self.v = vitollino()
        Kwarwp.VITOLLINO = self.v = vitollino()
        """Cria um matriz com os elementos descritos em cada linha de texto"""
        self.mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas no mapa"""
        self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        Kwarwp.LADO = self.lado
        w, h = self.col *self.lado, self.lin *self.lado
        self.taba = {}
        """Dicionário que a partir de coordenada (i,J) localiza um piso da taba"""
        medidas.update(width=w, height=f"{h}px")
        self.cena = self.cria(mapa=self.mapa) if vitollino else None

    def cria(self, mapa=" "):
        from collections import namedtuple as nt
        Fab = nt("Fab", "objeto imagem")
        
        fabrica = {
        "&": Fab(self.coisa, f"https://imgur.com/zUbUHO7.png"), # OCA
        "^": Fab(self.indio, f"https://imgur.com/8jMuupz.png"), # INDIO
        ".": Fab(self.vazio, f"https://i.imgur.com/npb9Oej.png"), # VAZIO
        "_": Fab(self.coisa, f"https://i.imgur.com/sGoKfvs.jpg"), # SOLO
        "#": Fab(self.coisa, f"https://imgur.com/kNoAnjR.png"), # TORA
        "@": Fab(self.coisa, f"https://imgur.com/eMEESZW.png"), # PICHE
        "~": Fab(self.coisa, f"https://i.imgur.com/UAETaiP.gif"), # CEU 
        "*": Fab(self.coisa, f"https://i.imgur.com/PfodQmT.gif")} # SOL
        
        """ Cria um cenário com imagem de terra de chão batido, céu e sol."""
        """O mapa pode pode ser o definido no argumento ou atributo da instância do Kwarwp."""
        mapa = mapa if mapa != "" else self.mapa

        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].imagem)
        ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena)
                
        
        #lado = self.lado
        #cena = self.v.c(self.GLIFOS["_"])
        #indio = self.v.a(self.INDIO, w=100, h=100, x=300, y=400, cena=cena)
        #oca = self.v.a(self.OCA, w=200, h=200, x=400, y=50, cena=cena)
        #tora = self.v.a(self.TORA, w=150, h=150, x=40, y=470, cena=cena)
        #piche = self.v.a(self.PICHE, w=200, h=200, x=50, y=100, cena=cena)
        #ceu = self.v.a(self.GLIFOS["~"], w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        #sol = self.v.a(self.GLIFOS["*"], w=60, h=60, x=0, y=40, cena=cena)
        #[self.cria_elemento(imagem, x=i*lado, y=j*lado+lado, cena=cena)
           #for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)]

        self.taba = {(i, j): fabrica[imagem].objeto(
            fabrica[imagem].imagem, x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
        
        cena.vai()
        return cena
        
    def coisa(self,imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
    
    def indio(self, imagem, x, y, cena):
        lado = self.lado
        return Indio(imagem, x=x, y=y, cena=cena) 
        
    def vazio(self, imagem, x, y, cena):
        lado = self.lado
        return self.v.a(imagem, x=x, y=y, cena=cena)        

if __name__ == "__main__":
    from _spy.vitollino.main import Jogo
    STYLE["width"]=600
    STYLE["height"]=500
    Kwarwp(Jogo)      
