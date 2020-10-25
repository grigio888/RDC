import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import tela_largura, tela_altura, tela_resolucao, tela
from modulos.classes import ExibicaoImagemEstatica, Escrever

# classes

class FundoInicio(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/fundo.png').convert()

		self.automatico()

class JanelaLanding(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y, janela):
		super().__init__(pos_x, pos_y)
		self.janela = janela

		self.imagem = 0

		self.lagura = 0
		self.altura = 0

		self.definir_janela()
		self.automatico()

	def definir_janela(self):
		if self.janela == 'cima':
			self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/janela_cima.png').convert_alpha()
			self.largura = 972
			self.altura = 333

		elif self.janela == 'meio':
			self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/janela_meio.png').convert_alpha()
			self.largura = 972
			self.altura = 1244

		elif self.janela == 'baixo':
			self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/janela_baixo.png').convert_alpha()
			self.largura = 972
			self.altura = 333

class Frames(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y, parte):
		super().__init__(pos_x, pos_y)
		self.parte = parte

		self.imagem = 0

		self.lagura = 0
		self.altura = 0

		self.definir_parte()
		self.automatico()

	def definir_parte(self):
		if self.parte == 'frame':
			self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/frame_personagem.png').convert_alpha()
			self.largura = 404
			self.altura = 517

		elif self.parte == 'sombra':
			self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/frame_sombra.png').convert_alpha()
			self.largura = 165
			self.altura = 94

		elif self.parte == 'frame_item':
			self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/frame_item.png').convert_alpha()
			self.largura = 210
			self.altura = 240

class ImagemItem(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y, item_ID, tamanho, escala_de_tamanho = 1):
		super().__init__(pos_x, pos_y)
		self.item_ID = item_ID
		self.tamanho = tamanho

		self.escala_de_tamanho = escala_de_tamanho

		self.imagem = 0

		self.lagura = 0
		self.altura = 0

		self.definir_parte()
		
		self.porcentagem_pos()
		self.transformando_resolucao()
		self.escalando_imagem()

	def definir_parte(self):
		caminho = ('modulos/pack_img/' + str(self.item_ID) + '_' + str(self.tamanho) + '.png')
		self.imagem = pygame.image.load(caminho).convert_alpha()

		if self.tamanho == 0:
			self.largura = 24
			self.altura = 24

		elif self.tamanho == 1:
			self.largura = 75
			self.altura = 100

	def escalando_imagem(self):
		largura_transformada = self.largura * self.escala_de_tamanho
		largura_transformada = round(largura_transformada)

		altura_transformada = self.altura * self.escala_de_tamanho
		altura_transformada = round(altura_transformada)
		
		if tela_resolucao == 1:
			largura_transformada = self.largura * 1.5
			largura_transformada = round(largura_transformada)
			altura_transformada = self.altura * 1.5
			altura_transformada = round(altura_transformada)

		if tela_resolucao == 2:
			largura_transformada = self.largura * 2.25
			largura_transformada = round(largura_transformada)
			altura_transformada = self.altura * 2.25
			altura_transformada = round(altura_transformada)

		if tela_resolucao == 3:
			largura_transformada = self.largura * 3
			largura_transformada = round(largura_transformada)
			altura_transformada = self.altura * 3
			altura_transformada = round(altura_transformada)

		self.transformado = pygame.transform.smoothscale(self.imagem, (largura_transformada, altura_transformada))
