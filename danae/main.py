# patricia.danae.main.py
from browser import document, html
H, D = html.H1, html.DIV
#document["pydiv"].html = ""
#document["pydiv"] <= D( H("Olá", Class="title"), Class="container")
class App:
    def __init__(self):
        document.html = CONST.SITE
        document.bodi.html = CONST.BODY
        
class CONST:
    SITE = """<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello Bulma!</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.0/css/bulma.min.css">
  </head>
  <body>
  </section>
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

