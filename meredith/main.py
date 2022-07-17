# patricia.meredith.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" 
Projeto para Estudo do Tutorial. 

.. codeauthor:: Erica Scheffel <ericascheffel@nce.ufrj.br>

"""
MAPA_INICIO = """
@....&
......
......
#....^
"""

from _spy.vitollino.main import Cena, Elemento, STYLE

class Indio():
    def __init__(self, imagem, x, y, cena):
        self.lado = lado = Kwarwp.LADO
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self.vaga = self
        self.posicao = (x//lado,y//lado)
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)

    def anda(self):
        """ Faz o índio caminhar na direção em que está olhando."""
        destino = (self.posicao[0], self.posicao[1]-1)
        """Assumimos que o índio está olhando para cima, decrementamos a posição **y**"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            vaga.acessa(self)
            """Inicia o protocolo duplo despacho, pedindo para acessar a vaga"""
        
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar."""
        self.anda()
        
    def sai(self):
        """ Rotina de saída falsa, o objeto Indio é usado como uma vaga nula."""
        pass
        
    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro.
        No caso do índio, retorna o elt do elemento do atributo **self.indio**."""    
        return self.indio.elt

    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        :param vaga: A vaga que será ocupada pelo componente.
        No caso do índio, requisita que a vaga seja ocupada por ele."""    
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga

    def acessa(self, ocupante):
        """ Pedido de acesso a essa posição, delegada ao ocupante pela vaga.
        :param ocupante: O componente candidato a ocupar a vaga já ocupada pelo índio.
        No caso do índio, ele age como um obstáculo e não prossegue com o protocolo."""    
        pass        

class Kwarwp():
    """ Jogo para ensino de programação.
    :param vitollino: Empacota o engenho de jogo Vitollino."""    
    VITOLLINO = None
    """Referência estática para obter o engenho de jogo."""
    LADO = None    
    """Referência estática para definir o lado do piso da casa."""
    
    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
        #self.v = vitollino()
        Kwarwp.VITOLLINO = self.v = vitollino()
        """Cria um matriz com os elementos descritos em cada linha de texto"""
        self.mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas no mapa"""
        self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        Kwarwp.LADO = self.lado
        w, h = self.col *self.lado, self.lin *self.lado
        self.taba = {}
        """Dicionário que a partir de coordenada (i,J) localiza um piso da taba"""
        medidas.update(width=w, height=f"{h}px")
        self.cena = self.cria(mapa=self.mapa) if vitollino else None
        self.o_indio = None
        """Instância do personagem principal, o índio, vai ser atribuído pela fábrica do índio"""

    def cria(self, mapa=" "):
        from collections import namedtuple as nt
        Fab = nt("Fab", "objeto imagem")
        
        fabrica = {
        "&": Fab(self.coisa, f"https://imgur.com/zUbUHO7.png"), # OCA
        "^": Fab(self.indio, f"https://imgur.com/8jMuupz.png"), # INDIO
        ".": Fab(self.vazio, f"https://i.imgur.com/npb9Oej.png"), # VAZIO
        "_": Fab(self.coisa, f"https://i.imgur.com/sGoKfvs.jpg"), # SOLO
        "#": Fab(self.coisa, f"https://imgur.com/izPRRu7.png"), # TORA
        "@": Fab(self.coisa, f"https://imgur.com/eMEESZW.png"), # PICHE
        "~": Fab(self.coisa, f"https://i.imgur.com/UAETaiP.gif"), # CEU 
        "*": Fab(self.coisa, f"https://i.imgur.com/PfodQmT.gif")} # SOL
        
        """ Cria um cenário com imagem de terra de chão batido, céu e sol."""
        """O mapa pode pode ser o definido no argumento ou atributo da instância do Kwarwp."""
        mapa = mapa if mapa != "" else self.mapa

        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].imagem)
        ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado, x=0, y=0, cena=cena, vai= self.executa)
        """No argumento *vai*, associamos o clique no céu com o método **executa ()** desta classe"""
        sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena)                
                
        self.taba = {(i, j): fabrica[imagem].objeto(
            fabrica[imagem].imagem, x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
        
        cena.vai()
        return cena
    
    def executa(self, *_):
        """Ordena a execução do roteiro do índio"""
        self.o_indio.executa()
            
    def coisa(self,imagem, x, y, cena):
        """ Cria um elemento na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        Cria uma vaga vazia e coloca o componente dentro dela."""    
        coisa = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        """o índio tem deslocamento zero, pois é relativo à vaga"""
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        """Aqui o índio está sendo usado para qualquer objeto, enquanto não tem o próprio"""
        return vaga
        
    def vazio(self, imagem, x, y, cena):
        """ Cria um espaço vazio na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado."""    
        vaga = Vazio(imagem, x=x, y=y, cena=cena, ocupante=self)
        """ O Kwarwp é aqui usado como um ocupante nulo, que não ocupa uma vaga vazia."""
        return vaga 
    
    def indio(self, imagem, x, y, cena):
        """ Cria o personagem principal na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado."""
    
        # self.o_indio = Indio(imagem, x=x, y=y, cena=cena)
        self.o_indio = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        """o índio tem deslocamento zero, pois é relativo à vaga"""
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=self.o_indio)
        return vaga
        
    def ocupa(self, *_):
        """ O Kwarwp é aqui usado como um ocupante falso, o pedido de ocupar é ignorado."""
        pass 
       
class Vazio():
    """ Cria um espaço vazio na taba, para alojar os elementos do desafio.
        :param imagem: A figura representando o espaço vazio (normalmente transparente).
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado."""    
    
    def __init__(self, imagem, x, y, cena, ocupante=None):
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado,y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        self.ocupante = ocupante or self
        """O ocupante será definido pelo acessa, por default é o vazio"""
        self.acessa(ocupante) 
        
    def _valida_acessa(self, ocupante):
        """ Consulta o ocupante atual se há permissão para substituí-lo pelo novo ocupante.
        :param ocupante: O canditato a ocupar a posição corrente."""    
        self.ocupante.acessa(ocupante)
        
    def _acessa(self, ocupante):
        """ Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.
        A responsabilidade de ocupar definitivamente a vaga é do candidato a ocupante
        Caso ele esteja realmente apto a ocupar a vaga e deve cahamar de volta ao vazio
        com uma chamada ocupou.
        :param ocupante: O canditato a ocupar a posição corrente."""
        ocupante.ocupa(self)
        
    def ocupou(self, ocupante):
        """ O candidato à vaga decidiu ocupá-la e efetivamente entra neste espaço.
        :param ocupante: O canditato a ocupar a posição corrente.
        Este ocupante vai entrar no elemento do Vitollino e definitivamente se tornar
        o ocupante da vaga. Com isso ele troca o estado do método acessa para primeiro
        consultar a si mesmo, o ocupante corrente usando o protocolo definido em
        **_valida_acessa ()**"""    
        self.vazio.ocupa(ocupante)
        self.ocupante = ocupante
        self.acessa = self._valida_acessa
        
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        No caso do espaço vazio, não faz nada."""    
        pass
        
    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela."""    
        self.ocupante = self
        self.acessa = self._acessa
        
    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso do espaço vazio, vai retornar um elemento que não contém nada."""
        return self._nada.elt

if __name__ == "__main__":
    from _spy.vitollino.main import Jogo
    STYLE["width"]=600
    STYLE["height"]=500
    Kwarwp(Jogo)      
