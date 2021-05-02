import pygame, sys
import sqlite3

sys.path.append('C:/Users/Grigio/Desktop/GitHub/RDC')

from modulos.segmentacao import *

tela_tamanho = pygame.display.get_window_size()
som_clique = pygame.mixer.Sound('modulos/som/sfx/mouse/click.ogg')

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
		self.retangulo = 0
		self.criando_retangulo()

	def porcentagem_pos(self):
		self.porcentagem_pos_x = tela_tamanho[0] / 100 * self.pos_x
		self.porcentagem_pos_y = tela_tamanho[1] / 100 * self.pos_y

	def transformando_resolucao(self):
		self.largura_transformada = round(self.largura * (tela_tamanho[0] / 1080))
		self.altura_transformada = round(self.altura * (tela_tamanho[1] / 2020))

	def transformando_imagem(self):
		self.transformado = pygame.transform.smoothscale(self.imagem.convert_alpha(), (self.largura_transformada, self.altura_transformada))

	def automatico(self):
		self.porcentagem_pos()
		self.transformando_resolucao()
		self.transformando_imagem()

	def criando_retangulo(self):
		self.retangulo = pygame.Rect(self.porcentagem_pos_x, self.porcentagem_pos_y, self.largura_transformada, self.altura_transformada)

	def desenho(self):
		tela.blit(self.transformado, (self.porcentagem_pos_x, self.porcentagem_pos_y))

class ExibirImagemInterativa(ExibirImagem):

	def __init__(self, caminho, caminho2, estado, largura, altura, pos_x, pos_y):
		super().__init__(caminho, largura, altura, pos_x, pos_y)
		self.caminho2 = caminho2
		self.estado = estado
		self.estado_int = int(self.estado)
		self.verificando_estado()

	def verificando_estado(self):
		if self.estado:
			self.imagem = pygame.image.load(self.caminho)
		if not self.estado:
			self.imagem = pygame.image.load(self.caminho2)

	def mudanca_de_estado(self):
		if self.estado:
			self.imagem = pygame.image.load(self.caminho2)
			self.estado = not self.estado
		else:
			self.imagem = pygame.image.load(self.caminho)
			self.estado = not self.estado

	def desenho(self):
		self.verificando_estado()
		tela.blit(self.transformado, (self.porcentagem_pos_x, self.porcentagem_pos_y))

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

	def __init__(self, pos_x, pos_y, tipo, frase, cor_escolhida, alinhamento = 'esquerda'):
		self.pos_x = pos_x
		self.pos_y = pos_y
		
		self.tipo = tipo
		self.frase = frase
		self.cor_escolhida = cor_escolhida
		self.cor = 0
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
		self.espaco_do_texto = 0
	
	def porcentagem_pos(self):
		self.porcentagem_pos_x = tela_tamanho[0] / 100 * self.pos_x
		self.porcentagem_pos_y = tela_tamanho[1] / 100 * self.pos_y
	
	def mudando_tamanho(self):
		tamanhos = {'titulo': 27, 'botao': 36, 'corpo': 32, 'item': 22, 'atributo': 30}
		for item in tamanhos:
			if item == self.tipo: tamanho_padrao = tamanhos[item]
		self.tamanho = round((tamanho_padrao * tela_tamanho[0]) / 1080)
		
	def mudando_cor(self):
		cores = {'preto': (0, 0, 0), 'vermelho': (150, 0, 0), 'verde': (0, 150, 0), 'azul': (54, 69, 111), 'cinza': (178, 178, 178)}
		self.cor = cores['preto']
		for item in cores:
			if item == self.cor_escolhida: self.cor = cores[item]

	def definindo_local_escrita(self):
		self.texto = self.fonte.render(self.frase, True, self.cor)
		self.espaco_do_texto = self.texto.get_rect()

	def desenho(self):
		self.definindo_local_escrita()
		if self.alinhamento == 'esquerda':
			self.espaco_do_texto.topleft = (self.porcentagem_pos_x, self.porcentagem_pos_y)
		if self.alinhamento == 'centro':
			self.espaco_do_texto.midtop = (self.porcentagem_pos_x, self.porcentagem_pos_y)
		if self.alinhamento == 'direita':
			self.espaco_do_texto.topright = (self.porcentagem_pos_x, self.porcentagem_pos_y)
		tela.blit(self.texto, self.espaco_do_texto)

