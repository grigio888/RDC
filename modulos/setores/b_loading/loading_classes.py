import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import tela_largura, tela_altura, tela_resolucao, tela
from modulos.classes import ExibicaoImagemEstatica, Escrever

# classes

class JanelaLoading(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/b_loading/loading/janela_loading.png').convert_alpha()

		self.largura = 483
		self.altura = 216

		self.automatico()





def func_carregar(lugar_x, lugar_y, porcentagem):
	janela_loading = JanelaLoading(lugar_x, lugar_y)
	texto_loading = Escrever(lugar_x + 2, lugar_y + 1, 'titulo', 'Loading', 'preto')
	texto_carregando = Escrever(lugar_x + 22.3, lugar_y + 6, 'titulo', 'Carregando', 'preto', 'centro')
	texto_carregamento = Escrever(lugar_x + 22.3, lugar_y + 8.1, 'titulo', porcentagem + '%', 'preto', 'centro')

	janela_loading.desenho()
	texto_loading.desenho()
	texto_carregando.desenho()
	texto_carregamento.desenho()