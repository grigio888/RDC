import pygame, sys
from modulos.segmentacao import *

sys.path.append(caminho_raiz_pc)

tela_tamanho = pygame.display.get_window_size()

#Esqueletos

class ExibirImagem():

	def __init__(self, caminho, largura, altura, pos_x, pos_y):
		self.caminho = caminho
		self.imagem = pygame.image.load(self.caminho)
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.porcentagem_pos_x = 0
		self.porcentagem_pos_y = 0
		self.largura = largura
		self.altura = altura
		self.largura_transformada = 0
		self.altura_transformada = 0
		self.transformado = 0
		self.automatico()

	def porcentagem_pos(self):
		self.porcentagem_pos_x = tela_tamanho[0] / 100 * self.pos_x
		self.porcentagem_pos_y = tela_tamanho[1] / 100 * self.pos_y

	def transformando_resolucao(self):
		if tela_cheia:
			self.largura_transformada = round(self.largura * (tela_tamanho[1] / 1080))
			self.altura_transformada = round(self.altura * ((tela_tamanho[1] / 1080) * 1.87))
		if not tela_cheia:
			self.largura_transformada = round(self.largura * (tela_tamanho[0] / 1080))
			self.altura_transformada = round(self.altura * (tela_tamanho[1] / 2020))

	def transformando_imagem(self):
		self.transformado = pygame.transform.smoothscale(self.imagem.convert_alpha(), (self.largura_transformada, self.altura_transformada))

	def automatico(self):
		self.porcentagem_pos()
		self.transformando_resolucao()
		self.transformando_imagem()

	def desenho(self):
		tela.blit(self.transformado, (self.porcentagem_pos_x, self.porcentagem_pos_y))

class ExibirImagemInterativa(ExibirImagem):

	def __init__(self, caminho, caminho2, largura, altura, pos_x, pos_y):
		super().__init__(caminho, largura, altura, pos_x, pos_y)
		self.caminho2 = caminho2
		self.estado = True

	def mudanca_de_estado(self):
		if self.estado:
			self.imagem = pygame.image.load(self.caminho2)
			self.estado = not self.estado
			self.desenho()
		else:
			self.imagem = pygame.image.load(self.caminho)
			self.estado = not self.estado
			self.desenho()

class ExibirItem(ExibirImagem):

	def __init__(self, pos_x, pos_y, item_ID, tamanho, escala_de_tamanho = 1):
		self.pos_x = pos_x
		self.pos_y = pos_y
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
		self.transformando_imagem()
		

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
		self.largura_transformada = round(self.largura_transformada * self.escala_de_tamanho)
		self.altura_transformada = round(self.altura_transformada * self.escala_de_tamanho)
		
		self.transformado = pygame.transform.smoothscale(self.imagem, (self.largura_transformada, self.altura_transformada))


class Escrever():

	def __init__(self, pos_x, pos_y, tipo, frase, cor, alinhamento = 'esquerda'):
		self.pos_x = pos_x
		self.pos_y = pos_y
		
		self.tipo = tipo
		self.frase = frase
		self.cor = cor
		self.alinhamento = alinhamento
		self.tamanho = 1

		self.largura = 40
		self.altura = 60
		
		self.porcentagem_pos_x = 0
		self.porcentagem_pos_y = 0

		self.porcentagem_pos()
		self.mudando_tamanho()
		self.mudando_cor()

		self.fonte = pygame.font.Font('modulos/pixelmix.ttf', self.tamanho)
	
	def porcentagem_pos(self):
		self.porcentagem_pos_x = tela_tamanho[0] / 100 * self.pos_x
		self.porcentagem_pos_y = tela_tamanho[1] / 100 * self.pos_y
	
	def mudando_tamanho(self):
		if self.tipo == 'titulo':
			tamanho_padrao = 27
			self.tamanho = round((tamanho_padrao * tela_tamanho[0]) / 1080)

		if self.tipo == 'botao':
			tamanho_padrao = 36
			self.tamanho = round((tamanho_padrao * tela_tamanho[0]) / 1080)

		if self.tipo == 'corpo':
			tamanho_padrao = 32
			self.tamanho = round((tamanho_padrao * tela_tamanho[0]) / 1080)
		
		if self.tipo == 'item':
			tamanho_padrao = 22
			self.tamanho = round((tamanho_padrao * tela_tamanho[0]) / 1080)

		if self.tipo == 'atributo':
			tamanho_padrao = 30
			self.tamanho = round((tamanho_padrao * tela_tamanho[0]) / 1080)
		
	def mudando_cor(self):
		if self.cor == 'preto':
			self.cor = (0, 0, 0)
		elif self.cor == 'vermelho':
			self.cor = (150, 0, 0)
		elif self.cor == 'verde':
			self.cor = (0, 150, 0)
		elif self.cor == 'azul':
			self.cor = (54, 69, 111)
		else:
			pass
			
	def desenho(self):
		self.texto = self.fonte.render(self.frase, True, self.cor)
		espaco_do_texto = self.texto.get_rect()
		if self.alinhamento == 'esquerda':
			espaco_do_texto.topleft = (self.porcentagem_pos_x, self.porcentagem_pos_y)
		if self.alinhamento == 'centro':
			espaco_do_texto.midtop = (self.porcentagem_pos_x, self.porcentagem_pos_y)
		if self.alinhamento == 'direita':
			espaco_do_texto.topright = (self.porcentagem_pos_x, self.porcentagem_pos_y)
		tela.blit(self.texto, espaco_do_texto)

class Loading(ExibirImagem):

	def __init__(self, pos_x, pos_y, porcentagem_de_carregamento):
		super().__init__(pos_x, pos_y)
		self.imagem = pygame.image.load('modulos/setores/loading/janela_loading.png').convert_alpha()

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

def capturar_posicao_mouse():
    largura = tela_largura[tela_resolucao]
    altura = tela_altura[tela_resolucao]
    porcentagem_pos_x = pygame.mouse.get_pos()[0] / largura * 100
    porcentagem_pos_y = pygame.mouse.get_pos()[1] / altura * 100
    return [porcentagem_pos_x, porcentagem_pos_y]

def transicao(tela_largura, tela_altura, velocidade): 
    transicao = pygame.Surface((tela_largura, tela_altura))
    transicao.fill((0,0,0))
    for alpha in range(0, 300):
        transicao.set_alpha(alpha)
        #redesenho_fundo()
        tela.blit(transicao, (0,0))
        pygame.display.update()
        pygame.time.delay(velocidade)
