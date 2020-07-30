# patricia.stacy.kwarapp.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Marília Campos Galvao <mail@local.tipo>

Changelog
---------
.. versionadded::    20.07
        Descreva o que você adicionou no código.

"""
from _spy.vitollino.main import Cena,Elemento,Texto, STYLE

STYLE["width"] = 1010
STYLE["heigth"] = "500px"

GLIFOS = {
"&": "https://i.imgur.com/dZQ8liT.jpg",  # OCA ⛺
"^": "https://imgur.com/8jMuupz.png",  # INDIO 
".": "https://i.imgur.com/npb9Oej.png",  # VAZIO 
"_": "https://i.imgur.com/sGoKfvs.jpg",  # SOLO 
"#": "https://imgur.com/ldI7IbK.png",  # TORA 
"@": "https://imgur.com/tLLVjfN.png",  # PICHE 
"~": "https://i.imgur.com/UAETaiP.gif",  # CEU 
"*": "https://i.imgur.com/PfodQmT.gif"  # SOL ☀
}

class Kwarwp():
    def __init__(self, vitollino=None, mapa=MAPA_INICIO, medidas={}):
    self.v = vitollino()
    """Cria um matriz com os elementos descritos em cada linha de texto"""
    mapa = mapa.split()
    """Largura da casa da arena dos desafios, número de colunas no mapa"""
    self.lado, self.col = 100, len(mapa[0])
    self.cena = self.cria(mapa=mapa) if vitollino else None
