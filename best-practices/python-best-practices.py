#  Algumas boas práticas a serem utilizadas no Python (doc string)

#  importando tipagem de variáveis
from typing import Type


def area_retangulo(lado_maior: float, lado_menor: float):
	"""
	Calcula a área de um retângulo a partir do parâmetro "lado" e retorna o valor baseado na fórmula:

	Área = lado * lado

	:param lado_maior é um valor real que define o lado de maior comprimento de um retângulo

	:param lado_menor é um valor real que define o lado de menor comprimento de um retângulo

	:returns Retorna o valor da área do retângulo baseado na fórmula acima
	"""
	return lado_maior * lado_menor


def area_quadrado(lado: Type[int]):
	return lado * lado


print(area_retangulo(3.0, 4.2))  # OK
print(area_retangulo(3, 4))  # OK
print(area_quadrado(4.2))  # NOK pq é float
print(area_quadrado(4))  # NOK pq..pq..pq?
