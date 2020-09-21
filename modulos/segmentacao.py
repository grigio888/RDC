import pygame

# variaveis

tela_largura = (480, 720, 1080, 1440)
tela_altura = (960, 1440, 2160, 2960)
tela_resolucao = 0
tela = pygame.display.set_mode((tela_largura[tela_resolucao], tela_altura[tela_resolucao]))
icone = pygame.image.load('modulos/icon.png')
pygame.display.set_icon(icone)
pygame.display.set_caption("Ragnarok Dugeon Crawler")
relogio_de_atualizacao = pygame.time.Clock()
ponteiro = 30

game_rodando = True
setor = 'pagina inicial'
subsetor = 'inicio'

def capturar_posicao_mouse():
    largura = tela_largura[tela_resolucao]
    altura = tela_altura[tela_resolucao]
    porcentagem_pos_x = pygame.mouse.get_pos()[0] / largura * 100
    porcentagem_pos_y = pygame.mouse.get_pos()[1] / altura * 100
    return [porcentagem_pos_x, porcentagem_pos_y]

# segmentacao de setores:

# SETOR 'pagina inicial':
# subsetor 'inicio':

from modulos.setores.a_pagina_inicial.inicio import *

# subsetor 'opcoes':

from modulos.setores.a_pagina_inicial.opcoes import *

# SETOR 'loading':

from modulos.setores.b_loading.loading import *

# SETOR 'inicio':
# subsetor 'landing page':

from modulos.setores.c_inicio.landing_page import *
