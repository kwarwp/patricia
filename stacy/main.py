# patricia.stacy.main.py
""" Projeto Kwarwp

.. codeauthor:: Marília Campos Galvão <marilia.campos.galvao@gmail.com>

Changelog
---------
.. versionadded::    17.09
       
"""
class Kwarwp():
    """ Jogo para ensino de programação.

    :param vitollino: Empacota o engenho de jogo Vitollino.
    :param mapa: Um texto representando o mapa do desafio.
    :param medidas: Um dicionário usado para redimensionar a tela.
    :param indios: Uma coleção com outros índios e outros comportamentos.
    """

def __init__(self, vitollino=None, mapa=None, medidas={}, indios=()):
    Vazio.VITOLLINO = self.v = vitollino()
    self.vitollino = vitollino
    """Referência estática para obter o engenho de jogo."""
    self.mapa = (mapa or MAPA_INICIO).split()
    """Cria um matriz com os elementos descritos em cada linha de texto"""
    self.taba = {}
    """Cria um dicionário com os elementos traduzidos a partir da interpretação do mapa"""
    self.o_indio = NULO
    self.os_indios = []
    """Instância do personagem principal, o índio, vai ser atribuído pela fábrica do índio"""
    self.lado, self.col, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
    """Largura da casa da arena dos desafios, número de colunas e linhas no mapa"""
    Vazio.LADO = self.lado
    """Referência estática para definir o lado do piso da casa."""
    w, h = self.col *self.lado, self.lin *self.lado
    medidas.update(width=w, height=f"{h}px")
    self.indios = deque(indios or [Indio])
    self.cena = self.cria(mapa=self.mapa) if vitollino else None

def cria(self, mapa=""):
    """ Fábrica de componentes.

    :param mapa: Um texto representando o mapa do desafio.
    """
    Fab = nt("Fab", "objeto imagem")
    """Esta tupla nomeada serve para definir o objeto construido e sua imagem."""

    fabrica = {
    "&": Fab(self.maloc, f"{IMGUR}dZQ8liT.jpg"), # OCA
    "^": Fab(self.indio, f"{IMGUR}UCWGCKR.png"), # INDIO
    "$": Fab(self.indio, f"{IMGUR}nvrwu0r.png"), # INDIA
    "p": Fab(self.indio, f"{IMGUR}HeiupbP.png"), # PAJE
    ".": Fab(self.vazio, f"{IMGUR}npb9Oej.png"), # VAZIO
    "_": Fab(self.coisa, f"{IMGUR}sGoKfvs.jpg"), # SOLO
    "#": Fab(self.atora, f"{IMGUR}0jSB27g.png"), # TORA
    "@": Fab(self.barra, f"{IMGUR}tLLVjfN.png"), # PICHE
    "~": Fab(self.coisa, f"{IMGUR}UAETaiP.gif"), # CEU
    "*": Fab(self.coisa, f"{IMGUR}PfodQmT.gif"), # SOL
    "|": Fab(self.coisa, f"{IMGUR}uwYPNlz.png")  # CERCA
    }
    """Dicionário que define o tipo e a imagem do objeto para cada elemento."""
    mapa = mapa if mapa != "" else self.mapa
    """Cria um cenário com imagem de terra de chão batido, céu e sol"""
    mapa = self.mapa
    lado = self.lado
    cena = self.v.c(fabrica["_"].imagem)
    self.ceu = self.v.a(fabrica["~"].imagem, w=lado*self.col, h=lado-10, x=0, y=0, cena=cena, vai=self.passo,
                   style={"padding-top": "10px", "text-align": "center"})
    """No argumento *vai*, associamos o clique no céu com o método **executa ()** desta classe.
       O *ceu* agora é um argumento de instância e por isso é referenciado como **self.ceu**.
    """
    sol = self.v.a(fabrica["*"].imagem, w=60, h=60, x=0, y=40, cena=cena, vai=self.executa)
    """No argumento *vai*, associamos o clique no sol com o método **esquerda ()** desta classe."""
    self.taba = {(i, j): fabrica[imagem].objeto(fabrica[imagem].imagem, x=i*lado, y=j*lado+lado, cena=cena)
        for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
    """Posiciona os elementos segundo suas posições i, j na matriz mapa"""
    cena.vai()
    return cena

def passo(self, *_):
    """ Ordena a execução do roteiro do índio.
    """
    # self.o_indio.esquerda()
    # self.v.executa()
    # self.o_indio.passo()

    [indio.passo() for indio in self.os_indios]


def executa(self, *_):
    """ Ordena a execução do roteiro do índio.
    """
    # self.v.ativa()
    # JogoProxy.ATIVA = True
    # self.o_indio.ativa()
    # self.o_indio.executa()
    # [indio.ativa() and indio.executa() for indio in self.os_indios]
    self.os_indios[0].ativa()
    self.v.ativa()
    self.os_indios[0].executa()

def indio(self, imagem, x, y, cena):
    """ Cria o personagem principal na arena do Kwarwp na posição definida.

    :param x: coluna em que o elemento será posicionado.
    :param y: linha em que o elemento será posicionado.
    :param cena: cena em que o elemento será posicionado.
    """
    self.o_indio = self.indios[0](imagem, x=1, y=0, cena=cena, taba=self, vitollino=self.v)
    """ O índio tem deslocamento zero, pois é relativo à vaga.
        O **x=1** serve para distinguir o indio de outros derivados.
    """
    self.o_indio.indio.vai = lambda *_: self.o_indio.pega()
    """o índio.vai é associado ao seu próprio metodo pega"""
    vaga = Vazio("", x=x, y=y, cena=cena, ocupante=self.o_indio)
    self.os_indios.append(self.o_indio)
    self.indios.rotate()
    """recebe a definição do próximo índio"""
    return vaga
    
    class Indio():
""" Cria o personagem principal na arena do Kwarwp na posição definida.

    :param imagem: A figura representando o índio na posição indicada.
    :param x: Coluna em que o elemento será posicionado.
    :param y: Cinha em que o elemento será posicionado.
    :param cena: Cena em que o elemento será posicionado.
    :param taba: Representa a taba onde o índio faz o desafio.
    :param vitollino: Recebe referência para o vitollino ou proxy.
"""
AZIMUTE = Rosa(Ponto(0, -1),Ponto(1, 0),Ponto(0, 1),Ponto(-1, 0),)
"""Constante com os pares ordenados que representam os vetores unitários dos pontos cardeais."""

def __init__(self, imagem, x, y, cena, taba, vitollino=None):
    self.vitollino = vitollino or Vazio.VITOLLINO
    self.lado = lado = Vazio.LADO
    self.azimute = self.AZIMUTE.n
    """índio olhando para o norte"""
    self.taba = taba
    self.vaga = self
    self.ocupante = NULO
    self.posicao = (x//lado,y//lado)
    self.indio = self.vitollino.e(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
    self.x = x
    """Este x provisoriamente distingue o índio de outras coisas construídas com esta classe"""
    if x:
        self.indio.siz = (lado*3, lado*4)
        """Define as proporções da folha de sprites"""
        self.gira()

def ativa(self):
    """ Ativa o proxy do índio para enfileirar comandos.
    """
    #self.vitollino.ativa()
    self.indio.ativa()


def passo(self):
    self.indio.executa()
