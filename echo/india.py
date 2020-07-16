# patricia.echo.india.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Victória Regina Caruzo <victoriareginalattes@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""

from _spy.vitollino.main import Cena, INVENTARIO, STYLE
from random import choice

STYLE["width"] = 840
STYLE["height"] = 550

TABULEIRO = "http://www.infcross.com.br/mestrado/tabuleiro.jpg"
BOTAO = "https://imgur.com/oC9lAgW"
DADO_1 = "http://infcross.com.br/mestrado/dado%1.png"

tabuleiro = Cena(TABULEIRO)
tabuleiro.vai()
dado_1 = Cena(DADO_1)
dado_1.vai()



"""def cena_principal():
    inicio = Cena(img=tabuleiro)
    inicio_e = Elemento (img = botao, tit="Gravidade", style = dict(left= 70,top=170, width=1150, height=550,bottom=100))
    lado1 = Cena(img=tabuleiro, direita =inicio)

    
    inicio_e.entra(inicio)

    inicio.vai()
    
cena_principal()"""