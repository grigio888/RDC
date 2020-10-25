import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import tela_largura, tela_altura, tela_resolucao, tela
from modulos.classes import ExibicaoImagemEstatica, Escrever

# classes

class Fundo(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio_ext/fundo.png').convert()

		self.largura = 1080
		self.altura = 2020

		self.automatico()

class Logo(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio_ext/logo.png').convert_alpha()

		self.largura = 950
		self.altura = 600

		self.automatico()

class JanelaInicio(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio_ext/janela_inicio.png').convert_alpha()

		self.largura = 972
		self.altura = 414

		self.automatico()

class Botao(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y, botao):
		super().__init__(pos_x, pos_y)
		self.botao = botao

		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio_ext/botao_largo.png').convert_alpha()

		self.largura = 431
		self.altura = 69

		self.definir_botao()
		self.automatico()

	def definir_botao(self):
		if self.botao == 'largo':
			self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio_ext/botao_largo.png').convert_alpha()
			self.largura = 431
			self.altura = 69

		elif self.botao == 'opcoes':
			self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio_ext/botao_opcoes.png').convert_alpha()
			self.largura = 69
			self.altura = 69

		elif self.botao == 'curto':
			self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes_ext/botao_curto.png').convert_alpha()
			self.largura = 106
			self.altura = 69
