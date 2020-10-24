import pygame

# variaveis

tela_largura = (480, 720, 1080, 1440)
tela_altura = (897, 1346, 2020, 2694)
tela_resolucao = 0
tela = pygame.display.set_mode((tela_largura[tela_resolucao], tela_altura[tela_resolucao]))
icone = pygame.image.load('modulos/icon.png')
pygame.display.set_icon(icone)
pygame.display.set_caption("Ragnarok Dugeon Crawler")
relogio_de_atualizacao = pygame.time.Clock()
ponteiro = 60

game_rodando = True
setor = 'pagina inicial'
subsetor = 'inicio'

def capturar_posicao_mouse():
    largura = tela_largura[tela_resolucao]
    altura = tela_altura[tela_resolucao]
    porcentagem_pos_x = pygame.mouse.get_pos()[0] / largura * 100
    porcentagem_pos_y = pygame.mouse.get_pos()[1] / altura * 100
    return [porcentagem_pos_x, porcentagem_pos_y]

from modulos.setores.a_pagina_inicial.inicio import *