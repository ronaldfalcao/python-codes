from src.Cachorro import Cachorro
from src.acoes.rosnar import EmitirRosnado
from src.acoes.latir import EmitirLatido

if __name__ == '__main__':
	cachorro_bravo = Cachorro(EmitirRosnado())
	cachorro_bravo.acionar()
	cachorro_alerta = Cachorro(EmitirLatido())
	cachorro_alerta.acionar()
