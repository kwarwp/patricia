# patricia.charlie.juliet.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" ensinar orientando ao objeto com quebra cabeça .

.. codeauthor:: Leniah Lima  <leniah@nce.ufrj.br>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""

from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
from _spy.vitollino.main import Inventario as inv

STYLE["width"] = 800
STYLE["height"] = "600px"

HERDO1 = "https://upload.wikimedia.org/wikipedia/commons/e/ea/Rocky_Landscape.jpg"#IMAGENS QUE FICAM NO QUEBRA CABEÇA, TEM QUE SER ONLINE(PNG OU JPG) 
HERDO2 = "https://upload.wikimedia.org/wikipedia/commons/e/ea/Rocky_Landscape.jpg"
HERDO3 = "https://upload.wikimedia.org/wikipedia/commons/e/ea/Rocky_Landscape.jpg"
MONITOR = "https://img2.gratispng.com/20171202/047/monitor-png-file-5a2301f39f9330.4508814915122436996536.jpg"
class minipython:
    """Usa um editor de imagem ( /) e recorta o Herdograma em linhas geracionais.
       No game, o jogador terá que clicar nas linhas em ordem certa para montar o herdograma corretamente.
    """
    def __init__(self, esta_cena, chama_quando_acerta):
        posiciona_proxima = self.posiciona_proxima
        class LinhaGeracional:
            """Representa cada uma das linhas recortadas do herdograma original"""
            def __init__(self, linha, posicao):
                self.posicao = posicao # posição original no topo da página
                self.linha = Elemento(linha, x=posicao*200, y=20, w=200, h=50, cena=esta_cena) #tamanho das imagens
                self.linha.vai = self.clica_e_posiciona_a_linha #quando clica, monta o herdograma
            def zera(self):
                self.linha.x = self.posicao*200  # posiciona cada peça com 200 pixels de distância
                self.linha.y = 20  # posiciona a peça no topo da página
                self.linha.vai = self.clica_e_posiciona_a_linha
            def clica_e_posiciona_a_linha(self, *_):
                x, y = posiciona_proxima(self.posicao)
                if y:  # se o y retornou zero é porque o posiciona próxima detectou montagem errada
                    self.linha.x, self.linha.y = x, y # monta a linha no herdograma
                    self.linha.vai = lambda *_:None #desativa o click da linha

        # coloca cada uma das linhas embaralhadas 
        self.linhas = [
            LinhaGeracional(linha=uma_linha, posicao=uma_posicao)
            for uma_posicao, uma_linha in enumerate([HERDO1, HERDO3, HERDO2])]# aqui fica as imagens
        self.acertou = chama_quando_acerta
        self.linha_inicial = 300
        self.altura_da_linha = 50  # cada peça do herdograma tem esta altura
        self.posicoes_montadas = []  #l ista das linhas já montadas 
        self.posicoes_corretas = [1, 2, 3]  # lista das linhas montadas corretamente

    def posiciona_proxima(self, posicao):
        """Chamdo pelo clique (vai) de cada peça. Atualiza a próxima posição da peça.
           Calcula se montou correto, comparando com a lista de posicões corretas.
           Se já montou quatro peças, e não acerto sinaliza com zero, para iniciar o jogo.
        """
        self.linha_inicial += self.altura_da_linha  # incrementa a posição para montar na linha de baixo
        self.posicoes_montadas += [posicao]  # adiciona o índice desta peça na lista de peças montadas
        if self.posicoes_montadas == self.posicoes_corretas:
            self.acertou()  # invoca a ação acertou se montou nas posições corretas
            return 300, self.linha_inicial
        else:
            if len(self.posicoes_montadas) == 4:  # se montou qutro peças incorretas reinicia o game
                [linha.zera() for linha in self.linhas]  # volta as peças para o topo
                self.posicoes_montadas = []  # indica que nenhuma peça foi montada
                self.linha_inicial = 300  # inicia a altura de ontagem da primeira peça
                return 0, 0  #  retorna uma posição inválida para sinalizar a peça
        return 300, self.linha_inicial
class normal():
        def __init__(self):
            self.monitor = Cena( img = MONITOR)
            self.monitor = monitor = Cena(img = MONITOR)
            minipython(self.monitor, self.mostra_conteudo_minipython)
            
        def mostra_conteudo_minipython(self, *_):        
                Texto(self.monitor, "Parábens, vc aprendeu como se faça o uso de orientação ao objeto em pyhton ").vai() # mensagem depois de montar o quebra cabeça
            
        def vai(self, *_):        
                self.monitor.vai()
normal().vai()