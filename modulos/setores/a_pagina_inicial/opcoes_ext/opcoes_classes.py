import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import tela_largura, tela_altura, tela_resolucao, tela
from modulos.classes import ExibicaoImagemEstatica, Escrever

# classes

class JanelaOpcoes(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes_ext/janela_opcoes.png').convert_alpha()

		self.largura = 920
		self.altura = 539

		self.automatico()

class CaixaConfirmadora(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_marcada.png').convert_alpha()

		self.marcado = True

		self.largura = 35
		self.altura = 35

		self.automatico()

	def mudanca_de_estado(self, valor):
		if valor == 1:
			if self.marcado:
				self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_nao_marcada.png').convert_alpha()
				self.marcado = not self.marcado
			else:
				self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_marcada.png').convert_alpha()
				self.marcado = not self.marcado
		
class BDIEsteira(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_esteira.png').convert_alpha()

		self.largura = 542
		self.altura = 32

		self.automatico()

class BDISetas(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y, estado):
		super().__init__(pos_x, pos_y)
		self.imagem = 0
		self.menor = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_menor.png').convert_alpha()
		self.maior = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_maior.png').convert_alpha()

		self.largura = 35
		self.altura = 46

		self.estado = estado
		self.mudanca_de_estado()

		self.automatico()

	def mudanca_de_estado(self):
		if self.estado == 'menor':
			self.imagem = self.menor
		if self.estado == 'maior':
			self.imagem = self.maior

class EsferaMarcadora(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes_ext/esfera_marcadora.png').convert_alpha()

		self.largura = 27
		self.altura = 32

		self.automatico()
