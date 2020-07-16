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
"""figuras"""
capa_do_jogo = "https://i.imgur.com/0RVnppj.png"
botao_jogar = "https://i.imgur.com/pG9wDIz.png"
botao_sobre = "https://i.imgur.com/F3Q0bDv.png"
sobre = "https://i.imgur.com/ZN0slvj.png"
escolhajogador = "https://i.imgur.com/IsUXeNV.png"
avatar1 = "https://i.imgur.com/fSrc1Ab.png"
avatar2 ="https://i.imgur.com/JQKcmov.png"
portadocastelo="https://i.imgur.com/zyfCCo0.png"
author = "https://i.imgur.com/ZWKxnAx.png"
FOCO = "https://i.imgur.com/6e096Va.png"

"""criando classe jogo"""
class Jogo:
    def __init__(self):
        """criando cena"""
    
        self.capa =Cena(img= capa_do_jogo)
        
        """inserindo elementos na cena"""
        self.botao_jogar = Elemento (img=botao_jogar,
        tit="Jogar",
        style= dict(left=500, top=400))
        
        self.botao_sobre = Elemento (img=botao_sobre, 
        tit="Sobre", 
        style= dict(left=400, top=400))
        
        """exibindo cena"""
        self.capa.vai()
        
        """Cena sobre"""
        self.cena_sobre = Cena (img=sobre)
        
        """Cena sobre"""
        self.escolha_jogador = Cena (img=escolhajogador)
        
        self.avatar1 = Elemento (img=avatar1, 
        tit="Personagem 1", 
        style= dict(left=400, top=400))
        
        self.avatar2 = Elemento (img=avatar2, 
        tit="Personagem 2", 
        style= dict(left=500, top=400))
        
        """exibindo elementos na cena sobre"""
        self.botao_sobre.entra(self.capa)
        self.botao_jogar.entra(self.capa)   
             
        
        
        """Cena do Castelo"""
        self.castelo = Cena (img=portadocastelo)
        """texto castelo"""
        self.texto_castelo = Texto (self.castelo, "Parado aí! Identifique-se!")
        self.porta = Elemento(FOCO, x=600, y=180, w=300, h=300, cena=self.castelo, style={"opacity": 0.0}, vai=self.texto_castelo.vai)
                   
        """textos"""
        self.texto_jogar = Texto (self.capa, "Volte em breve para jogar. Enquanto isso, aproveite uma demonstração.")
        
        
        
        """ação caso seja clicado"""
        self.botao_sobre.vai=self.cena_sobre.vai
        self.botao_jogar.vai=self.texto_jogar.vai
        self.cena_sobre.esquerda = self.capa.vai()
        self.texto_jogar.foi = self.escolha_jogador.vai
        self.avatar1.entra(self.escolha_jogador)
        self.avatar2.entra(self.escolha_jogador)
        
        """Cena de identificacao"""
        self.cenaauthor = Cena (img=author)
        
        """ação após escolha do Avatar"""
        self.avatar1.vai = self.castelo.vai
        self.avatar2.vai = self.castelo.vai
        self.castelo.vai = self.texto_castelo.vai
        self.texto_castelo.foi = self.cenaauthor.vai

        
if __name__ == "__main__":
    Jogo()

