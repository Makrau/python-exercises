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
			print('entrou no if')
			jogador_atual = jogador_atual.proximo_jogador()
			print(Jogador.JOGADOR_1)

