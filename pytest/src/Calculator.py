class Calculator:

	def __init__(self, adicao, subtracao, multiplicacao, divisao):
		self.adicao = adicao
		self.subtracao = subtracao
		self.multiplicacao = multiplicacao
		self.divisao = divisao

	def add(self, number1, number2, op):
		if op:
			return self.adicao.soma(number1, number2)
		return None

	def sub(self, number1, number2, op):
		if op:
			return self.subtracao.diferenca(number1, number2)
		return None

	def mult(self, number_1, number_2, op):
		if op:
			return self.multiplicacao.multiplication(number_1, number_2)

	def div(self, number_1, number_2, op):
		if op:
			return self.divisao.division(number_1, number_2)
