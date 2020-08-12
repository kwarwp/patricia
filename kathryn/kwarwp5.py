# patricia.indio.kwarwp.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" 
Montagem orientada do Kwarwp do zero! Parte 6

.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

Changelog
---------
.. versionadded::    20.07

- Andar do índio "para cima" com o clique na imagem do céu.
- Restrição do movimento / Organizando a Taba (aldeia)
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
    """ Jogo para ensino de programação."""   
    VITOLLINO = None
    """Referência estática para obter o engenho de jogo."""
    LADO = None
    """Referência estática para definir o lado do piso da casa."""

    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
        """Contrutor da classe que permite a declaração dos parâmetros iniciais."""        
        Kwarwp.VITOLLINO = self.v = vitollino()
        self.mapa = mapa.split()
        self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        Kwarwp.LADO = self.lado
        w, h = self.col*self.lado, self.lin*self.lado
        medidas.update(width=w, height=f"{h}px")
        self.taba = {}       
        """Instância do personagem principal, o índio, vai ser atribuído pela fábrica do índio"""
        self.o_indio = None
        self.cena = self.cria(mapa=self.mapa) if vitollino else None
            
    def cria(self, mapa = "  "):
        """Este método define uma fábrica de componentes."""
        Fab = nt("Fab", "objeto imagem")
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
        cena = self.v.c(fabrica["_"].imagem)
        
        """No argumento *vai*, associamos o clique no céu com o método **executa ()** desta classe"""
        ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado, x=0, y=0, cena=cena, vai= self.executa) 
        sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena)
        
        self.taba = {(i, j): 
            fabrica[imagem].objeto(fabrica[imagem].imagem, x=i*lado, y=j*lado+lado, cena=cena)
            for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
            
        cena.vai()
        return cena
        
    def executa(self, *_):
        """ Ordena a execução do roteiro do índio.
        
        :param _: este argumento recebe a estrutura oriunda do evento, o _ indica que não será usado."""
        self.o_indio.executa()
    
    def coisa(self, imagem, x, y, cena):
        """ Cria uma vaga vazia e coloca o componente dentro dela. 
            o índio tem deslocamento zero, pois é relativo à vaga"""
        coisa = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        """Aqui o índio está sendo usado para qualquer objeto, enquanto não tem o próprio"""
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        return vaga
        '''
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)'''
        
    def vazio(self, imagem, x, y, cena):
        """ O Kwarwp é aqui usado como um ocupante nulo, que não ocupa uma vaga vazia."""
        vaga = Vazio(imagem, x=x, y=y, cena=cena, ocupante=self)
        return vaga
        '''
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)'''
        
    def indio(self, imagem, x, y, cena):
        # self.o_indio = Indio(imagem, x=x, y=y, cena=cena)
        self.o_indio = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        """o índio tem deslocamento zero, pois é relativo à vaga"""
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=self.o_indio)
        return vaga
        
    def ocupa(self, *_):
        """ O Kwarwp é aqui usado como um ocupante falso, o pedido de ocupar é ignorado.
        """
        pass

class Indio():
    ''' Cria o personagem principal na arena do Kwarwp na posição definida.'''
    def __init__(self, imagem, x, y, cena, taba):
        self.taba = taba
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado, y//lado)  #definir posição (2,6)
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        
    def anda(self):
        '''Faz o indio caminhar olhando rpa cima'''
        destino = (self.posicao[0], self.posicao[1]-1)
        """Assumimos que o índio está olhando para cima, decrementamos a posição **y**"""
        taba = self.taba.taba
        if destino in taba:
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            vaga = taba[destino]
            """Inicia o protocolo duplo despacho, pedindo para acessar a vaga"""
            vaga.acessa(self)

    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar."""
        self.anda()
    
    def sai(self):
        """ Rotina de saída falsa, o objeto Indio é usado como uma vaga nula."""
        pass
        
    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
    
        No caso do índio, retorna o elt do elemento do atributo **self.indio**.
        """
        return self.indio.elt
    
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
    
        :param vaga: A vaga que será ocupada pelo componente.
    
        No caso do índio, requisita que a vaga seja ocupada por ele.
        """
        self.vaga = vaga
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
    
    def acessa(self, ocupante):
        """ Pedido de acesso a essa posição, delegada ao ocupante pela vaga.
    
        :param ocupante: O componente candidato a ocupar a vaga já ocupada pelo índio.

        No caso do índio, ele age como um obstáculo e não prossegue com o protocolo.
        """
        pass
        
class Vazio():
    def __init__(self, imagem, x, y, cena, ocupante=None):
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado, y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        self.ocupante = ocupante or self
        """O ocupante será definido pelo acessa, por default é o vazio"""
        self.acessa(ocupante)
        
    def _valida_acessa(self, ocupante):
        """ Consulta o ocupante atual se há permissão para substituí-lo pelo novo ocupante.
    
            :param ocupante: O canditato a ocupar a posição corrente.
        """
        self.ocupante.acessa(ocupante)
        
    def _acessa(self, ocupante):
        """ Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.

        A responsabilidade de ocupar definitivamente a vaga é do candidato a ocupante
        Caso ele esteja realmente apto a ocupar a vaga e deve cahamar de volta ao vazio
        com uma chamada ocupou.

            :param ocupante: O canditato a ocupar a posição corrente.
        """
        ocupante.ocupa(self)
        
    def ocupou(self, ocupante):
        """ O candidato à vaga decidiu ocupá-la e efetivamente entra neste espaço.

        :param ocupante: O canditato a ocupar a posição corrente.

        Este ocupante vai entrar no elemento do Vitollino e definitivamente se tornar
        o ocupante da vaga. Com isso ele troca o estado do método acessa para primeiro
        consultar a si mesmo, o ocupante corrente usando o protocolo definido em
        **_valida_acessa ()**
        """
        self.vazio.ocupa(ocupante)
        self.ocupante = ocupante
        self.acessa = self._valida_acessa
        
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.

        No caso do espaço vazio, não faz nada.
        """
        pass
        
    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela.
        """
        self.ocupante = self
        self.acessa = self._acessa
        
    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .

        No caso do espaço vazio, vai retornar um elemento que não contém nada.
        """
        return self._nada.elt
        
    
        
if __name__ == "__main__":
    from _spy.vitollino.main import Jogo
    from _spy.vitollino.main import STYLE
    Kwarwp(Jogo, medidas=STYLE)
