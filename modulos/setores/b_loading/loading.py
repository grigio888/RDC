import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.setores.b_loading.loading_classes import *

pygame.init()

janela_loading = JanelaLoading(27.7, 70.5)
texto_loading = Escrever(29.7, 71.5, 'titulo', 'Loading', 'preto')
texto_carregando = Escrever(50, 76.5, 'titulo', 'Carregando', 'preto', 'centro')

def desenho_pagina_loading():
    fundo.desenho()

    janela_loading.desenho()
    texto_loading.desenho()
    texto_carregando.desenho()
