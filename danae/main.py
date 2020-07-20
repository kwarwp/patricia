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
from browser import window, document
from browser.html import H1 as H, DIV as D, SECTION as S, P, STRONG as B, ARTICLE as R
__version__ = "20.07"
__author__ = "Carlo"
import functools


def if_edit(ev):
    if ev.altKey:
        window.__SUPERPYTHON__._edit
document.onclick = if_edit

class bulma(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    def __init__(self, func, clazz):
        self.tag = D
        self.clazz = clazz
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)  ## TA-DA! ##
    def __call__(self, *args, **kwargs):
        return D(self.func(*args, **kwargs), Class=self.clazz)


class App:
    """ Implementa um painel de controle de admnistrador.
        Código original em : https://bulmatemplates.github.io/bulma-templates/templates/admin.html
    """
    def __init__(self):
        s, c, t, u, h, b, p, w = CONST.CLS + [" "]  # alguma constantes para estilo
        document.html = CONST.SITE  # Instala o cabeçalho do documento
        document.body.html = ""  
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

