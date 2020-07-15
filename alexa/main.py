# patricia.alexa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
STYLE["width"] = 1150
STYLE["height"] = "550px"

class oi:
    cena = Cena( img = "https://i.imgur.com/POhwRe1.jpg")
    opi = Elemento (img = "https://images.vexels.com/media/users/3/139740/isolated/preview/bfecbaa063a84b2e9bbd9f8b9b41d410-bot--o-de-reprodu----o-redondo-azul-by-vexels.png" , x = 20, y=290)
    ope = Elemento (img = "https://images.vexels.com/media/users/3/139740/isolated/preview/bfecbaa063a84b2e9bbd9f8b9b41d410-bot--o-de-reprodu----o-redondo-azul-by-vexels.png")
    opi.entra(cena)
    ope.entra(cena)
    cena.vai()
oi()