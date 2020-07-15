# patricia.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, Labirinto, Texto, Codigo, Sala, STYLE
from _spy.vittolino.main import INVENTARIO as inv
#aqui eu importei os cenarios e os elementos
praia= Cena (img = "https://image.freepik.com/vetores-gratis/cena-praia-com-rede_1308-31618.jpg")
jardim= Cena (img = "https://upload.wikimedia.org/wikipedia/commons/8/83/Butchardgardens.jpg")
boneca = Elemento (img= "https://i.pinimg.com/originals/05/27/ea/0527ea10d8ef34745e6c808d620c7813.png")
#aqui eu coloquei o elemento para entrar na cena
boneca.entra(praia)
#aqui eu falei para o elemento ir para o jardim, então quando clicar na boca ela vai p jardim
boneca.vai=jardim.vai
praia.vai()