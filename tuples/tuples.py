from collections import namedtuple


def retorna_lista():
	pecas_longboard = namedtuple("Longboard", "shape roda rolamento truck")

	return pecas_longboard(
		shape="Udora",
		roda={"revenge", 70.00, "83a"},
		rolamento=["Black Sheep", "9"],
		truck=["Taura", 1.80]
	)


if __name__ == '__main__':
	compra = retorna_lista()
	print(compra)
	print("Rolamento: " + compra.rolamento[0] + " ABEC " + compra.rolamento[1] + ".")
