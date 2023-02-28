#!usr/bin/python3
from enum import Enum
class Jogador(Enum):
	JOGADOR_1 = 1
	JOGADOR_2 = 2

	def proximo_jogador(self):
		if(self is Jogador.JOGADOR_1):
			return Jogador.JOGADOR_2
		elif(self is Jogador.JOGADOR_2):
			return Jogador.JOGADOR_1
		else:
			print('Erro ao mudar jogador')