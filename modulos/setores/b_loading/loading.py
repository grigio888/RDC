import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.classes import *

loading_display = '000'

pygame.init()

texto_loading = Escrever(7, 68.2, 'titulo', 'Loading', 'preto')
texto_carregamento = Escrever(50, 75, 'titulo', loading_display, 'preto', 'centro')

def desenho_pagina_loading():
    fundo.desenho()

    janela_inicio.desenho()
    texto_loading.desenho()
    texto_carregamento.desenho()
