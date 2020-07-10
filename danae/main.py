# patricia.danae.main.py
from browser import document, html
from browser.html import H1 as H, DIV as D, SECTION as S, P, STRONG as B
H, D = html.H1, html.DIV
#document["pydiv"].html = ""
#document["pydiv"] <= D( H("Olá", Class="title"), Class="container")
class App:
    def __init__(self):
        s, c, t, u = CONST.CLS
        #H, D, S, P, B = CONST.ELM
        document.html = CONST.SITE
        document.body.html = ""
        document.body <= S(D(H("Hello World", Class=t)+P("My first website with", Class=u), Class=c), Class=s)
        
class CONST:
    CLS = "section container title subtitle".split()
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

