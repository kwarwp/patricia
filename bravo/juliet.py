# patricia.bravo.juliet.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Elemento (mude esta linha).

.. codeauthor:: Gabrielle Alves <mail@local.tipo>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vitollino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "550px"

class oi:
    #primeira cena (onde está localizado as duas opções
    cena = Cena( img = "https://i.imgur.com/S5tAUe8.png")
    #opção 1 
    op1 = Elemento ( img = "https://i.imgur.com/5YTF1VP.png" , x = 700, y=390, tit= "Clique")
    #cena que direciona a opção 1
    cena2 = Cena ( img = "https://i.imgur.com/IYekltO.png")
    #opção 2
    op2 = Elemento ( img = "https://images.vexels.com/media/users/3/139740/isolated/preview/bfecbaa063a84b2e9bbd9f8b9b41d410-bot--o-de-reprodu----o-redondo-azul-by-vexels.png", x = 350, y=390, tit= "Clique")
    #cena que direciona a opção2
    cena3 = Cena ( img = "https://i.imgur.com/nsi5Cwh.jpg")
    ##elemento que está na cena 3 que foi direcionado pela op2, mas irá direcionar p cena2
    #certo = Elemento ( img = "https://images.vexels.com/media/users/3/139740/isolated/preview/bfecbaa063a84b2e9bbd9f8b9b41d410-bot--o-de-reprodu----o-redondo-azul-by-vexels.png")
    #cena do personagem
    personagem_mulher_maravilha = Elemento(img = "https://i.imgur.com/fK906ve.png",style=dict(left=40, top=300, width=400, height="200px"))   
    personagem_mulher_maravilha.entra(cena2)
    ok= Elemento (img = "https://i.imgur.com/jR7lluz.png")

    
    
    
    op1.entra(cena)
    op2.entra(cena)
    ok.entra(cena2)
    #certo.entra(cena3)
    #certo.vai=cena2.vai
    op1.vai=cena2.vai
    op2.vai=cena3.vai
    
    cena.vai()
oi()