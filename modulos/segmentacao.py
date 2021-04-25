import pygame, sys

sys.path.append('C:/Users/Grigio/Desktop/GitHub/RDC')

# variaveis

tela_largura = (385, 480, 720, 768, 1080, 1440)
tela_altura = (720, 897, 1346, 1435, 2020, 2694)
tela_resolucao = 0
tela = pygame.display.set_mode((tela_largura[tela_resolucao], tela_altura[tela_resolucao]), pygame.SCALED)

icone = pygame.image.load('modulos/icon.png')
pygame.display.set_icon(icone)
pygame.display.set_caption("Ragnarok Dugeon Crawler")
relogio_de_atualizacao = pygame.time.Clock()
ponteiro = 30

pygame.mouse.set_visible(False)

game_rodando = True
setor = 'pagina inicial'
subsetor = 'inicio'

from modulos.classes import *

som_clique = pygame.mixer.Sound('modulos/som/sfx/mouse/click.ogg')
mouse = Mouse()

for event in pygame.event.get():
    pass

#########################################################################

def mouse_colidindo(objeto):
    variavel = pygame.Rect.colliderect(mouse.retangulo, objeto.retangulo)
    if variavel:
        mouse.estado_mouse = 'apontador'
        return variavel
    if not variavel:
        mouse.estado_mouse = 'standby'

def mouse_clicando():
    variavel = pygame.mouse.get_pressed()[0]
    if variavel:
        som_clique.play()
        return variavel


from modulos.setores.a_pagina_inicial.inicio import *