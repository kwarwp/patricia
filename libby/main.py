from _spy.vitollino.main import Cena
_version_ = "20.07"
_autor_ = "Carlo_Charles"
CENA_PRAIA = "https://i.imgur.com/zOxshRh.jpg"

class Calcada: 
   """Representa uma cena da calçada"""
   def vai(self):
      """Mostra a cena da Praia"""
      Cena(CENA_PRAIA).vai()

Calcada().vai()