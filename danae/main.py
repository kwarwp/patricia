# patricia.danae.main.py
from browser import document, html
from browser.html import H1 as H, DIV as D, SECTION as S, P, STRONG as B, ARTICLE as R
class App:
    def __init__(self):
        s, c, t, u, h, b, p, w = CONST.CLS + [" "]
        #H, D, S, P, B = CONST.ELM
        document.html = CONST.SITE
        document.body.html = ""
        body = S(D(D(
            H("Hello World", Class=t)+P("My first website with "+B("Bulma"), Class=u),
        Class=c), Class=b), Class=h+w+p)+
        S(D(
            "".join([D("1234"+tx, Class="tile is-parent") for tx in "abcd"])
        Class="tile is-ancestor has-text-centered"), Class="info-tiles")
        document.body <= body
        
class CONST:
    CLS = "section container title subtitle hero hero-body is-primary".split()
    ELM = [html.H1, html.DIV, html.SECTION, html.P, html.STRONG]
    SITE = """<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello Bulma!</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.0/css/bulma.min.css">
  </head>
  <body>
  </body>
"""
    BODY = """  <section class="section">
    <div class="container">
      <h1 class="title">
        Hello World
      </h1>
      <p class="subtitle">
        My first website with <strong>Bulma</strong>!
      </p>
    </div>
"""
App()        

