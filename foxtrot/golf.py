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
botao_jogar = "https://i.imgur.com/pG9wDIz.png"
botao_sobre = "https://i.imgur.com/F3Q0bDv.png"
sobre = "https://i.imgur.com/lear9Bn.png"

#criando classe jogo
class Jogo:
    def __init__(self):
    #criando cena
    
        self.capa =Cena(img= capa_do_jogo)
        
        #inserindo elementos na cena
        self.botao_jogar = Elemento (img=botao_jogar,
        tit="Jogar",
        style= dict(left=500, top=400))
        
        self.botao_sobre = Elemento (img=botao_sobre, 
        tit="Sobre", 
        style= dict(left=400, top=400))
        
        #exibindo cena
        self.capa.vai()
        
        #exibindo elementos na cena
        self.botao_sobre.entra(self.capa)
        self.botao_jogar.entra(self.capa)
        
        #textos
        self.texto_jogar = Texto (self.capa, "Olá! Volte em breve para Jogar!")

        #cenasobre
        self.cena_sobre = Cena (img=sobre)
        self.cena_sobre.esquerda=capa.vai
        
        #ação caso seja clicado
        self.botao_jogar.vai=self.texto_jogar.vai
        self.botao_sobre.vai=self.cena_sobre.vai
     
     
       #voltar 
        
        
if __name__ == "__main__":
    Jogo()

