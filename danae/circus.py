# patricia.danae.circus.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    20.09
        Descreva o que você adicionou no código.

"""
class Piso:
    ALDEIA = "https://i.imgur.com/Gqoucvd.png"
    #ALDEIA = "https://i.imgur.com/UCWGCKR.png"
    def __init__(self, x, y, pos, siz, cena):
        tile = 100
        self.elt = Aldeia.J.a(self.ALDEIA, x=x*150, y=y*150, w=tile, h=tile, cena=cena)
        self.elt.pos = pos
        self.elt.siz = siz
    def possize(self, pos, siz=None):
        self.elt.pos = pos
        self.elt.siz = siz if siz else self.elt.siz
        
class Aldeia:
    ALDEIA = "https://i.imgur.com/Gqoucvd.png"
    J = None
    #ALDEIA = "https://i.imgur.com/UCWGCKR.png"
    def __init__(self, j):
        Aldeia.J = j
        def elt(x, y):
            tile = 100
            ald=j.a(self.ALDEIA, x=x*150, y=y*150, w=tile, h=tile)  # , style=dict(transform="rotate(90deg)"))
            ald.siz = (tile*4, tile*3)
            ald.pos = (-x*tile, -y*tile)
            ald.entra(cena)
            return ald
        def spr(ald, x, y):
            tile = 100
            ald.siz = (tile*4, tile*3)
            ald.pos = (-x*tile, -y*tile)
            #ald.entra(cena)
            return ald
            e.elt.html = f"siz {e.siz} pos {e.pos}"
            e.o = 0.5
        tile = 100
        cena = j.c("https://i.imgur.com/sGoKfvs.jpg")
        a = [Piso(x, y, (-x*tile, -y*tile), (tile*4, tile*3), cena=cena)
             for x in range(4) for y in range(3)]
        # b = [spr(a[x*3+y], x, y) for x in range(4) for y in range(3)]
        
        # b = [spr(a[x*4+y],x,y) for x in range(4) for y in range(3)]
        #a[0].siz = (400, 300)
        #a[0].entra(cena)
        cena.vai()
        
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE.update(width=900, height="600px")
    Aldeia(Jogo())
        