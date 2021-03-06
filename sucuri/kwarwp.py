"""   Implementação do mapa no Kwarwp

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

.. version:: 20.01.1
       - Mapa 
       - Indio Independente
      
"""
from _spy.vitollino.main import Jogo, STYLE 
from collections import namedtuple as nt


MAPA_INICIAL2= """
#########
#...##..#
#.@.#&^.#
#.#.##|.#
#.......#
#########
"""
MAPA_INICIAL= """
......@..
.........
......^..
.......
.........

"""


class Indio():
    """ Cria estrutura índio que será chamada no kwarwp"""
    def __init__(self, imagem, x, y, cena):
        self.lado = lado = Kwarwp.LADO
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self.posicao = (x//lado,y//lado)
        """ O operador // retorna apenas a parte inteira do da divisão.
            esta linha gera a matiz de posição do indio 
        """ 
        
    def anda(self):
        """ Faz o indio caminhar na direcao em que esta olhando"""
        self.posicao = (self.posicao[0], self.posicao[1]-1)
        """A posição é matrizada em uma tupla onde a primeira posição parte do zero e a segunda posição 
           parte do um pois almeja-se que o índio ande apenas para cima (y).
           Essa posição é a default, ou seja, a decrementação do y em um inteiro é o posicionamento do 
           índio com alteração incial 0 em y.
        """
        self.indio.x = self.posicao[0]*self.lado
        self.indio.y = self.posicao[1]*self.lado
        """Acumula o valor resultante, aplicando na próxima execução.
           executa():
           x => posição inicial valor 0 * 100 = 0 (nova posição em x)
           y => posição inicial valor 1 * 100 = 100 (nova posição em y)
        """
        
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        self.anda()
    
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
        
        lado = self.lado
        return self.v.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        
    def indio(self, imagem,x,y,cena):
        self.o_indio = Indio(imagem, x=x, y=y, cena=cena) #era para estar funcionando este imagem mesmo? Troquei para caracter 
        #e funcionou normalmente.
        return self.o_indio
    
    #def solo(self):
        #self.o_solo = self.v.c(self.solo.url)
        #return self.o_solo
    #Tentativa fracassada de chamar a cena de outra forma    
        
    def vazio(self, imagem, x,y ,cena):
        lado = self.lado
        return Indio(imagem, x=x, y=y, cena=cena)
        
    def vaga(self):
        pass
        
    def executa(self, *_):
        """ Ordena a execução do roteiro do índio.
        """
        self.o_indio.executa()


if __name__ == "__main__":
    Kwarwp(Jogo, medidas = STYLE)