# patricia.kellee.main.py

"""
 Iniciando  jogo!

"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
#aqui eu importei os cenarios e os elementos
STYLE["width"] = 1300
STYLE["leight"]= "550px"
praia= Cena (img = "https://i.imgur.com/cdMKAka.png")
erro= Cena (img = "https://i.imgur.com/idqEr5C.png")
casa= Cena (img = "https://plantasdecasas.com/storage/2017/07/planta-fachada-casa-115-fr-AG.jpg")
triste = Elemento (img= "https://i.imgur.com/0R5Xo83.png", tit="CLICK", x=1000, y=100)
feliz = Elemento (img= "https://i.imgur.com/UaihdhW.png", tit="CLICK", x=40, y=80)
codigo1 = Elemento (img="https://i.imgur.com/QGEgNAt.png", tit="CLICK", style=dict(left=80, top=280, width=500, height="250px"))
codigo2 = Elemento (img="https://i.imgur.com/ccJqbMb.png", tit="CLICK", style=dict(left=680, top=280, width=500, height="250px"))
pergunta = Elemento (img= "https://i.imgur.com/fYmNuBj.png", style=dict(left=540, top=80, width=250, height="150px"))
#aqui eu coloquei o elemento para entrar na cena
codigo1.entra(praia)
codigo2.entra(praia)
triste.entra(erro)
feliz.entra(casa)
pergunta.entra(praia)
#aqui eu falei para o elemento ir para o jardim, então quando clicar na boca ela vai p jardim
codigo1.vai=erro.vai
codigo2.vai=casa.vai
triste.vai=praia.vai
feliz.vai=praia.vai
praia.vai()


#from _spy.vitollino.main import Cena, Elemento, STYLE
#_version_="14.07"
#_author_ = "Rosilane"

#FUNDO = "https://image.freepik.com/vetores-gratis/plataforma-de-tileset-e-plano-de-fundo-para-criar-jogos-para-celular_22289-375.jpg"

#def vai():
#	""" Mostrar o Fundo"""
#	Cena(FUNDO).vai()
#vai()


#""" Jogo do Mistério da Praia.

#    Descubra o mistério desta praia.

#Changelog
#---------
 #   20.07
#        * NEW: O jogo original.

#"""
#from _spy.vitollino.main import Cena, Elemento, Texto,STYLE
#from _spy.vitollino.main import INVENTARIO as inv
#from natalia.main import Mar
#from grace.main import Praia
#__version__ = "15.07"
#__author__ = "Rosilane"
#STYLE["width"] = 700
#STYLE["leight"]= "550px"
#CENA_FUNDO = "https://static.vecteezy.com/system/resources/previews/000/561/495/non_2x/gray-white-polygonal-background-creative-design-templates-vector.jpg"
#BANHISTA = "https://i.imgur.com/CWQ00XG.png"
#class Opcao:
 #   """ Representa uma cena da calçada da praia """
 #   def __init__(self):
  #      """ Mostra a cena da praia """
  #      self.cena = Cena(CENA_FUNDO)
  #      self.banhista = Elemento(BANHISTA, x=100, y=200, cena=self.cena)
        
        #Cena(CENA_FUNDO).vai()
   # def vai(self):
   #     """ Mostra a cena da praia """
   #     self.cena.vai()
    #    self.banhista.entra(Praia())
        #Cena(CENA_FUNDO).vai()
    
#if __name__ == "__main__":
#    Opcao().vai()

