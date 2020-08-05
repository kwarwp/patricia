# patricia.kathryn.kwarwp2.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" 
Montagem orientada do Kwarwp do zero! Parte 4

.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

Changelog
---------
.. versionadded::    20.07

"""
from collections import namedtuple as nt

IMGUR = "https://imgur.com/"

MAPA_INICIO = """
+++++++++
+...+..@+
+.......+
+...@###+
+^..+.&.+
+++++++++
"""
class Kwarwp():
    """ Jogo para ensino de programação.
        
        Declara o dicionário GLIFOS que possui a str símbolo do elemento e o correspodente link de imagem
        
        Declara a string MAPA_INICIO que possui a posição dos elementos (GLIFOS) no mapa através da matriz linha x coluna. 
        As linha separadas pela tecla <Enter>, a coluna determinada pelos caracteres colineares em linha singulares.

        :param vitollino: Empacota o engenho de jogo Vitollino.
        :param mapa: Um texto representando o mapa do desafio.
        :param medidas: Um dicionário usado para redimensionar a tela.
    """
    
    VITOLLINO = None
    """Referência estática para obter o engenho de jogo."""
    LADO = None
    """Referência estática para definir o lado do piso da casa."""

    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
        """
        Contrutor da classe que permite a declaração dos parâmetros iniciais.
        
            >> Kwarwp.VITOLLINO = self.v = vitollino()
       
        Cria um matriz com os elementos descritos em cada linha de texto.
        
            >> self.lado, self.col 
        
        Determina a largura da arena dos desafios, número de colunas no mapa.
        
            >>len(self.mapa[0]), len(self.mapa)+1 
            
        Retorna o número de colunas e linhas que existem no mapa.
                       
        STYLE["width"] = 700 -> Altera o canvas do jogo em largura da tela. Recebe int.
        STYLE["height"] = "600px" -> Altera o canvas do jogo em altura da tela. Recebe str.
        """
        
        Kwarwp.VITOLLINO = self.v = vitollino()
        """Cria um matriz com os elementos descritos em cada linha de texto"""
        self.mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas e linhas no mapa"""
        self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        Kwarwp.LADO = self.lado
        w, h = self.col*self.lado, self.lin*self.lado
        self.taba = {}
        """Dicionário que a partir de coordenada (i,J) localiza um piso da taba"""
        medidas.update(width=w, height=f"{h}px")
        self.cena = self.cria(mapa=self.mapa) if vitollino else None
                       
        STYLE["width"] = w
        STYLE["height"] = "{}px".format(h)
            
    def cria(self, mapa = ""):
        """
        *Este método define uma fábrica de componentes.*

        :param mapa: Um texto representando o mapa do desafio.
        
        :nome Fab: O nome da tupla que descreve a fábrica.
        :campo objeto: O tipo de objeto que vai ser criado.
        :campo imagem: A imagem que representa o objeto que vai ser criado.
                
            >> cena = self.v.c(self."url")
        
        Gera a cena do jogo chamano **self.v.c** referente ao módulo Jogo do Vitollino e **(self."url")** referente a imagem do canvas.
        
            >> elemento = self.v.a(self.elemento, w=int, h=int, x=int, y=int, cena="url")
            
        Gera um elemento do jogo chamano **self.v.a** chamado pelo módulo do Jogo do Vitollino criando a classe Elemento com os seguintes parâmetros:
        
            >> (self."url", w=largura_img, h=altura_img, x=canvas_x, y=canvas_y, cena="url")
            .
            >> solo.vai()
        
        Retorna a cena para o canvas com o método .vai() do vitollino.
        
            >> for j, linha in enumerate(mapa):
            
        Enumera e declara cada **linha** da lista matriz recortada.
        
            >>     for i, imagem in enumerate(linha):
            
        Enumera e declara cada **caractere** da lista matriz recortada. 
        Sendo i, j respecticamente linha, coluna de cada GLIFO contido na MATRIZ_INICIO.
        
        O valor de retorno da combinação de for retorna a invocação do cria_elemento com os parâmetros esncotrados através da ultima contagem
        
            >> x=i*lado
        
        É a posição do x (largura) do canvas do jogo gerado através do produto índice da linha e o valor arbitrário lado referente ao temanho do elemento
        
            >> y=j*lado+lado
            
        É a posição do y (altura) do canvas do jogo gerado através do produto índice lista coluna mais altura do elemento.
        
        """
        Fab = nt("Fab", "objeto url_imagem")
        fabrica = {
            "&": Fab(self.coisa, f"{IMGUR}dZQ8liT.jpg"), # OCA
            "^": Fab(self.indio, f"{IMGUR}8jMuupz.png"), # INDIO
            ".": Fab(self.vazio, f"{IMGUR}npb9Oej.png"), # VAZIO
            "_": Fab(self.coisa, f"{IMGUR}sGoKfvs.jpg"), # SOLO
            "#": Fab(self.coisa, f"{IMGUR}ldI7IbK.png"), # TORA  
            "@": Fab(self.coisa, f"{IMGUR}tLLVjfN.png"), # PICHE
            "~": Fab(self.coisa, f"{IMGUR}UAETaiP.gif"), # CEU
            "*": Fab(self.coisa, f"{IMGUR}PfodQmT.gif"), # SOL
            "|": Fab(self.coisa, f"{IMGUR}uwYPNlz.png")  # CERCA
            }
        
        mapa = mapa if mapa != "" else self.mapa

        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].url_imagem)
        ceu = self.v.a(fabrica["~"].url_imagem, w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(fabrica["*"].url_imagem, w=60, h=60, x=0, y=40, cena=cena)
        
        self.taba = {(i, j): fabrica[imagem].objeto(
            fabrica[imagem].url_imagem, x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)
            }
        cena.vai()
        return cena
        '''
        Tentar criar mesmo código com a descrição de dependência a baixo
        for j, linha in enumerate(mapa):
            for i, imagem in enumerate(linha):
                self.cria_elemento( x=i*lado, y=j*lado+lado, cena=cena)
                
        def cria_elemento(self, x, y, cena):
        """
        Função que retorna o **script do elemento** na posição determinada pela matriz(mapa).        
        x, y equivalem as posições x, y no canvas do jogo.        
        cena equivale a "url" atual do jogo."""
            lado = self.lado
            return self.v.a(self.GLIFOS[imagem], w=lado, h=lado, x=i*lado, y=j*lado+lado, cena=cena)
        '''
    def coisa(self, imagem, x, y, cena):
        """
        Este método define uma fábrica para coisas que estão no cenário.
        Cria um elemento na arena do Kwarwp na posição definida.
        
        :param imagem: imagem que representa o elemento que será posicionado.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        """
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        
    def indio(self, imagem, x, y, cena):
        """
        Este método define uma fábrica criando o índio o personagem principal.

        :param imagem: imagem que representa o elemento que será posicionado.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        """
        lado = self.lado
        return Indio(imagem, x=x, y=y, cena=cena)

class Indio():
    '''
    Cria o personagem principal na arena do Kwarwp na posição definida.

    :param imagem: A figura representando o índio na posição indicada.
    :param x: Coluna em que o elemento será posicionado.
    :param y: Linha em que o elemento será posicionado.
    :param cena: Cena em que o elemento será posicionado.
    '''
    def __init__(self, imagem, x, y, cena):
        self.lado = lado = Kwarwp.LADO
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        
if __name__ == "__main__":
    """
    class Jogo:
        def __init__(self):
            self.c = Cena
            self.a = Elemento
      
    Kwarwp(Jogo) -> Chama a Classe Kwarwp com o método Jogo da biblioteca Vitollino
    """
    from _spy.vitollino.main import Jogo, STYLE
    Kwarwp(Jogo)