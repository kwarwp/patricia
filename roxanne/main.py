MAPA_INICIO = """
@....&
......
......
.#.^..
"""

class Kwarwp():
    GLIFOS = {
    "&": "https://i.imgur.com/dZQ8liT.jpg",  # OCA
    "^": "https://imgur.com/8jMuupz.png",  # INDIO
    ".": "https://i.imgur.com/npb9Oej.png",  # VAZIO
    "_": "https://i.imgur.com/sGoKfvs.jpg",  # SOLO
    "#": "https://imgur.com/ldI7IbK.png",  # TORA
    "@": "https://imgur.com/tLLVjfN.png",  # PICHE
    "~": "https://i.imgur.com/UAETaiP.gif",  # CEU
    "*": "https://i.imgur.com/PfodQmT.gif"  # SOL
    }
    
    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
        self.v = vitollino()
        mapa = mapa.split()
        self.lado, self.col = 100, len(mapa[0]) 
        self.cena = self.cria(mapa=mapa) if vitollino else None
        
    def cria(self, mapa="  "):
        lado = self.lado
        cena = self.v.c(self.GLIFOS["_"])
        ceu = self.v.a(self.GLIFOS["~"], w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(self.GLIFOS["*"], w=60, h=60, x=0, y=40, cena=cena)
        [self.cria_elemento( x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)]
        cena.vai()
        return cena
        
    def cria_elemento(self, x, y, cena):
        lado = self.lado
        return self.v.a(self.GLIFOS[imagem], w=lado, h=lado, x=i*lado, y=j*lado+lado, cena=cena)

def main(vitollino):
    Kwarwp(vitollino)
        
    
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE.update(width=600, height="500px")
    main(Jogo)
        