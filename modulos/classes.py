import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import tela_largura, tela_altura, tela_resolucao, tela

#Esqueletos

class ExibicaoImagemEstatica():

	def __init__(self, pos_x, pos_y):
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio_ext/fundo.png').convert()
		self.pos_x = pos_x
		self.pos_y = pos_y
		
		self.porcentagem_pos_x = 0
		self.porcentagem_pos_y = 0

		self.largura = 1080
		self.altura = 2020

		self.largura_transformada = 0
		self.altura_transformada = 0
		self.transformado = 0

		self.automatico()

	def porcentagem_pos(self):
		largura = tela_largura[tela_resolucao]
		altura = tela_altura[tela_resolucao]

		self.porcentagem_pos_x = largura / 100 * self.pos_x
		self.porcentagem_pos_y = altura / 100 * self.pos_y

	def transformando_resolucao(self):

		largura_ratio = tela_largura[tela_resolucao] / tela_largura[2]
		altura_ratio = tela_altura[tela_resolucao] / tela_altura[2]

		self.largura_transformada = self.largura * largura_ratio
		self.largura_transformada = round(self.largura_transformada)
		self.altura_transformada = self.altura * altura_ratio
		self.altura_transformada = round(self.altura_transformada)

	def transformando_imagem(self):
		self.transformado = pygame.transform.smoothscale(self.imagem, (self.largura_transformada, self.altura_transformada))

	def automatico(self):
		self.porcentagem_pos()
		self.transformando_resolucao()
		self.transformando_imagem()

	def desenho(self):

		if self.pos_x == 0 and self.pos_y == 0:
			tela.blit(self.transformado, (self.pos_x, self.pos_y))

		else:
			tela.blit(self.transformado, (self.porcentagem_pos_x, self.porcentagem_pos_y))

class Escrever(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y, tipo, frase, cor, alinhamento = 'esquerda'):
		super().__init__(pos_x, pos_y)
		self.tipo = tipo
		self.frase = frase
		self.cor = cor
		self.alinhamento = alinhamento
		self.tamanho = 1

		self.largura = 40
		self.altura = 60

		self.porcentagem_pos()
		self.mudando_tamanho()
		self.mudando_cor()

		self.fonte = pygame.font.Font('modulos/pixelmix.ttf', self.tamanho)

		self.texto = self.fonte.render(self.frase, True, self.cor)
	
	def mudando_tamanho(self):
		if self.tipo == 'titulo':
			if tela_resolucao == 0:
				self.tamanho = 12

			elif tela_resolucao == 1:
				self.tamanho = 18

			elif tela_resolucao == 2:
				self.tamanho = 27

			elif tela_resolucao == 3:
				self.tamanho = 41

		if self.tipo == 'botao':
			if tela_resolucao == 0:
				self.tamanho = 16

			elif tela_resolucao == 1:
				self.tamanho = 24

			elif tela_resolucao == 2:
				self.tamanho = 38

			elif tela_resolucao == 3:
				self.tamanho = 58

		if self.tipo == 'corpo':
			if tela_resolucao == 0:
				self.tamanho = 14

			elif tela_resolucao == 1:
				self.tamanho = 21

			elif tela_resolucao == 2:
				self.tamanho = 32

			elif tela_resolucao == 3:
				self.tamanho = 47
		
		if self.tipo == 'item':
			if tela_resolucao == 0:
				self.tamanho = 10

			elif tela_resolucao == 1:
				self.tamanho = 15

			elif tela_resolucao == 2:
				self.tamanho = 22

			elif tela_resolucao == 3:
				self.tamanho = 34

	def mudando_cor(self):
		if self.cor == 'preto':
			self.cor = (0, 0, 0)
		elif self.cor == 'vermelho':
			self.cor = (150, 0, 0)
		elif self.cor == 'verde':
			self.cor = (0, 150, 0)
		elif self.cor == 'azul':
			self.cor = (0, 0, 150)
		else:
			pass

	def desenho(self):
		espaco_do_texto = self.texto.get_rect()
		if self.alinhamento == 'esquerda':
			espaco_do_texto.topleft = (self.porcentagem_pos_x, self.porcentagem_pos_y)
		if self.alinhamento == 'centro':
			espaco_do_texto.center = (self.porcentagem_pos_x, self.porcentagem_pos_y)
		if self.alinhamento == 'direita':
			espaco_do_texto.topright = (self.porcentagem_pos_x, self.porcentagem_pos_y)
		tela.blit(self.texto, espaco_do_texto)

class Loading(ExibicaoImagemEstatica):

	def __init__(self, pos_x, pos_y, porcentagem_de_carregamento):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/b_loading/loading/janela_loading.png').convert_alpha()

		self.largura = 483
		self.altura = 216

		self.porcentagem_de_carregamento = porcentagem_de_carregamento

		self.texto_loading = Escrever(self.pos_x + 2, self.pos_y + 1, 'titulo', 'Loading', 'preto')
		self.texto_carregando = Escrever(self.pos_x + 22.3, self.pos_y + 5.5, 'titulo', 'Carregando', 'preto', 'centro')
		self.texto_carregamento = Escrever(self.pos_x + 22.3, self.pos_y + 7.5, 'titulo', self.porcentagem_de_carregamento + '%', 'preto', 'centro')

		self.automatico()

	def desenho(self):

		tela.blit(self.transformado, (self.porcentagem_pos_x, self.porcentagem_pos_y))
		self.texto_loading.desenho()
		self.texto_carregando.desenho()
		self.texto_carregamento = Escrever(self.pos_x + 22.3, self.pos_y + 8.1, 'titulo', self.porcentagem_de_carregamento + '%', 'preto', 'centro')
		self.texto_carregamento.desenho()

def transicao(tela_largura, tela_altura, velocidade): 
    transicao = pygame.Surface((tela_largura, tela_altura))
    transicao.fill((0,0,0))
    for alpha in range(0, 300):
        transicao.set_alpha(alpha)
        #redesenho_fundo()
        tela.blit(transicao, (0,0))
        pygame.display.update()
        pygame.time.delay(velocidade)
