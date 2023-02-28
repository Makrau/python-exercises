#!usr/bin/python
from jogador import *
def iniciar_tabuleiro_vazio():
	tabuleiro_vazio = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	return tabuleiro_vazio

def verificar_posicao(posicao):
	if posicao in posicoes_disponiveis:
		return True

def marcar_posicao(jogador, posicao):
	if(verificar_posicao(posicao)):
		posicoes_disponiveis.discard(posicao)
		linha = int((posicao - 1) / 3)
		coluna = (posicao - 1) % 3
		if(jogador is Jogador.JOGADOR_1):
			tabuleiro[linha][coluna] = 'O'
		elif(jogador is Jogador.JOGADOR_2):
			tabuleiro[linha][coluna] = 'X'
		else:
			print("Jogador invalido!!!")
		return True
	else:
		print("Posicao já ocupada! Escolha uma opcao disponivel.")
		return False


tabuleiro = iniciar_tabuleiro_vazio()
posicoes_disponiveis = set(list(range(1, 10)))