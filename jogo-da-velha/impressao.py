#!usr/bin/python3

def imprimir_jogo_da_velha(estrutura_jogo):
	print('   |   |   ')
	print(estrutura_jogo[0][0] + '  |' + estrutura_jogo[0][1] + '  |' + estrutura_jogo[0][2])
	print('___|___|___')
	print(estrutura_jogo[1][0] + '  |' + estrutura_jogo[1][1] + '  |' + estrutura_jogo[1][2])
	print('   |   |   ')
	print('___|___|___')
	print('   |   |   ')
	print(estrutura_jogo[2][0] + '  |' + estrutura_jogo[2][1] + '  |' + estrutura_jogo[2][2])
	print('   |   |   ')
