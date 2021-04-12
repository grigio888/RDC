import pygame, sys

caminho_raiz_pc = 'D:/Vini/Projetos/004 - RDC'
caminho_raiz_cel = '/storage/emulated/0/RDC'

sys.path.append(caminho_raiz_pc)

# variaveis

tela_cheia = False

if tela_cheia:
    tela_largura = (480, 720, 1080, 1440)
    tela_altura = (897, 1346, 2020, 2694)
    tela_resolucao = 2
    tela = pygame.display.set_mode((tela_largura[tela_resolucao], tela_altura[tela_resolucao]), pygame.SCALED | pygame.FULLSCREEN)
    variavel_daqui = pygame.display.get_window_size()
    tela_largura = variavel_daqui[1]
    tela_altura = round(tela_largura * 1.87)
    tela = pygame.display.set_mode((tela_largura, tela_altura), pygame.SCALED | pygame.FULLSCREEN)

if not tela_cheia:
    tela_largura = (480, 720, 1080, 1440, 385)
    tela_altura = (897, 1346, 2020, 2694, 720)
    tela_resolucao = 4
    tela = pygame.display.set_mode((tela_largura[tela_resolucao], tela_altura[tela_resolucao]), pygame.SCALED)

icone = pygame.image.load('modulos/icon.png')
pygame.display.set_icon(icone)
pygame.display.set_caption("Ragnarok Dugeon Crawler")
relogio_de_atualizacao = pygame.time.Clock()
ponteiro = 30

game_rodando = True
setor = 'pagina inicial'
subsetor = 'inicio'

from modulos.setores.a_pagina_inicial.inicio import *
from modulos.classes import *

som_clique = pygame.mixer.Sound('modulos/som/sfx/mouse/click.ogg')