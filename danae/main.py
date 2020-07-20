# patricia.danae.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Usando Bulma para criar páginas formatadas em HTML e CSS.

    Exemplo de um painel de controle do Administrador.

Changelog
---------
    20.07
        * NEW: Exemplo inicial.

"""
from browser import document, html
# from browser.window import __SUPERPYTHON__
from browser import window
from browser.html import H1 as H, DIV as D, SECTION as S, P, STRONG as B, ARTICLE as R
__version__ = "20.07"
__author__ = "Carlo"
import functools
s, c, t, u, h, b, p, w = "section container title subtitle hero hero-body is-primary".split()+[" "]

class bulma(object):
    """Decorator that includes an enclosing DIV
    """
    def __init__(self, clazz="", oid=None, tag=D):
        self.tag = tag
        self.clazz, self.oid = clazz, oid
        # functools.update_wrapper(self, func)  ## TA-DA! ##
    def __call__(self, fn, *args, **kwargs):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            return self.tag(fn(*args, **kwargs), Class=self.clazz, Id=self.oid
                            ) if self.oid else self.tag(
                                    fn(*args, **kwargs), Class=self.clazz)
        return decorated


class section(bulma):
    """Decorator that includes an enclosing SECTION
    """
    def __init__(self, clazz="", oid=None, tag=S):
        super().__init__(clazz=clazz, oid=oid, tag=S)


class article(bulma):
    """Decorator that includes an enclosing ARTICLE
    """
    def __init__(self, clazz="", oid=None, tag=R):
        super().__init__(clazz=clazz, oid=oid, tag=R)

class App:
    """ Implementa um painel de controle de admnistrador.
        Código original em : https://bulmatemplates.github.io/bulma-templates/templates/admin.html
    """
    def __init__(self):
        # s, c, t, u, h, b, p, w = CONST.CLS + [" "]  # alguma constantes para estilo
        document.html = CONST.SITE  # Instala o cabeçalho do documento
        document.body.html = ""
        self.go()
    def _go(self):
        body = S(D(D(
            H("Hello World", Class=t)+P("My first website with "+B("Bulma"), Class=u),
        Class=c), Class=b), Class=h+w+p)+S(D(
        Class="tile is-ancestor has-text-centered", Id="ancestor-tile"), Class="info-tiles")
        # ^^^ constrói a estrutura do corpo, onde 'ancestor-tile' é onde adiciona os ladrilhos

        document.body <= body  # instala os elementos estruturados no corpo do documento
        tiles = document["ancestor-tile"]  # localiza os elemento onde coloca os ladrilhos
        dados = [("435k", "Usuários"), ("53k", "Produtos"), ("735k", "Pedidos"), ("23", "Devoluções")]
        # ^^^ Pares (valor, legenda) que vão ser apresentados nos ladrilhos
        [tiles <= D(R(
                P(valor , Class=t)+P(legenda , Class=u),
            Class="tile is-child box"), Class="tile is-parent") for valor, legenda in dados]
        # ^^^ usa um list comprehension para instalar cada ladrilho no ancestral 'tiles'

    def go(self):
        document.body <= self.topo()+self.tiles()

    @section(h+w+p)
    @bulma(c)
    @bulma(b)
    def topo(self):
        return H("Hello World", Class=t)+P("My first website with "+B("Bulma"), Class=u)

    @section("info-tiles")
    def tiles(self):
        dados = [("435k", "Usuários"), ("53k", "Produtos"), ("735k", "Pedidos"), ("23", "Devoluções")]
        tiles = D(Class="tile is-ancestor has-text-centered")
        [tiles <= self.tile(valor, legenda) for valor, legenda in dados]
        return tiles

    @bulma("tile is-parent")
    @article("tile is-child box")
    def tile(self, valor, legenda):
        return P(valor , Class=t)+P(legenda , Class=u)
       
        
class CONST:
    CLS = "section container title subtitle hero hero-body is-primary".split()
    SITE = """<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello Bulma!</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.0/css/bulma.min.css">
  </head>
  <body>
  </body>
"""

App()  

