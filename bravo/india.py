# patricia.bravo.india.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""
#from _spy.vitollino.main  import Cena,Elemento,Texto
fundo_1 = "https://i.pinimg.com/originals/ca/a8/25/caa8256ded30c7703fadf79651d7833b.jpg" 
balao = "https://4.bp.blogspot.com/-WKsFkjFqfdM/WMATuFHzIqI/AAAAAAAAl1I/Ib-2sPFDfJU0ImaSV8g0fOSBh4_sKAGNwCLcB/s1600/Daniel%2BStudios%2BPack%2BRender%2B%252810%2529.png"
fundo = "https://www.10wallpaper.com/wallpaper/1366x768/1504/black_and_blue-High_Quality_HD_Wallpaper_1366x768.jpg"
# ada.sara.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from browser import html, alert, timer
from random import choice, shuffle
STYLE["width"] , STYLE["height"] = 1200, "600px"
def teste():
	cena = Cena(img = fundo_1)
	elmt = Elemento(img = balao, style=dict(left=405, top=400, width=20, height="80px"))
	cena.vai()
teste()    
