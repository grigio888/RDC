import pygame
import sys

sys.path.append('C:/Users/Pri e Vini/Desktop/Projetos/004 - RDC')

from modulos.segmentacao import tela_largura, tela_altura, tela_resolucao, tela

# classes

# SETOR Pagina Inicial
# subsetor inicio:
class Fundo():

	def __init__(self, pos_x, pos_y):
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio/fundo.png').convert()
		self.pos_x = pos_x
		self.pos_y = pos_y
		
		self.porcentagem_pos_x = 0
		self.porcentagem_pos_y = 0

		self.largura = 1080
		self.altura = 2160

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

class Logo(Fundo):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio/logo.png')

		self.largura = 950
		self.altura = 600

		self.automatico()

class JanelaInicio(Fundo):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio/janela_inicio.png')

		self.largura = 972
		self.altura = 414

		self.automatico()

class Botao(Fundo):

	def __init__(self, pos_x, pos_y, botao):
		super().__init__(pos_x, pos_y)
		self.botao = botao

		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio/botao_largo.png')

		self.largura = 431
		self.altura = 69

		self.definir_botao()
		self.automatico()

	def definir_botao(self):
		if self.botao == 'largo':
			self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio/botao_largo.png')
			self.largura = 431
			self.altura = 69

		elif self.botao == 'opcoes':
			self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/inicio/botao_opcoes.png')
			self.largura = 69
			self.altura = 69

		elif self.botao == 'curto':
			self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes/botao_curto.png')
			self.largura = 106
			self.altura = 69

# subsetor opcoes:

class JanelaOpcoes(Fundo):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes/janela_opcoes.png')

		self.largura = 920
		self.altura = 539

		self.automatico()

class CaixaConfirmadora(Fundo):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes/caixa_marcada.png')

		self.marcado = True

		self.largura = 35
		self.altura = 35

		self.automatico()

	def mudanca_de_estado(self, valor):
		if valor == 1:
			if self.marcado:
				self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes/caixa_nao_marcada.png')
				self.marcado = not self.marcado
			else:
				self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes/caixa_marcada.png')
				self.marcado = not self.marcado

class Escrever(Fundo):

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
		
class BDIEsteira(Fundo):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes/barra_intensidade_esteira.png')

		self.largura = 542
		self.altura = 32

		self.automatico()

class BDISetas(Fundo):

	def __init__(self, pos_x, pos_y, estado):
		super().__init__(pos_x, pos_y)
		self.imagem = 0
		self.menor = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes/barra_intensidade_menor.png')
		self.maior = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes/barra_intensidade_maior.png')

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

class EsferaMarcadora(Fundo):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/a_pagina_inicial/opcoes/esfera_marcadora.png')

		self.largura = 27
		self.altura = 32

		self.automatico()

# SETOR Loading:

def transicao(tela_largura, tela_altura, velocidade): 
    transicao = pygame.Surface((tela_largura, tela_altura))
    transicao.fill((0,0,0))
    for alpha in range(0, 300):
        transicao.set_alpha(alpha)
        #redesenho_fundo()
        tela.blit(transicao, (0,0))
        pygame.display.update()
        pygame.time.delay(velocidade)


# SETOR Inicio:
# subsetor Landing Page:

class FundoInicio(Fundo):

	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/fundo.png')

		self.automatico()

class JanelaLanding(Fundo):

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
			self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/janela_cima.png')
			self.largura = 972
			self.altura = 333

		elif self.janela == 'meio':
			self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/janela_meio.png')
			self.largura = 972
			self.altura = 1244

		elif self.janela == 'baixo':
			self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/janela_baixo.png')
			self.largura = 972
			self.altura = 333

class Frames(Fundo):

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
			self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/frame_personagem.png')
			self.largura = 404
			self.altura = 517

		elif self.parte == 'sombra':
			self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/frame_sombra.png')
			self.largura = 165
			self.altura = 94

		elif self.parte == 'frame_item':
			self.imagem = pygame.image.load('modulos/setores/c_inicio/landing_page/frame_item.png')
			self.largura = 210
			self.altura = 240

class ImagemItem(Fundo):

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
		self.imagem = pygame.image.load(caminho)

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