class FerramentaBancoDeDados():
	
	def __init__(self, database):
		self.database = database
		self.resultado = 0

	def executar(self, comando):
		login = sqlite3.connect(self.database) #Loga
		cursor = login.cursor() #Aponta
		executar = (comando) #Recebe comando
		cursor.execute(executar) #Executa comando
		login.commit() #Commit
		login.close() #Encerra conexão

	def ler(self, comando):
		login = sqlite3.connect(self.database) #Loga
		cursor = login.cursor() #Aponta
		executar = (comando) #Recebe comando
		cursor.execute(executar) #Executa comando
		self.resultado = cursor.fetchall() #Lê o cursor
		login.close() #Encerra conexão
		return self.resultado


class Mouse():

	def __init__(self):
		self.caminho = 'modulos/pack_img/mouse/mouse_stb_1.png'
		self.imagem = pygame.image.load(self.caminho)
		self.pos_x = 0
		self.pos_y = 0
		self.largura = 26
		self.altura = 31
		self.dimensao_mult = 2
		self.largura_transformada = 0
		self.altura_transformada = 0
		self.transformado = 0

		self.relogio = 0
		self.animacao_frame = 0
		self.estado_mouse = 'standby'
		self.imagens_cursor_standby = ['modulos/pack_img/mouse/mouse_stb_1.png', 'modulos/pack_img/mouse/mouse_stb_2.png', 'modulos/pack_img/mouse/mouse_stb_3.png', 'modulos/pack_img/mouse/mouse_stb_4.png', 'modulos/pack_img/mouse/mouse_stb_5.png', 'modulos/pack_img/mouse/mouse_stb_6.png', ]
		self.imagens_cursor_apontador = ['modulos/pack_img/mouse/mouse_apt_1.png', 'modulos/pack_img/mouse/mouse_apt_2.png']

		self.automatico()
		self.retangulo = pygame.Rect(self.pos_x, self.pos_y, 1, 1)

	def posicao(self):
		self.pos_x = pygame.mouse.get_pos()[0]
		self.pos_y = pygame.mouse.get_pos()[1]
		self.retangulo = pygame.Rect(self.pos_x, self.pos_y, 1, 1)

	def transformando_resolucao(self):
		self.largura_transformada = round(self.largura * (tela_tamanho[0] / 1080))
		self.altura_transformada = round(self.altura * (tela_tamanho[1] / 2020))

	def transformando_imagem(self):
		self.transformado = pygame.transform.smoothscale(self.imagem.convert_alpha(), (round((self.largura_transformada * self.dimensao_mult)), round((self.altura_transformada* self.dimensao_mult))))

	def automatico(self):
		self.posicao()
		self.transformando_resolucao()
		self.transformando_imagem()

	def animacao(self):
		self.relogio += 1
		if self.estado_mouse == 'apontador':
			self.dimensao_mult = 2.5
			if not pygame.mouse.get_pressed()[0]:
				self.imagem = pygame.image.load(self.imagens_cursor_apontador[0])
				self.transformando_imagem()
			if pygame.mouse.get_pressed()[0]:
				self.imagem = pygame.image.load(self.imagens_cursor_apontador[1])
				self.transformando_imagem()
		else:
			self.dimensao_mult = 2
			if self.relogio > 49 and self.relogio % 2 == 0: self.animacao_frame += 1
			if self.relogio >= 60:
				self.relogio = 0
				self.animacao_frame = 0
			if self.animacao_frame >= len(self.imagens_cursor_standby): self.animacao_frame = 0
			self.imagem = pygame.image.load(self.imagens_cursor_standby[self.animacao_frame])
			self.transformando_imagem()


	def desenho(self):
		self.posicao()
		self.animacao()
		tela.blit(self.transformado, (self.pos_x, self.pos_y))


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


def atualizacao_da_tela():
	pygame.display.update()
	relogio_de_atualizacao.tick(ponteiro)
	tela_tamanho = pygame.display.get_window_size()


############################################################################################################

class Personagem():
	def __init__(self, nome, cabelo, classe, atributos, pos_x, pos_y):
		self.nome = nome
		self.cabelo = cabelo
		self.classe = classe

		self.atributos = atributos

		self.acao = 'parado'

		self.pos_x = pos_x
		self.pos_y = pos_y
		self.porcentagem_pos_x = 0
		self.porcentagem_pos_y = 0
		self.largura = 0
		self.altura = 0
		self.largura_transformada = 0
		self.altura_transformada = 0
		self.transformado = 0

	def mudando_cabelo(self, comando):
		
		if comando == 'anterior':
			pass


############################################################################################################

def pressionar_botao(botao):
	if pygame.mouse.get_pos()[0] >= botao.porcentagem_pos_x and pygame.mouse.get_pos()[1] >= botao.porcentagem_pos_y and pygame.mouse.get_pos()[0] <= botao.porcentagem_pos_x + botao.largura_transformada and pygame.mouse.get_pos()[1] <= botao.porcentagem_pos_y + botao.altura_transformada:
		som_clique.play()
		return True
	else:
		return False