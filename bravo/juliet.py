# patricia.bravo.juliet.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Elemento (mude esta linha).

.. codeauthor:: Gabrielle Alves <mail@local.tipo>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.
        ''' NESSA PARTE O JOGADOR TERÁ QUE ESCOLHER DUAS OPÇÕES DE COMO SE DECLARA UM ELEMENTO
    SE O JOGADOR ESCOLHER A OPÇÃO DO CÓDIGO CERTO, ELE IRÁ CONSEGUIR CRIAR UM ELEMENTO
       ''' SOBRE A OPÇÃO ERRADA:
        - SE O JOGADOR ESCOLHER A OPÇÃO QUE TEM O CÓDIGO ERRADO, ELE IRÁ PARA UMA OUTRA CENA EXPLICANOD O ERRO
        - NESSES CÓDIGOS HÁ:
              A DECLARAÇÃO DO CÓDIGO ERRADO
              A CENA QUE IRÁ CORRIGIR O CÓDIGO
              E UM EMOJI DE NEGATIVO
               '''elemento que está na cena 3 que foi direcionado pela op2, mas irá direcionar p cena2

"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vitollino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "550px"

class oi:
    def __init__(self):
    #primeira cena (onde está localizado as duas opções
        self.cena = cena =Cena( img = "https://i.imgur.com/S5tAUe8.png")
    #opção 2 certo
        op2 = Elemento ( img = "https://i.imgur.com/dVn8Gfo.png" , x = 700, y=350, w = 450, h = 150 , tit= "Clique")
    #cena que direciona a opção 2
        cena2 = Cena ( img = "https://i.imgur.com/IYekltO.png")
    #emoji de ok
        ok= Elemento (img = "https://i.imgur.com/jR7lluz.png")
        ok.entra(cena2)
        ok.vai=cena.vai
    

    
    #opção 1 errado
        op1 = Elemento ( img = "https://i.imgur.com/lN2umME.png", x = 150, y=350, w = 450, h = 150, tit= "Clique")
        #cena que direciona a opção1
        cena3 = Cena ( img = "https://i.imgur.com/aN24UEx.png")
        errado = Elemento (img = "https://i.imgur.com/elvddXi.png")
        errado.entra(cena3)
        errado.vai= cena.vai


        personagem_mulher_maravilha = Elemento(img = "https://i.imgur.com/fK906ve.png",style=dict(left=40, top=300, width=400, height="200px"))   
        personagem_mulher_maravilha.entra(cena2)
        ok= Elemento (img = "https://i.imgur.com/jR7lluz.png")

    
    
    
        op2.entra(cena)
        op1.entra(cena)
    
    
    #certo.entra(cena3)
    #certo.vai=cena2.vai
        op2.vai=cena2.vai
        op1.vai=cena3.vai
    
    def vai(self, *_): 
        self.cena.vai()

    
if __name__ == "__main__":
    oi().vai()