# patricia.indio.kwarwp.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" 
Montagem orientada do Kwarwp do zero!

.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

Changelog
---------
.. versionadded::    20.07

"""


GLIFOS = {
"&": "https://i.imgur.com/dZQ8liT.jpg",  # OCA 
"^": "https://imgur.com/8jMuupz.png",  # INDIO 
".": "https://i.imgur.com/npb9Oej.png",  # VAZIO 
"_": "https://i.imgur.com/sGoKfvs.jpg",  # SOLO 
"#": "https://imgur.com/ldI7IbK.png",  # TORA 
"@": "https://imgur.com/tLLVjfN.png",  # PICHE 
"~": "https://i.imgur.com/UAETaiP.gif",  # CEU 
"*": "https://i.imgur.com/PfodQmT.gif",  # SOL 
"+": "https://imgur.com/uwYPNlz.png"   # CERCA
}

MAPA_INICIO = """
+++++++
+..+.@+
+.....+
+^.+.&+
+++++++
"""
class Kwarwp():
    """ Jogo para ensino de programação.
        
        Declara o dicionário GLIFOS que possui a str símbolo do elemento e o correspodente link de imagem
        
        Declara a string MAPA_INICIO que possui a posição dos elementos (GLIFOS) no mapa através da matriz linha x coluna. 
        As linha separadas pela tecla <Enter>, a coluna determinada pelos caracteres colineares em linha singulares.

        :param vitollino: Empacota o engenho de jogo Vitollino.
    """
'''    GLIFOS = {
    "&": "https://i.imgur.com/dZQ8liT.jpg",  # OCA 
    "^": "https://imgur.com/8jMuupz.png",  # INDIO 
    ".": "https://i.imgur.com/npb9Oej.png",  # VAZIO 
    "_": "https://i.imgur.com/sGoKfvs.jpg",  # SOLO 
    "#": "https://imgur.com/ldI7IbK.png",  # TORA 
    "@": "https://imgur.com/tLLVjfN.png",  # PICHE 
    "~": "https://i.imgur.com/UAETaiP.gif",  # CEU 
    "*": "https://i.imgur.com/PfodQmT.gif",  # SOL 
    "+": "https://imgur.com/uwYPNlz.png"   # CERCA
    }
    
    MAPA_INICIO = """
    +++++++
    +..+.@+
    +.....+
    +^.+.&+
    +++++++
    """
'''    
    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
        """
        Contrutor da classe que permite a declaração dos parâmetros iniciais.
        
            >> self.v = vitollino()
       
        Cria um matriz com os elementos descritos em cada linha de texto.
        
            >> self.lado, self.col 
        
        Determina a largura da arena dos desafios, número de colunas no mapa.
        
            >>len(mapa[0]) 
            
        Retorna o número de colunas que existem no mapa.
        """
        mapa = mapa.split()
        self.v = vitollino()
        
        #Largura da casa da arena dos desafios, número de colunas no mapa
        self.lado, self.col = 100, len(mapa[0])
        self.cena = self.cria(mapa=mapa) if vitollino else None
            
    def cria(self, mapa = "  "):
        """
        *Cria o ambiente de programação Kwarwp.*
                
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
        lado = self.lado
        cena = self.v.c(self.GLIFOS["_"])
        ceu = self.v.a(self.GLIFOS["~"], w=lado*self.col, h=lado, x=0, y=0, cena=cena)
        sol = self.v.a(self.GLIFOS["*"], w=60, h=60, x=0, y=40, cena=cena)
        #indio = self.v.a(self.GLIFOS["^"], w=100, h=100, x=300, y=400, cena=cena)
        #oca = self.v.a(self.GLIFOS["&"], w=100, h=100, x=500, y=100, cena=cena)
        #tora = self.v.a(self.GLIFOS["#"], w=100, h=100, x=100, y=400, cena=cena)
        #piche = self.v.a(self.GLIFOS["@"], w=100, h=100, x=100, y=100, cena=cena)        
        #ceu = self.v.a(self.GLIFOS["~"], w=600, h=100, x=0, y=0, cena=cena)        
        #cerca = self.v.a(self.GLIFOS["_"], w=50, h=50, x=0, y=450, cena=cena)
        #cena.vai()       
        for j, linha in enumerate(mapa):
            for i, imagem in enumerate(linha):
                self.cria_elemento( x=i*lado, y=j*lado+lado, cena=cena)
        cena.vai()
        return cena
        
    def cria_elemento(self, x, y, cena):
        """
        Função que retorna o **script do elemento** na posição determinada pela matriz(mapa).
        
        x, y equivalem as posições x, y no canvas do jogo.
        
        cena equivale a "url" atual do jogo.
        
        """
        lado = self.lado
        return self.v.a(self.GLIFOS[imagem], w=lado, h=lado, x=i*lado, y=j*lado+lado, cena=cena)


if __name__ == "__main__":
    """
    class Jogo:
        def __init__(self):
            self.c = Cena
            self.d = self.codigo = Codigo
            self.q = Sala
            self.salao = self.s = Salao
            self.a = Elemento
            self.texto = self.t = Popup
            self.n = Texto
            self.labirinto = self.l = Labirinto
            self.inventario = self.i = INVENTARIO
            self.portal = self.p = Portal
            self.dropper = self.d = Dropper
            self.droppable = self.r = Droppable
            self.musica = self.m = Musica
            self.codigo = Codigo
            self.document = document
            self.html = html
            self.window = win
            self.timer = timer
            pass
        
    STYLE["width"] = 600 -> Altera o canvas do jogo em largura da tela. Recebe int.
    STYLE["height"] = "500px" -> Altera o canvas do jogo em altura da tela. Recebe str.
        
    Kwarwp(Jogo) -> Chama a Classe Kwarwp com o método Jogo da biblioteca Vitollino
    """
    from _spy.vitollino.main import Jogo, STYLE

    STYLE["width"] = 700
    STYLE["height"] = "600px"
    Kwarwp(Jogo)
    #STYLE["width"] = self.lado*self.col
    #STYLE["height"] = str("{}px".format(self.lado*(len(MAPA_INICIO.split()[0]))))