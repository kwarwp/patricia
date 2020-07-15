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

fundo = "https://www.10wallpaper.com/wallpaper/1366x768/1504/black_and_blue-High_Quality_HD_Wallpaper_1366x768.jpg"
# ada.sara.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from browser import html, alert, timer
from random import choice, shuffle
STYLE["width"] , STYLE["height"] = 1200, "600px"

class Kamui:
    def __init__(self):
        self.pulo = -10
        self.issun_top = 380
        _kamui = fundo#"https://i.imgur.com/R3pCA3a.jpg"
        _okami = "https://i.imgur.com/1jSbzEj.png"
        _issun = "https://i.imgur.com/lAYKq3F.png"
        self.kamui = Cena(_kamui)
        self.kamui.vai()
        def pula_issun(_=0, issun_=self.issun.elt.style):
            issun_.top = self.issun_top + self.pulo
            self.pulo = -self.pulo
        self.pula_issun = timer.set_interval(pula_issun, 300)
        def para_issun(_=0):
            Texto(self.kamui, tit="Issun - O artista intinerante", txt="Essa é a história da deusa Amaterasu").vai()
            timer.clear_interval(self.pula_issun)
        self.issun.vai = para_issun

if __name__ == "__main__":
    _ = Kamui()