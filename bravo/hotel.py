# patricia.bravo.hotel.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Rosilane Lessa <rosilanefonte@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

 CENA

"""
'''from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE["width"] = 1250
STYLE["height"]= "550px"

class cena:
    expli= Cena(img = "https://i.imgur.com/oHAC3Xi.png")
    fundo= Cena (img = "https://i.imgur.com/hexAWk7.png")
    erro= Cena (img = "https://i.imgur.com/idqEr5C.png")
    casa= Cena (img = "https://plantasdecasas.com/storage/2017/07/planta-fachada-casa-115-fr-AG.jpg")
    triste = Elemento (img= "https://i.imgur.com/0R5Xo83.png", tit="CLICK", x=1000, y=100)
    feliz = Elemento (img= "https://i.imgur.com/UaihdhW.png", tit="CLICK", x=40, y=80)
    codigo1 = Elemento (img="https://i.imgur.com/QGEgNAt.png", tit="CLICK", style=dict(left=40, top=350, width=500, height="200px"))
    codigo2 = Elemento (img="https://i.imgur.com/ccJqbMb.png", tit="CLICK", style=dict(left=620, top=350, width=500, height="200px"))
    pergunta = Elemento (img= "https://i.imgur.com/fYmNuBj.png", style=dict(left=450, top=180, width=250, height="150px"))
    siga = Elemento (img="https://i.imgur.com/kRmXNkz.png", style=dict(left=540, top=480, width=150, height="150px"))
    codigo1.entra(fundo)
    codigo2.entra(fundo)
    triste.entra(erro)
    feliz.entra(casa)
    pergunta.entra(fundo)
    siga.entra(expli)
    codigo1.vai=erro.vai
    codigo2.vai=casa.vai
    triste.vai=fundo.vai
    feliz.vai=fundo.vai
    siga.vai=fundo.vai
    #fundo.vai()
    expli.vai()

cena()'''

# patricia.bravo.hotel.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Rosilane Lessa <rosilanefonte@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

 CENA

"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vitollino.main import INVENTARIO as inv

STYLE["width"] = 1250
STYLE["height"]= "550px"

class cena:
    def __init__(self):
        self.expli= expli= Cena(img = "https://i.imgur.com/oHAC3Xi.png")
        fundo= Cena (img = "https://i.imgur.com/hexAWk7.png")
        erro= Cena (img = "https://i.imgur.com/idqEr5C.png")
        casa= Cena (img = "https://plantasdecasas.com/storage/2017/07/planta-fachada-casa-115-fr-AG.jpg")
        triste = Elemento (img= "https://i.imgur.com/0R5Xo83.png", tit="CLICK", x=1000, y=100)
        feliz = Elemento (img= "https://i.imgur.com/UaihdhW.png", tit="CLICK", x=40, y=80)
        codigo1 = Elemento (img="https://i.imgur.com/QGEgNAt.png", tit="CLICK", style=dict(left=40, top=350, width=500, height="200px"))
        codigo2 = Elemento (img="https://i.imgur.com/ccJqbMb.png", tit="CLICK", style=dict(left=620, top=350, width=500, height="200px"))
        pergunta = Elemento (img= "https://i.imgur.com/fYmNuBj.png", style=dict(left=450, top=180, width=250, height="150px"))
        siga = Elemento (img="https://i.imgur.com/kRmXNkz.png", style=dict(left=540, top=480, width=150, height="150px"))
        codigo1.entra(fundo)
        codigo2.entra(fundo)
        triste.entra(erro)
        feliz.entra(casa)
        pergunta.entra(fundo)
        siga.entra(expli)
        codigo1.vai=erro.vai
        codigo2.vai=casa.vai
        triste.vai=fundo.vai
        feliz.vai=fundo.vai
        siga.vai=fundo.vai
    #fundo.vai()
        #expli.vai()
    def vai(self, *_):
        """Tem que ter este método vai para ser usado como cena direita ou esquerda"""
        self.expli.vai()


if __name__ == "__main__":
    """ A chamada de teste tem que estar dentro deste if"""
    cena().vai()




