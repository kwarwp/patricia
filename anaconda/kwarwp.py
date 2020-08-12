"""   Implementação do mapa no Kwarwp

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

.. version:: 20.01.1

"""
from _spy.vitollino.main import Jogo, STYLE 
from collections import namedtuple as nt

#largura e altura, respectivamente
#STYLE["width"] = 700
#STYLE["height"] = "600px"


MAPA_INICIAL= """
#########
#...##..#
#.@.#&^.#
#.#.##|.#
#.......#
#########
"""

class Indio():
    """ Segue protocolo duplo despacho"""
    def __init__(self, imagem, x, y, cena):
        self.lado = lado = Kwarwp.LADO
        self.indio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self.vaga = self
        self.posicao = (x//lado,y//lado)
        self.indio = Kwarwp.VIOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        
    def anda(self):
        """ Faz o índio caminhar na direção em que está olhando.
        """
        destino = (self.posicao[0], self.posicao[1]-1)
        #self.posicao = (self.posicao[0], self.posicao[1]-1)
        taba = self.taba.taba
        if destino in taba:
           vaga = taba[destino]
           """Recupera na taba a vaga para a qual o índio irá se transferir"""
           vaga.acessa(self)
           """Inicia protocolo duplo despacho, pedindo para acessar a vaga"""
        
    def executa(self):
        """ Roteiro do índio. Conjunto de comandos para ele executar.
        """
        self.anda()
        
    def vaga(self):
        pass
        
    def sai(self):
       """Rotina de saída falsa, o objeto índio é usado como vaga nula"""
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

class vazio():
    """ Cria um espaço vazio na taba, para alojar os elementos do desafio.

        :param imagem: A figura representando o espaço vazio (normalmente transparente).
        :param x: Coluna em que o elemento será posicionado.
        :param y: Cinha em que o elemento será posicionado.
        :param cena: Cena em que o elemento será posicionado.
        :arg ocupante: Objeto que está ocupando o vazio. Por padrão inicia-se zerado.
      """
    
    def __init__(imagem,x,y,cena,ocupante=None): 
        self.lado = lado = Kwarwp.LADO
        self.posicao = (x//lado, y//lado-1)
        self.vazio = Kwarwp.VITOLLINO.a(imagem, w=lado, h=lado, x=x, y=y, cena=cena)
        self._nada = Kwarwp.VITOLLINO.a()
        self.acessa = self._acessa
        self.ocupante = ocupante or self
        """O ocupante é definido pelo acessa"""
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
        self.lado, self.coluna, self.lin = 100, len(self.mapa[0]), len(self.mapa)+1
        Kwarwp.LADO = self.lado
        w,h = self.coluna*self.lado, self.lin*self.lado
        medidas.update(width=w, height=f"{h}px")
        #medidas = STYLE
        self.taba = {}
        """Dicionário que a partir de coordenada (i,J) localiza um piso da taba"""
        
        self.cena = self.cria(mapa=self.mapa) if vitollino else None

    def cria(self, mapa=""):
    
        IMGUR = "https://i.imgur.com/"
        Fab = nt("Fab", "objeto url")   
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
        
        mapa = mapa if mapa != "" else self.mapa

        mapa = self.mapa
        lado = self.lado
        cena = self.v.c(fabrica["_"].url)
        ceu = self.v.a(fabrica["~"].url, w=lado*self.coluna, h=lado, x=0, y=0, cena=cena, vai=self.executa)
        sol = self.v.a(fabrica["*"].url, w=60, h=60, x=0, y=40, cena=cena)
        """Compreensão de Dicionário. 
           
           Sintaxe: {keyexpression:valuexpression for key, value in iterable if condition}
           Sintaxe: {key:value for (key,value) in interable}
           
           leitura: Para cada coluna (i), linha (j) : chama caracter específico (acessa atributo) objeto(chama 
           caracter específico (acessa atributo) url específica, posição x, posição y e cena=solo)
           para cada segmento de caracteres e número respectivo, para cada caracter específico e número específico
        """ 
        self.taba = {(i, j): fabrica[imagem].objeto(
              fabrica[imagem].url, x=i*lado, y=j*lado+lado, cena=cena)
              for j, linha in enumerate(mapa) for i, imagem in enumerate(linha)}
              
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
        """o índio tem deslocamento zero, pois é relativo à vaga"""
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=coisa)
        """Aqui o índio está sendo usado para qualquer objeto, enquanto não tem o próprio"""
        return vaga
        
    def indio(self, imagem,x,y,cena):
        """ Cria o personagem principal na arena do Kwarwp na posição definida.

        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        """
        # self.o_indio = Indio(imagem, x=x, y=y, cena=cena) 
        self.o_indio = Indio(imagem, x=0, y=0, cena=cena, taba=self.indio) #ver se não vai dar problema posteriormente
        """o índio tem deslocamento zero, pois é relativo à vaga"""
        vaga = Vazio("", x=x, y=y, cena=cena, ocupante=self.o_indio)
        return vaga
        
    def vazio(self, imagem, x,y ,cena):
        """ Cria um espaço vazio na arena do Kwarwp na posição definida.

        :param x: coluna em que o elemento será posicionado.
        :param y: linha em que o elemento será posicionado.
        :param cena: cena em que o elemento será posicionado.
        """
        vaga = Vazio(imagem, x=x, y=y, cena=cena, ocupante=self)
        """ O Kwarwp é aqui usado como um ocupante nulo, que não ocupa uma vaga vazia."""
        return vaga
        
    def ocupa(self, *_):
        """ O Kwarwp é aqui usado como um ocupante falso, o pedido de ocupar é ignorado."""
        pass
        
    def vaga(self):
        pass
        
    def executa(self, *_):
        """ Ordena a execução do roteiro do índio.
        """
        self.o_indio.executa()


if __name__ == "__main__":
    Kwarwp(Jogo, medidas = STYLE) 