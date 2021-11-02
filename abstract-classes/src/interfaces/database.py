from abc import ABC, abstractmethod


class Database(ABC):

	@abstractmethod
	def select(self):
		raise Exception("É necessário implementar o método select()")

	@abstractmethod
	def insert(self):
		raise Exception("É necessário implementar o método insert()")

	@abstractmethod
	def delete(self):
		raise Exception("É necessário implementar o método delete()")
