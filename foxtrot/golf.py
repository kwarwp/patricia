# patricia.foxtrot.golf.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto SuperPython World,

.. codeauthor:: Raquel Fernandes <raquelmachado4993@gmail.com>

Changelog
---------
.. versionadded::    20.07
        Página inicial do Jogo.

"""
#importação
from _spy.vitollino.main import Cena,Elemento,Texto, STYLE
#formatacao
STYLE["width"] = 1010
STYLE["heigth"] = "500px"
#figuras
capa_do_jogo = "https://i.imgur.com/0RVnppj.png"
botao_jogar = "https://i.imgur.com/F3Q0bDv.png"
botao_sobre = "https://i.imgur.com/pG9wDIz.png"
#criando classe jogo
class Jogo:
    def __init__(self):
    #criando cena
    
        self.capa =Cena(img= capa_do_jogo)
        
        #inserindo elementos na cena
        self.botao_jogar = Elemento (img= botao_jogar, tit = "jogar",
        style= dict((left=180, top=50,  Width=3, height=20))
        
        self.botao_sobre = Elemento (img=botao_sobre, 
        tit="sobre", 
        style=dict((left=180, top=50,  Width=3, height=20))
        
        #exibindo cena
        self.capa.vai()
        
        #exibindo elementos na cena
        self.botao_sobre.entra(self.capa)
        self.botao_jogar.entra(self.capa)
        
if __name__ == "__main__":
    Jogo()

