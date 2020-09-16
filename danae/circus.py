# patricia.danae.circus.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    20.09
        Descreva o que você adicionou no código.

"""
from random import shuffle
class Letra:
    TRANSP= "https://i.imgur.com/npb9Oej.png"
    def __init__(self, cena, x, y, lt="A"):
        OFF = 0x24B6 - ord("A")
        la = j.a(self.TRANSP, x=x+15, y=y ,w=90, h=90, style={'font-size': '52pt'}, cena=cena)
        la.elt.html = chr(OFF+ord(lt))
        
        
class Piso:
    #ALDEIA = "https://i.imgur.com/Gqoucvd.png"
    #ALDEIA = "https://i.imgur.com/UCWGCKR.png"
    ALDEIA = "https://i.imgur.com/xsjhNjh.png"
    def __init__(self, cena, x, y, ai="NA"):
        azz = {key: nk*90 for nk, key in enumerate("NLSO")}
        pos = {key: (-(nk%4)*100, -(nk//4)*100) for nk, key in enumerate("ABCDEFGHIJKL")}
        tile = 100
        az = azz[ai[1]]
        self.elt = Aldeia.J.a(self.ALDEIA, x=x, y=y, w=tile, h=tile, cena=cena, style=dict(transform=f"rotate({az}deg)"))
        self.elt.pos = pos[ai[0]]
        self.elt.siz = (400, 300)
    def possize(self, pos, siz=None):
        self.elt.pos = pos
        self.elt.siz = siz if siz else self.elt.siz
        
class Aldeia:
    ALDEIA = "https://i.imgur.com/Gqoucvd.png"
    ESPRIT = "https://i.imgur.com/XFVLtJE.png"
    MAPING = "https://i.imgur.com/MRmfpAv.png"
    YARA = "https://i.imgur.com/RfLJEhs.png"
    TRANSP= "https://i.imgur.com/npb9Oej.png"
    J = None
    ORDERED_KEYS = [['Coycol', 'Cauha', 'Tetlah'],
                    ['Huatlya', 'Zitllo', 'Micpe'],
                    ['Nenea', 'Cahuitz', 'Pallotl']]
    KEYS = [key for line in ORDERED_KEYS for key in line]
    shuffle(KEYS)
    KEYS = [KEYS[n:n+3] for n in range(0,9,3)] 
    COUNT = 2
    #ALDEIA = "https://i.imgur.com/UCWGCKR.png"
    def __init__(self, j):
        Aldeia.J = j
        tile = 100
        self.shuffle_keys = self.ORDERED_KEYS[:]
        self.cena = cena = j.c("https://i.imgur.com/sGoKfvs.jpg")
        self.logger = j.a(self.TRANSP, x=0, y=500, w=900, h=100, cena=cena)
        # self.guia()
        self.desafios = [self.guia, self.desafio0, self.desafio0, self.desafio1, self.desafio2, self.desafio3, self.desafio4]
        cena.vai()
    def log(self, log):
        print(log)
        self.logger.elt.html = log
    def guia(self):
        cena = self.cena
        big = "LS JN HN JN HN KO HO AN FN FN BN IL JO DO AO BL DO JL IO AO DS DN CL HL GS JS HS HS JS GL".split()
        small = "AN DN DS CN IN HN HN AS IO KN KL KO GS DS DN KN".split()
        a = [Piso(cena, nk%4*150, nk//4*150, ai+"N" ) for nk, ai in enumerate("ABCDEFGHIJKL")]
        c = [Piso(cena, 600+nk%3*100, nk//3*100, ai ) for nk, ai in enumerate("LS JN LO JO FN JL GS JS GL".split())]
        d = [Letra(cena, nk%4*150, nk//4*150, lt ) for nk, lt in enumerate("ABCDEFGHIJKL")]
        e = [Piso(cena, 200+nk%4*150, 450+nk//4*150, "A"+ai ) for nk, ai in enumerate("NLSO")]
        #Letra(cena, 0, 0, "A")
        e = [Letra(cena, 200+nk%4*150, 450+nk//4*150, lt ) for nk, lt in enumerate("NLSO")]
    def todos(self):
        cena = self.cena
        big = "LS JN HN JN HN KO HO AN FN FN BN IL JO DO AO BL DO JL IO AO DS DN CL HL GS JS HS HS JS GL".split()
        small = "AN DN DS CN IN HN HN AS IO KN KL KO GS DS DN KN".split()
        # a = [Piso(cena, nk%4*150, nk//4*150, ai+"N" ) for nk, ai in enumerate("ABCDEFGHIJKL")]
        b = [Piso(cena, nk%6*100, nk//6*100, ai ) for nk, ai in enumerate(big)]
        c = [Piso(cena, 600+nk%3*100, nk//3*100, ai ) for nk, ai in enumerate("LS JN LO JO FN JL GS JS GL".split())]
        #     for x in range(4) for y in range(3)]
        D = [Piso(cena, 600+nk%3*100, 300+nk//3*100, ai ) for nk, ai in enumerate("AN JN BN DO EO DO KL HS KN".split())]
        # b = [spr(a[x*3+y], x, y) for x in range(4) for y in range(3)]
        D = [Piso(cena, 900+nk%4*100, nk//4*100, ai ) for nk, ai in enumerate(small)]
        j.a(self.ESPRIT, x=220, y=220,w=60, h=60, cena=cena)
        j.a(self.MAPING, x=420, y=220,w=60, h=60, cena=cena)
        j.a(self.YARA, x=520, y=20,w=60, h=60, cena=cena)
        
    def desafio0(self, solucao):
        c = [Piso(self.cena, i*100, j*100, ai ) for i, linha in enumerate(solucao) for j, ai in enumerate(linha)]
        
    def desafio1(self, solucao):
        c = [[solucao[ai] for ai in linha] for linha in self.ORDERED_KEYS]
        self.desafio0(c)
        
    def desafio2(self, solucao):
        c = [[solucao[ai] for ai in linha] for linha in self.KEYS]
        self.desafio0(c)
        
    def desafio3(self, solucao):
        self.desafio2(solucao)
        keys = [key for line in self.ORDERED_KEYS for key in line]
        shuffle(keys) if not Aldeia.COUNT else None
        Aldeia.KEYS = [[keys[n:n+3]] for n in range(0,9,3)] 
        self.log(f"{Aldeia.COUNT} Aldeia.KEYS: {Aldeia.KEYS} XXXkeysXXX  {keys}")
        Aldeia.COUNT = Aldeia.COUNT -1 if Aldeia.COUNT else 2
        
    def desafio4(self, solucao):
        c = [[solucao[ai] for ai in linha] for linha in self.ORDERED_KEYS]
        self.desafio0(c)

        
    def circus(self, desafio, solucao):
        self.desafios[desafio](solucao)
        
        # b = [spr(a[x*4+y],x,y) for x in range(4) for y in range(3)]
        #a[0].siz = (400, 300)
        #a[0].entra(cena)
def circus(desafio, solucao):
    Aldeia(Jogo()).circus(desafio, solucao)
        
def desafio0():
    TOPO_ESQUERDA = "AN"
    TOPO_DIREITA = "AN"
    TOPO_CENTRO = "AN"
    MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "AN", "AN", "AN"
    FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA =  "AN", "AN", "AN"

    # O comando abaixo voce vai entender no próximo desafio
    circus(1, [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
            MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]])
        
def desafio1():
    MASMORRA = [[ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"]
                ]

    circus(2, MASMORRA)
        
        
def desafio2(lev=3):

    MASMORRA = {'Cahuitz': 'AN', 'Cauha': 'BN', 'Coycol': 'CN',
     'Huatlya': 'DN', 'Micpe': 'EN', 'Nenea': 'FN',
     'Pallotl': 'GN', 'Tetlah': 'HN', 'Zitllo': 'IN'}

    circus(lev, MASMORRA)
    

if __name__ == "__main__":
    from _spy.vitollino.main import Jogo, STYLE
    STYLE.update(width=1300, height="600px")
    #Aldeia(Jogo())
    desafio2(5)
        