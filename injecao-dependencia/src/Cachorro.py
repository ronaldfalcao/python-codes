class Cachorro:

	def __init__(self, comportamento):
		self.comportamento = comportamento

	def acionar(self):
		self.comportamento.acao()

