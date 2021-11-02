from src.interfaces import Database


class Base(Database):

	def __init__(self):
		pass

	def select(self):
		print("select")

	def insert(self):
		print("insert")

	def delete(self):
		print("delete")
