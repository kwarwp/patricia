# patricia.indio.kwarwp.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" 
Montagem orientada do Kwarwp do zero!

.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

Changelog
---------
.. versionadded::    20.07

"""

class Kwarwp():
    """ Jogo para ensino de programação.

        :param vitollino: Empacota o engenho de jogo Vitollino.
    """
    
    OCA = "https://i.imgur.com/dZQ8liT.jpg"
    INDIO = "https://imgur.com/8jMuupz.png"
    SOLO = "https://i.imgur.com/sGoKfvs.jpg"
    TORA = "https://imgur.com/ldI7IbK.png"
    PICHE = "https://imgur.com/tLLVjfN.png"
    CEU = "https://i.imgur.com/UAETaiP.gif"
    SOL = "https://i.imgur.com/PfodQmT.gif"
    CERCA = "https://i.imgur.com/uwYPNlz.png"
    
    def __init__(self, vitollino=None, cenario_padrao="default"):
        """
        Contrutor da classe que permite a declaração dos parâmetros iniciais.
        self.v = vitollino()
        """
        self.v = vitollino()
        self.cena = self.cria(cenario=cenario_padrao) if vitollino else None

    def cria(self, cenario="default"):
        """
        Cria o ambiente de programação Kwarwp.
        
        
            >> cena = self.v.c(self."url")
        
        - Gera a cena do jogo chamano *self.vitolino.c* referente ao módulo Jogo e *(self."url")* referente a imagem do canvas.
        
            >> elemento = self.v.a(self.elemento, w=100, h=100, x=300, y=400, cena=cena)
        """
        cena = self.v.c(self.SOLO)
        indio = self.v.a(self.INDIO, w=100, h=100, x=300, y=400, cena=cena)
        oca = self.v.a(self.OCA, w=100, h=100, x=500, y=100, cena=cena)
        tora = self.v.a(self.TORA, w=100, h=100, x=100, y=400, cena=cena)
        piche = self.v.a(self.PICHE, w=100, h=100, x=100, y=100, cena=cena)
        piche = self.v.a(self.CEU, w=600, h=100, x=0, y=0, cena=cena)
        sol = self.v.a(self.SOL, w=60, h=60, x=0, y=40, cena=cena)
        cerca = self.v.a(self.CERCA, w=60, h=60, x=0, y=500, cena=cena)
        cena.vai()
        return cena
        
if __name__ == "__main__":
    """
    class Jogo:
        def __init__(self):
            self.c = Cena
            self.d = self.codigo = Codigo
            self.q = Sala
            self.salao = self.s = Salao
            self.a = Elemento
            self.texto = self.t = Popup
            self.n = Texto
            self.labirinto = self.l = Labirinto
            self.inventario = self.i = INVENTARIO
            self.portal = self.p = Portal
            self.dropper = self.d = Dropper
            self.droppable = self.r = Droppable
            self.musica = self.m = Musica
            self.codigo = Codigo
            self.document = document
            self.html = html
            self.window = win
            self.timer = timer
            pass
        
    STYLE["width"] = 600 -> Altera o canvas do jogo largura da tela. Recebe int.
    STYLE["height"] = "500px" -> Altera o canvas do jogo altura da tela. Recebe str.
        
    Kwarwp(Jogo) -> Chama a Classe Kwarwp com o método Jogo da biblioteca Vitollino
    """
    from _spy.vitollino.main import Jogo, STYLE

    STYLE["width"] = 600
    STYLE["height"] = "500px"
    Kwarwp(Jogo)