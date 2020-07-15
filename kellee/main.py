# patricia.kellee.main.py

"""
 Iniciando  jogo!

"""
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
#aqui eu importei os cenarios e os elementos
praia= Cena (img = "https://image.freepik.com/vetores-gratis/cena-praia-com-rede_1308-31618.jpg")
jardim= Cena (img = "https://upload.wikimedia.org/wikipedia/commons/8/83/Butchardgardens.jpg")
casa= Cena (img = "https://plantasdecasas.com/storage/2017/07/planta-fachada-casa-115-fr-AG.jpg")
boneca = Elemento (img= "https://i.pinimg.com/originals/05/27/ea/0527ea10d8ef34745e6c808d620c7813.png", tit="Aminoácido", x=20, y=80)
menino = Elemento (img= "https://cdn.vitaclinica.com.br/wp-content/uploads/2018/06/Wagner1.jpg", tit="Aminoácido", x=140, y=80)
cachorro = Elemento (img="https://super.abril.com.br/wp-content/uploads/2018/05/filhotes-de-cachorro-alcanc3a7am-o-c3a1pice-de-fofura-com-8-semanas1.png", tit="Aminoácido", x=140, y=80)
gato = Elemento (imag="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQeeDZ_y9ueUWAbQ7zcWunGjvS7PYeVd-13Jg&usqp=CAU", tit="Aminoácido", x=20, y=80)
#aqui eu coloquei o elemento para entrar na cena
boneca.entra(praia)
menino.entra(praia)
cachorro.entra(jardim)
gato.entra(casa)
#aqui eu falei para o elemento ir para o jardim, então quando clicar na boca ela vai p jardim
boneca.vai=jardim.vai
menino.vai=casa.vai
cachorro.vai=praia.vai
gato.vai=praia.vai
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

