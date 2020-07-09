# patricia.roxanne.main.py
class Pessoa:
	def __init__(self, nome, idade, profissao, nick):
		self.nome = nome
		self.idade = idade        
		self.profissao = profissao
		self.nick = nick

	def sobre_pessoa(self):
		print(f'Nome: {self.nome} | Idade: {self.idade} | Profissão: {self.profissao} | Redes Sociais: {self.nick}')

isaac = Pessoa('Isaac', 27, 'Analista', 'idcesares')
isaac.sobre_pessoa()



#Olá doginho
#def ola(nome):
#	print(f': Olá, {nome}, meu nome é doginho!')
#nome = input("Digite o seu nome: ")    
#ola(nome)
