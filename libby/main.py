# SPDX-License-Identifier: GPL-3.0-or-later
# patricia.libby.parte_1.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Aula Kwarwp Charles.

.. codeauthor:: Charles Pimentel <pimentelufrj@gmail.com>

Changelog
---------
.. versionadded::    05.08
        main.

"""

MAPA_INICIO = """
@....&
......
......
.#.^..
"""
MAPA_CERCA = """
%%%%%%%
%..%..&
%..#..%
%^.%..%
%%%%%%%
"""
class Indio():

   def __init__(self, imagem, x, y, cena):
      self.lado = lado = Kwarwp.LADO
      self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
      
      
class Kwarwp():
   VITOLLINO = None
   """Referência estática para obter o engenho de jogo."""
   LADO = None
   """Referência estática para definir o lado do piso da casa."""

   def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
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
        
    
    def cria(self, mapa="  "):
        """ Cria o ambiente de programação Kwarwp.
            :param mapa: Um texto representando o mapa do desafio.
        """
        """Cria um cenário com imagem de terra de chão batido, céu e sol"""
        lado = self.lado
        cena = self.v.c(self.GLIFOS["_"])
        ceu = self.v.a(self.GLIFOS["~"], w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(self.GLIFOS["*"], w=60, h=60, x=0, y=40, cena=cena)
        """Posiciona os elementos segundo suas posições i, j na matriz mapa"""
        [self.cria_elemento( x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)]
        cena.vai()
        return cena
        
    def cria_elemento(self, x, y, cena):
        """ Cria um elemento na arena do Kwarwp na posição definida.
            :param x: coluna em que o elemento será posicionado.
            :param y: linha em que o elemento será posicionado.
            :param cena: cena em que o elemento será posicionado.
        """
        lado = self.lado
        return self.v.a(self.GLIFOS[imagem], w=lado, h=lado, x=i*lado, y=j*lado+lado, cena=cena)

def main(vitollino):
    Kwarwp(vitollino)
    
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE.update(width=600, height="500px")
    main(Jogo)
