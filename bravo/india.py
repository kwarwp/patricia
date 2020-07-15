# patricia.bravo.india.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from browser import html, alert, timer
from random import choice, shuffle
#from _spy.vitollino.main  import Cena,Elemento,Texto
balao = "https://4.bp.blogspot.com/-WKsFkjFqfdM/WMATuFHzIqI/AAAAAAAAl1I/Ib-2sPFDfJU0ImaSV8g0fOSBh4_sKAGNwCLcB/s1600/Daniel%2BStudios%2BPack%2BRender%2B%252810%2529.png"
fundo = "https://i.pinimg.com/originals/ca/a8/25/caa8256ded30c7703fadf79651d7833b.jpg"

#STYLE["width"] , STYLE["height"] = 1200, "600px"

def teste():
    cena = Cena(img = fundo)
    elmt = Elemento(img = balao, style=dict(left=135, top=400, width=20, height="20px"))
    #cena.vai()
    elmt.vai()
teste()    
    
