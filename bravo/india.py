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
balao = "https://i.pinimg.com/236x/d2/dd/c4/d2ddc45b2599d5fc60f03ec81c53bb6c.jpg"
balao2 = "https://i.pinimg.com/236x/14/3a/14/143a14c4535873de51301549ba96e051.jpg"
fundo = "https://i.pinimg.com/originals/ca/a8/25/caa8256ded30c7703fadf79651d7833b.jpg"

STYLE["width"] , STYLE["height"] = 1200, "600px"

def teste():
    cena = Cena(img = fundo)
    cenas = Elemento(img = balao, style=dict(left=200, top=250, width=200, height="200px"))
    elementos = Elemento(img = balao2, style=dict(left=800, top=250, width=200, height="200px"))
    txt1 = Texto(cena,"Vamos aprender a programar?")
    txt2 = Texto(cena,"Escolha entre cenas ou elementos para começar.")
    #txt1.vai=txt2.vai
    cena.vai()
    cenas.entra(cena)
    elementos.entra(cena)
    txt1.vai()
    if txt1.vai == true:
        txt2.vai()
    #cenas.vai()
    #elementos.vai()
teste()    
    
