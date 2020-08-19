# patricia.sucuri.surucucu.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Construção do Kwarwp no vitollino.

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    20.08
        -índio anda pelo mapa.

"""
from _spy.vitollino.main import Jogo, STYLE 
from collections import namedtuple as nt

#largura e altura, respectivamente
#STYLE["width"] = 700
#STYLE["height"] = "600px"


MAPA_INICIAL= """
.........
......|.&
.........
.........
.........
......^..
"""
MAPA_INICIAL2= """
#########
#...##..#
#.@.#&.|#
#.#.##..#
#.....^.#
#########
"""

Ponto = nt("Ponto", "x y")
"""Par de coordenadas na direção horizontal (x) e vertiacal (y)."""
Rosa = nt("Rosa", "n l s o")
"""Rosa dos ventos com as direções norte, leste, sul e oeste."""


class Indio():
    """ Cria estrutura índio que será chamada no kwarwp"""
    #def __init__(self, imagem, x, y, cena):###01###
    def __init__(self, imagem, x, y, cena, taba):###01###Adicionei o taba para ser chamado
        self.lado = lado = Kwarwp.LADO
        self.vaga = self
        self.posicao = (x//lado,y//lado)
        """ O operador // retorna apenas a parte inteira do da divisão.
            esta linha gera a matiz de posição do indio 
        """ 
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self.taba = taba
        
    def anda(self):
        """ Faz o indio caminhar na direcao em que esta olhando"""
        #self.posicao = (self.posicao[0], self.posicao[1]-1) 
        destino = (self.posicao[0], self.posicao[1]-1)
        """Assume-se que o indio está olhando para cima, decrementa-se a posição y"""
        taba = self.taba.taba  #que isso aqui faz?
        if destino in taba:
            vaga = taba[destino]
            """recupera na taba a vaga para o qual o indio irá se tranferir"""
            vaga.acessa(self)
            """Inicia protocolo duplo depacho, pedindo para acessar a vaga"""
        #self.indio.x = self.posicao[0]*self.lado
        #self.indio.y = self.posicao[1]*self.lado
        
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        self.anda()
        
    def sai(self):
        """ Rotina de saída falsa, o objeto Indio é usado como uma vaga nula.
        """
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
    """ Cria um espaço vazio na taba, para alojar os elementos do desafio.
        :param imagem: A figura representando o espaço vazio (normalmente transparente).
        :param x: Coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
    """

    def __init__(self, imagem, x, y, cena, ocupante=None):
        self.lado = lado = Kwarwp.LADO # o lado previsto no tabuleiro
        self.posicao = (x//lado,y//lado-1) #o retorno será sempre um inteiro
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena) # o x e o y são substituiddos pelo mapa
        self._nada = Kwarwp.VITOLLINO.a() # descobrir o pq disso
        self.acessa = self._acessa #
        """É um método dinâmico que varia com o estado da vaga. Inicialmente é _aceesa, ou seja, vago e aceitanto ecupante"""
        self.ocupante = ocupante or self #Importante para o funcionamento dos métodos abaixo
        """O ocupante será definido pelo acessa, por default é o vazio"""
        self.acessa(ocupante)
        
    def _valida_acessa(self, ocupante): 
        """ ESTE É O ESTADO OCUPADO
             Consulta o ocupante atual se há permissão para substituí-lo pelo novo ocupante.
            :param ocupante: O canditato a ocupar a posição corrente.
        """
        self.ocupante.acessa(ocupante)
        
    def _acessa(self, ocupante):
        """ESTE É O ESTADO VAGO
        Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.
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
    
    
class Kwarwp():

    """ Jogo para ensino de programação.
        :param vitollino: Empacota o engenho de jogo Vitollino.
        :param mapa: Texto representando o mapa do desafio
        :param medidas: Dicionário usado para redimensionar a tela
    """
    VITOLLINO = None
    """Referência estática para obter o engenho de jogo"""
    self.o_indio = None
    """Instância do personagem principal, o índio, vai ser atribuído pela fábrica do índio"""
    LADO = None
    """Referência estática para definir o lado do piso da casa"""

    def __init__(self, vitollino=None, mapa = MAPA_INICIAL, medidas = {}):
        Kwarwp.VITOLLINO = self.v = vitollino()
        """Transforma o texto matriz, explicitando o bloco de strings para cada linha."""
        self.mapa = mapa.split()
        """Largura da casa da arena dos desafios, número de colunas no mapa"""
        self.lado, self.coluna, self.linha = 100, len(self.mapa[0]), len(self.mapa)+1
        """Lado, coluna, linha"""
        Kwarwp.LADO = self.lado
        
        self.o_indio = None
        """O personagem principal, o indio, vai ser atribuído pela fábrica do índio"""
        w,h = self.coluna*self.lado, self.linha*self.lado
        """ (largura) w = len(self.mapa[0] * 100 (Requer a quantidade de itens internos à contagem do 
            primeiro indexado do mapa)
            (altura) h = len(self.mapa)+1 * 100 (esse +1 adiciona o valor do tamanho reservado para o céu)
        """
        medidas.update(width=w, height=f"{h}px")
        """Adiciona variáveis ao dicionário implementado no parêmetro medidas"""
        
        self.taba = {}
        """Inicia a existência do dicionário que a partir de coordenada (i,J) localiza um piso da taba a partir 
           das coordenadas i e j
        """
        self.cena = self.cria(mapa=self.mapa) if vitollino else None
        """Tentar entender
        """
        
    def cria(self, mapa=""):
    
        IMGUR = "https://i.imgur.com/"
        """ Gera uma global interna usada na formatação do dicionário fabrica"""
        Fab = nt("Fab", "objeto url")
        """ Resgate do colections.nametuple.
            Criado uma nova coleção de dados, do tipo fab que acolhe informações quanto ao objeto e
            a url deste 
        """
        fabrica ={"#": Fab(self.coisa, f"{IMGUR}uwYPNlz.png"), # CERCA
                 "^": Fab(self.indio, f"{IMGUR}8jMuupz.png"), # INDIO
                 ".": Fab(self.vazio, f"{IMGUR}npb9Oej.png"), #VAZIO
                 "_": Fab(self.coisa, f"{IMGUR}sGoKfvs.jpg"), #SOLO
                 "&": Fab(self.coisa, f"{IMGUR}dZQ8liT.jpg"), #OCA
                 "@": Fab(self.coisa, f"{IMGUR}tLLVjfN.png"), #PICHE
                "*": Fab(self.coisa, f"{IMGUR}PfodQmT.gif"), #SOL
                "~": Fab(self.coisa, f"{IMGUR}UAETaiP.gif"), #CEU
                "|": Fab(self.coisa, f"{IMGUR}ldI7IbK.png")  # TORA 
                }
        
        mapa = mapa if mapa != "" else self.mapa #descobrir o que isso faz
        
        mapa = self.mapa #uguala ao mapa do init
        lado = self.lado #iguala ao lado do init
        cena = self.v.c(fabrica["_"].url)
        """Chama elemento da fábrica [solo] agregando ao seu atributo url para criar a cena"""
        ceu = self.v.a(fabrica["~"].url, w=lado*self.coluna, h=lado, x=0, y=0, cena=cena, vai=self.executa)
        """ Chama elemento da fábrica [ceu] agregando ao seu atributo url para gerar um elemento na cena"""
        sol = self.v.a(fabrica["*"].url, w=60, h=60, x=0, y=40, cena=cena)
        """Gera o elemento sol"""
        self.taba = {(i, j): fabrica[caracter].objeto(fabrica[caracter].url, x=i*lado, y=j*lado+lado, cena=cena)
              for j, linha in enumerate(mapa) for i, caracter in enumerate(linha)}
        """Compreensão de Dicionário. 
           
           Sintaxe: {key:value for key, value in iterable if condition}
           Sintaxe: {key:value for (key,value) in interable}
           
           leitura: Para cada coluna (i), linha (j) : chama caracter específico (acessa atributo) objeto(chama 
           caracter específico (acessa atributo) url específica, posição x, posição y e cena=solo)
           para cada segmento de caracteres e número respectivo, para cada caracter específico e número específico
        """       
        cena.vai()
        return cena
    
    def coisa(self,imagem,x,y,cena):
        """ Cria um elemento na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        Cria uma vaga vazia e coloca o componente dentro dela.
        """
        coisa = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio(imagem, x=x, y=y, cena=cena, ocupante=coisa)
        return vaga
        
    def indio(self, imagem,x,y,cena):
        #self.o_indio = Indio(imagem, x=x, y=y, cena=cena) #era para estar funcionando este imagem mesmo?
        self.o_indio = Indio(imagem, x=0, y=0, cena=cena, taba=self)
        """indio tem deslocamento zro pois é relativo à vaga"""
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante = self.o_indio)
        return vaga   
        
    def vazio(self, imagem, x,y ,cena):
        vaga = Vazio(imagem, x=x, y=y, cena=cena, ocupante=self)
        return vaga
        
    def ocupa(self, *_):
        pass
        
        
    def executa(self, *_):
        """ Ordena a execução do roteiro do índio.
        """
        self.o_indio.executa()
        

if __name__ == "__main__":
    Kwarwp(Jogo, medidas = STYLE) 