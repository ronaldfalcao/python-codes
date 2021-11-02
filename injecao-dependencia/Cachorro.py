class Cachorro:

	def __init__(self):
		"""
		Iniciando o objeto...
		"""
		pass

	@staticmethod
	def latir():
		"""
		Quando o cachorro está em alerta emite um som de latido.
		:return: string
		"""
		print("Uau!")

	@staticmethod
	def comer():
		"""
		Quando o cachorro está com fome e precisa pedir comida.
		:return: string
		"""
		print("Traz a ração!")

	@staticmethod
	def rosnar():
		"""
		Quando o cachorro se sente ameaçado e emite um sinal de perigo.
		:return: string
		"""
		print("Perigo!")


if __name__ == '__main__':

	rex = Cachorro()

	rex.latir()
	rex.comer()
	rex.rosnar()
