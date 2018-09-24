from impressao import imprimir_jogo_da_velha
import tabuleiro
from jogador import *


def iniciar_jogo():
	jogador_atual = Jogador.JOGADOR_1
	#loop do jogo aqui
	continuar_jogo = True
	while(continuar_jogo):
		imprimir_jogo_da_velha(tabuleiro.tabuleiro)
		posicao = int(input())
		if(tabuleiro.marcar_posicao(jogador_atual, posicao)):
			jogador_atual = jogador_atual.proximo_jogador()
			#verificar_linhas(tabuleiro.tabuleiro)
			verificar_colunas(tabuleiro.tabuleiro)
			#continuar_jogo = !verificar_vitoria(tabuleiro)

def verificar_vitoria(tabuleiro):
	if(verificar_linhas(tabuleiro)):
		return True
	if(verificar_colunas(tabuleiro)):
		return True
	if(verificar_diagonais(tabuleiro)):
		return True

	return False

def verificar_linhas(tabuleiro):
	for linha in tabuleiro:
		if(all((x==linha[0] for x in linha)) and linha[0] != ' '):
			print('linha igual em: ', linha)
			return True
	return False


def verificar_colunas(tabuleiro):
	for i in range(0,3):
		if(all(x[i] == tabuleiro[0][i] for x in tabuleiro) and tabuleiro[0][i] != ' '):
			print('coluna igual em: ', i)
			return True
	return False

