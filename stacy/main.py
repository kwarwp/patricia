# patricia.stacy.main.py
""" Projeto Kwarwp

.. codeauthor:: Marília Campos Galvão <marilia.campos.galvao@gmail.com>

Changelog
---------
.. versionadded::    20.08
        - índio anda pelo mapa.
        - Armadilha Piche
        - Destino Oca
"""
from _spy.vitollino.main import Jogo, STYLE 
from collections import namedtuple as nt


MAPA_INICIAL= """
#########
#...#....
#.@.#&.|#
#.#.#...#
#.....^.#
#########
"""

Ponto = nt("Ponto", "x y")
"""Par de coordenadas na direção horizontal (x) e vertiacal (y)."""
Rosa = nt("Rosa", "n l s o")
"""Rosa dos ventos com as direções norte, leste, sul e oeste."""


class Indio():
    """ Cria estrutura índio que será chamada no kwarwp"""
    AZIMUTE = Rosa(Ponto(0, -1),Ponto(1, 0),Ponto(0, 1),Ponto(-1, 0))
    """ Norte, leste, sul, oeste; 
        
        Constante com os pares ordenados que representam os vetores unitários dos pontos cardeais.
    """

    def __init__(self, imagem, x, y, cena, taba, vai=None):
    
        self.lado = lado = Kwarwp.LADO
        self.azimute = self.AZIMUTE.n
        """índio olhando para o norte"""
        self.taba = taba
        self.vaga = self
        self.posicao = (x//lado,y//lado)
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self.x = x
        """Este x provisoriamente distingue o índio de outras coisas construídas com esta classe"""
        if x:
            self.indio.siz = (lado*3, lado*4)
            """Define as proporções da folha de sprites"""
            self.mostra()
            
    def empurra(self):
        """Objeto tenta sair, tem que consultar a vaga onde está"""
        # self.vaga.sair() # esta parte vai ser feita mais tarde.
        ...
        # de resto o código é semelhante ao _anda
        """ Registra o empurrante para uso no procolo e inicia dispathc com a vaga.

            :param requistante: O ator querendo pegar o objeto.
        """
        self.empurrante = empurrante
        # continue aqui com o início do double dispatch para ocupar a vaga na direção do azimute
        self.vaga # acrescente o resto do comndo

    def mostra(self):
        """ Modifica a figura (Sprite) do índio mostrando para onde está indo.
        """
        sprite_col = sum(self.posicao) % 3
        """ Soma o conteúdo da tupla e pede o resto da divisão por 3.
            Faz com que três casas adjacentes tenha valores diferentes para a coluna do sprite
        """
        sprite_lin = self.AZIMUTE.index(self.azimute)
        """A linha do sprite depende da direção que índio está olhando"""
        self.indio.pos = (-self.lado*sprite_col, -self.lado*sprite_lin)
        """@pos.setter
           def pos(self, xy):
           Recebe uma tupla de inteiros definindo a posição da imagem do elemento
        
            :param xy: x - posição da imagem na horizontal a partir da esquerda
            :param xy: y - posição da imagem na vertical a partir do topo
        
           self.elt.style.backgroundPosition = '{}px {}px'.format(*xy)
        """
    def esquerda(self):
        """ Faz o índio mudar da direção em que está olhando para a esquerda.
        """
        self.azimute = self.AZIMUTE[self.AZIMUTE.index(self.azimute)-1]
        """ -1 referencia à leitura da lista."""
        self.mostra()
    
    def direita(self):
        """ Faz o índio mudar da direção em que está olhando para a direita.
        """
        self.azimute = self.AZIMUTE[self.AZIMUTE.index(self.azimute)-3]
        """ -3 referencia à leitura da lista."""
        self.mostra()

    def fala(self, texto=""):
        """ O índio fala um texto dado.
        :param texto: O texto a ser falado.
        """
        self.taba.fala(texto)  

    def anda(self):
        """Objeto tenta sair, tem que consultar a vaga onde está"""
        self.vaga.sair()

    def sair(self):
        """Objeto de posse do índio tenta sair e é autorizado"""
        self.vaga.ocupante.siga()

    def siga(self):
        """Objeto tentou sair e foi autorizado"""
        self._anda()

    def _anda(self):
        """ Faz o índio caminhar na direção em que está olhando.
        """
        destino = (self.posicao[0]+self.azimute.x, self.posicao[1]+self.azimute.y)
        """A posição para onde o índio vai depende do vetor de azimute corrente"""
        taba = self.taba.taba
        if destino in taba:
            vaga = taba[destino]
            """Recupera na taba a vaga para a qual o índio irá se transferir"""
            vaga.acessa(self)   

    def sai(self):
        """ Rotina de saída falsa, o objeto Indio é usado como uma vaga nula.
        """
        pass

    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        :param vaga: A vaga que será ocupada pelo componente.
        No caso do índio, requisita que a vaga seja ocupada por ele.
        """
        vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga

    def acessa(self, ocupante):
        """ Pedido de acesso a essa posição, delegada ao ocupante pela vaga.
        :param ocupante: O componente candidato a ocupar a vaga já ocupada pelo índio.
        No caso do índio, ele age como um obstáculo e não prossegue com o protocolo.
        """
        pass
    
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        self.anda()
            
    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso do índio, retorna o elt do elemento do atributo **self.indio**.
        """
        return self.indio.elt
        

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
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado leniente, aceitando saidas"""
        
    def _sair(self):
        self.ocupante.siga()

    def _pede_sair(self):
        self.ocupante.sair()
        
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
        self.sair = self._pede_sair    
    
    def ocupa(self, vaga):
        """ Pedido por uma vaga para que ocupe a posição nela.
        No caso do espaço vazio, não faz nada.
        """
        pass
        
    def sai(self): #
        """ Pedido por um ocupante para que desocupe a posição nela.
        """
        self.ocupante = self
        self.acessa = self._acessa
        self.sair = self._sair
    
    @property
    def elt(self): 
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso do espaço vazio, vai retornar um elemento que não contém nada.
        """
        return self.vazio.elt
        #return self._nada.elt essa linha antes fazia com que o piche "colasse" no sol

class Piche(Vazio):
    def __init__(self, imagem, x, y, cena, taba):
        self.taba = taba
        self.vaga = taba
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado,y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=0, y=0, cena=cena)
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado vago, aceitando ocupantes"""
        
    def sai(self):
        """ Pedido por um ocupante para que desocupe a posição nela.
        """
        ... # faz as coisas normais que fazia quando usava o sai do Vazio
        
        
        self.vaga.limpa()
    def ocupa(self, vaga):
        self.vaga.sai()
        self.posicao = vaga.posicao
        vaga.ocupou(self)
        self.vaga = vaga
        
    def _pede_sair(self):
        self.taba.fala("Você ficou preso MUAHAHAHA")
        
class Vazio():
    """ Cria um espaço vazio na taba, para alojar os elementos do desafio.

        :param imagem: A figura representando o índio na posição indicada.
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
    """
    VITOLLINO, LADO = None, None

    def __init__(self, imagem, x, y, cena, ocupante=None):
    
    def limpa(self):
        """ Pedido por um ocupante para ele seja eliminado do jogo.
        """
        self._nada.ocupa(self.ocupante)
        """a figura do ocupante vai ser anexada ao elemento nada, que não é apresentado"""
        ... # faz as coisas normais que o método sai faz


class Oca(Piche):

    def __init__(self, imagem, x, y, cena, taba):
        self.taba = taba
        self.vaga = taba
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado,y//lado-1)
        self.maloc = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=0, y=0, cena=cena) #ACHO QUE DEVE TROCAR POR PICHE AQUI
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        """O **acessa ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_acessa ()** que é o estado vago, aceitando ocupantes"""
        self.sair = self._sair
        """O **sair ()** é usado como método dinâmico, variando com o estado da vaga.
        Inicialmente tem o comportamento de **_sair ()** que é o estado vago, aceitando ocupantes"""
        
    def sai(self):
        ... # O que devemos fazer aqui para que a oca não seja removida?
    
    def _pede_sair(self):
        """Objeto tenta sair mas não é autorizado"""
        self.taba.fala("Você chegou no seu objetivo")
        
    def _acessa(self, ocupante):
        """ Atualmente a posição está vaga e pode ser acessada pelo novo ocupante.
        A responsabilidade de ocupar definitivamente a vaga é do candidato a ocupante
        Caso ele esteja realmente apto a ocupar a vaga e deve cahamar de volta ao vazio
        com uma chamada ocupou.
            :param ocupante: O canditato a ocupar a posição corrente.
        """
        self.taba.fala("Você chegou no seu objetivo")
        ocupante.ocupa(self)        

    @property
    def elt(self):
        """ A propriedade elt faz parte do protocolo do Vitollino para anexar um elemento no outro .
        No caso da oca, vai retornar o maloc.
        """
        return self.maloc.elt
        
         
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
                 "^": Fab(self.indio, f"{IMGUR}UCWGCKR.png"), # INDIO
                 ".": Fab(self.vazio, f"{IMGUR}npb9Oej.png"), #VAZIO
                 "_": Fab(self.coisa, f"{IMGUR}sGoKfvs.jpg"), #SOLO
                 "&": Fab(self.maloc, f"{IMGUR}dZQ8liT.jpg"), #OCA
                 "@": Fab(self.barra, f"{IMGUR}tLLVjfN.png"), #PICHE
                "*": Fab(self.coisa, f"{IMGUR}PfodQmT.gif"), #SOL
                "~": Fab(self.coisa, f"{IMGUR}UAETaiP.gif"), #CEU
                "|": Fab(self.coisa, f"{IMGUR}ldI7IbK.png")  # TORA 
                }
        """Dicionário que define o tipo e a imagem do objeto para cada elemento"""
        mapa = mapa if mapa != "" else self.mapa #descobrir o que isso faz
        """Cria um cenáriocom imagem de terra de chão batido, ceu e sol"""
        mapa = self.mapa 
        lado = self.lado 
        cena = self.v.c(fabrica["_"].url)
        """Chama elemento da fábrica [solo] agregando ao seu atributo url para criar a cena"""
        self.ceu = self.v.a(fabrica["~"].url, w=lado*self.coluna, h=lado-10, x=0, y=0, cena=cena, vai=self.executa,
                   style={"padding-top": "10px", "text-align": "center"})
        """No argumento *vai*, associamos o clique no céu com o método **executa ()** desta classe.
           O *ceu* agora é um argumento de instância e por isso é referenciado como **self.ceu**.
        """
        
        sol = self.v.a(fabrica["*"].url, w=60, h=60, x=0, y=20, cena=cena, vai = self.esquerda)
        """No argumento *vai*, associamos o clique no sol com o método **esquerda ()** desta classe.""""""Gera o elemento sol"""

        self.taba = {(i, j): fabrica[caracter].objeto(fabrica[caracter].url, x=i*lado, y=j*lado+lado, cena=cena)
              for j, linha in enumerate(mapa) for i, caracter in enumerate(linha)}
        """Posiciona os elementos segundo suas posições i, j na matriz mapa"""     
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
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        return vaga
        
    def indio(self, imagem,x,y,cena):
        #self.o_indio = Indio(imagem, x=x, y=y, cena=cena) #era para estar funcionando este imagem mesmo?
        self.o_indio = Indio(imagem, x=1, y=2, cena=cena, taba=self)#estou precisando de um deslocamento mínimo. pq?
        """indio tem deslocamento zro pois é relativo à vaga"""
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante = self.o_indio)
        return vaga 
        
    def maloc(self, imagem, x, y, cena):
        """ Cria uma maloca na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        Cria uma vaga vazia e coloca o componente dentro dela.
        """
        coisa = Oca(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante= coisa)
        return vaga
        
    def barra(self, imagem, x, y, cena):
        """ Cria uma armadilha na arena do Kwarwp na posição definida.
        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        Cria uma vaga vazia e coloca o componente dentro dela.
        """
        coisa = Piche(imagem, x=0, y=0, cena=cena, taba=self)
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        return vaga
        
    def fala(self, texto=""):
        """ O Kwarwp é aqui usado para falar algo que ficará escrito no céu.
        """
        self.ceu.elt.html = texto
        pass

    def esquerda(self, *_):
        """ Ordena a execução do roteiro do índio.
        """
        self.o_indio.esquerda()
        
    def direita(self, *_):
        """ Ordena a execução do roteiro do índio.
        """
        self.o_indio.direita()
        
    def vazio(self, imagem, x,y ,cena):
        vaga = Vazio(imagem, x=x, y=y, cena=cena, ocupante=self)
        return vaga
        
    def ocupa(self, *_):
        """ O Kwarwp é aqui usado como um ocupante falso, o pedido de ocupar é ignorado."""
        pass
        
    def sai(self, *_):
        """ O Kwarwp é aqui usado como uma vaga falsa, o pedido de sair é ignorado."""
        pass
        
    def executa(self, *_):
        """ Ordena a execução do roteiro do índio.
        """
        self.o_indio.executa()
        

if __name__ == "__main__":
    Kwarwp(Jogo, medidas = STYLE) 