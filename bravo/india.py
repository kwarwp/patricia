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
frase1 = "https://i.pinimg.com/236x/4c/f8/6c/4cf86c786beb1c6457f31bf4fcd7ec99.jpg"
frase2 = "https://i.pinimg.com/236x/7a/d6/c2/7ad6c2fdfd198c6903dee4425825ed9a.jpg"
pr = "https://romanticopornatureza.files.wordpress.com/2012/03/proximo.gif"
STYLE["width"] , STYLE["height"] = 1200, "600px"

def teste():
    x = 0
    cena = Cena(img = fundo)
    cenas = Elemento(img = balao, style=dict(left=200, top=250, width=200, height="200px"))
    cena2 = Cena(img = pr)
    elementos = Elemento(img = balao2, style=dict(left=800, top=250, width=200, height="200px"))
    txt1 = Elemento(img = frase1, style=dict(left=500, top=100, width=200, height="200px"))
    txt2 = Elemento(img = frase2, style=dict(left=500, top=100, width=200, height="200px"))
    txt1.entra(cena)
    txt2.entra(cena)
    txt1.vai=cena2.vai
    cena2.vai=txt2.vai
    cena.vai()
    cenas.entra(cena)
    elementos.entra(cena)
    '''if x == 0:
        txt1.vai()
        print("1")
        x = 1
    if x == 1:
        txt2.vai()
        print("2")'''
    #cenas.vai()
    #elementos.vai()
teste()    
    
