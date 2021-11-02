class DivisionOperation:

	def division(self, number_1, number_2):
		try:
			return number_1 / number_2
		except ZeroDivisionError:
			pass
