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
        """Contrutor da classe que permite a declaração dos parâmetros iniciais."""
        
        Kwarwp.VITOLLINO = self.v = vitollino()
        """Cria um matriz com os elementos descritos em cada linha de texto"""
        self.mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas e linhas no mapa"""
        self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        Kwarwp.LADO = self.lado
        w, h = self.col*self.lado, self.lin*self.lado
        """Dicionário que a partir de coordenada (i,j) localiza um piso da taba"""
        self.taba = {}
        """Atuaiza a largura e o comprimento do mapa do jogo"""
        medidas.update(width=w, height=f"{h}px")
        
        self.cena = self.cria(mapa=self.mapa) if vitollino else None
            
    def cria(self, mapa = ""):
        """
        *Este método define uma fábrica de componentes.*

        :param mapa: Um texto representando o mapa do desafio.
        
        :nome Fab: O nome da tupla que descreve a fábrica.
        :campo objeto: O tipo de objeto que vai ser criado.
        :campo url_imagem: A imagem que representa o objeto que vai ser criado.
        
        Define uma fábrica de tuplas nomeáveis gerada pela biblioteca collections.namedpuple()
        Declara o dicionário para fabricar as tuplas com as características de objeto em função do glifo.
        
        .. note::
           Fab = collections.namedpuple("título", "nome_coluna url_imagem") 
           faz o parenteses ser uma "nomeadora de colunas" das seguintes tuplas.
           Dessa forma a tupla a seguir poderá ser separada por vírgulas a cada variável ou str diferente.
           Exemplo:
               >>Fab(self.coisa, "https://imgur.com/")
           Para acessar a coluna desejada basta invocar o nome dela:
               >>Fab(self.coisa, "https://imgur.com/").nome_coluna
           Retornará o valor contido na tupla de informação
               >>self.coisa

        O self.taba é um conjunto que utiliza da funcinalidade de compreensão de conjuntos
        (list/set compreention) para alteração da lista mapa em um conjunto com mais características.
        
        .. note::
           **List/set compreetion** é uma maneira de edição/contrução de listas e conjuntos.
           A sintáxe básica é:
               >>[expr for item in lista if cond]
           Sendo que: 
              * as chaves podem ser substituídas por colcheias 
              * expr é a expressão a ser imprimida
              * item é a variável de contagem
              * lista é a lista a ser modificada pelo código da expressão
              * cond são as condições que devem ser satisfeitas para gerar a expressão
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
        "+": Fab(self.coisa, f"{IMGUR}uwYPNlz.png")}  # CERCA

        mapa = mapa if mapa != "" else self.mapa

        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].url_imagem)
        ceu = self.v.a(fabrica["~"].url_imagem, w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(fabrica["*"].url_imagem, w=60, h=60, x=0, y=40, cena=cena)
        
        self.taba = {(i, j): 
            fabrica[imagem].objeto(fabrica[imagem].url_imagem, x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
        cena.vai()
        return cena
        

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
        
    def vazio(self, imagem, x, y, cena):
        """
        Este método define uma fábrica para espaços vazios que estão no cenário.
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